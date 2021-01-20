"""
This script allows to migrate a genesis state from morpheus-13000 (based on Desmos v0.15.1)
to morpheus-13001 (based on Desmos v0.15.1).
No major changes are needed, only some renomination of JSON fields.
"""

import json
import sys

with open(sys.argv[1]) as json_file:
    data = json.load(json_file)

    # Migrate chain data
    data['chain_id'] = 'morpheus-13001'
    data['genesis_time'] = '2021-01-20T07:00:00Z'

    # Migrate posts state
    posts_state = data['app_state']['posts']
    for post in posts_state['posts']:
        # Posts' id has been renamed post_id
        post['post_id'] = post.pop('id')

        if 'poll_data' in post:
            for poll_answer in post['poll_data']['provided_answers']:
                # Poll answer's id has been renamed answer_id
                poll_answer['answer_id'] = poll_answer.pop('id')

    # Migrate profiles state
    profiles_state = data['app_state']['profiles']
    moniker_params = profiles_state['params']['moniker_params']
    moniker_params['min_moniker_length'] = moniker_params.pop('min_length')
    moniker_params['max_moniker_length'] = moniker_params.pop('max_length')
    dtag_params = profiles_state['params']['dtag_params']
    dtag_params['min_dtag_length'] = dtag_params.pop('min_length')
    dtag_params['max_dtag_length'] = dtag_params.pop('max_length')

    # Print the result
    print(json.dumps(data))
