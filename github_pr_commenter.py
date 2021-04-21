import json
import os
import sys
import time

import requests

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token {token}".format(token=os.getenv("GITHUB_TOKEN"))
}

HOST = "https://api.github.com"
PR_LIST_ENDPOINT = "{host}/repos/{owner}/{repo}/pulls".format(host=HOST, owner="desmos-labs", repo="morpheus")
PR_DETAILS_ENDPOINT = "{host}/repos/{owner}/{repo}/pulls".format(host=HOST, owner="desmos-labs", repo="morpheus")


def execute_command(command):
    os.system("{command}".format(command=command))


def get_prs(filters=''):
    return requests.get(PR_LIST_ENDPOINT + filters, headers=HEADERS).json()


def find_not_bot_prs(prs):
    not_bot_prs = []
    for pr in prs:
        is_not_bot = False
        is_invalid = False
        for label in pr['labels']:
            if label['name'] == 'not-bot':
                is_not_bot = True

            if label['name'] == 'invalid':
                is_invalid = True

        if is_not_bot and not is_invalid:
            not_bot_prs.append(pr)

    return not_bot_prs


def checkout_pr(username):
    execute_command("/bin/bash /home/riccardo/.config/JetBrains/PyCharm2021.1/scratches/checkout.sh {user}".format(
        user=username
    ))


def merge_master_and_remove_genesis(username, ref):
    execute_command("git pull -X theirs")
    execute_command("git pull -X theirs origin master")

    print("Reverting genesis file")
    execute_command(
        "curl https://raw.githubusercontent.com/desmos-labs/morpheus/master/morpheus-apollo-1/genesis.json > "
        "morpheus-apollo-1/genesis.json"
    )
    execute_command("git add morpheus-apollo-1/genesis.json")
    execute_command("git commit -m 'Updated genesis.json'")

    print("Pushing changes")
    execute_command("git push {username} HEAD:{ref}".format(username=username, ref=ref))


def accept_and_merge_pr(pr):
    pr_url = pr['url']

    approve_url = "{endpoint}/reviews".format(endpoint=pr_url)
    requests.post(approve_url, data=json.dumps({"event": "APPROVE"}), headers=HEADERS).json()

    merged = try_merging_pr(pr_url)
    while not merged:
        time.sleep(5)
        merged = try_merging_pr(pr_url)


def try_merging_pr(url) -> bool:
    pr_details = requests.get(url).json()
    pr_number = pr_details['number']

    print("===> Trying merging pr #{number}".format(number=pr_number))

    mergable = pr_details['mergeable']
    if mergable:
        merge_url = "{endpoint}/merge".format(endpoint=url)
        response = requests.put(merge_url, data=json.dumps({
            "commit_title": "Add {username} Apollo gentx".format(username=pr_details['user']['login']),
            "commit_message": "See PR #{number}".format(number=pr_number),
            "merge_method": "squash"
        }), headers=HEADERS).json()
        return response['message'] != 'Pull Request is not mergeable'

    return False


def clean_remote_and_branch(username):
    execute_command("git checkout master")
    execute_command("git branch -D {username}/master".format(username=username))
    execute_command("git remote rm {username}".format(username=username))


def find_duplicate_prs():
    prs = get_prs(filters="?state=all&per_page=100")

    users = []
    duplicate_users = []
    for pr in prs:
        user = pr['user']['login']
        if user in users:
            duplicate_users.append(user)
        else:
            users.append(user)

    return duplicate_users


def update_prs():
    print("===> Getting PRs")
    not_bot_prs = find_not_bot_prs(get_prs(filters="?state=open&per_page=100"))

    print("===> Updating PRs")
    for pr in not_bot_prs:
        username = pr['head']['user']['login']
        print("===> Checking out {} branch".format(username))
        checkout_pr(username)

        print("===> Merging master and removing genesis.json")
        merge_master_and_remove_genesis(username, pr['head']['ref'])

        print("===> Accepting PR")
        accept_and_merge_pr(pr)

        print("===> Cleaning remote and username")
        clean_remote_and_branch(username)

        print("===> Waiting for next PR")
        time.sleep(1)


if __name__ == "__main__":
    try:
        update_prs()
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
