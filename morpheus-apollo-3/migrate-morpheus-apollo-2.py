import json
import sys

if len(sys.argv) < 3:
    raise Exception("Not enough arguments provided. Make sure you specify the input and output file path")

input_file, output_file = sys.argv[1], sys.argv[2]

genesis_state = {}

# Read the exported state
with open(input_file, 'r') as f:
    # Load the exported state
    data = json.load(f)

    # Clean relationships with invalid counterparty
    print("Fixing relationships")
    relationships = []
    for relationship in data['app_state']['relationships']['relationships']:
        if relationship['counterparty'] != "":
            relationships.append(relationship)
    data['app_state']['relationships']['relationships'] = relationships

    # Clean invalid reactions
    reactions = []
    for reaction in data['app_state']['reactions']['reactions']:
        if reaction['subspace_id'] == '5' and reaction['post_id'] == '9' and reaction['id'] == 2:
            continue
        reactions.append(reaction)
    data['app_state']['reactions']['reactions'] = reactions

    # Set the new chain id
    print("Setting new chain id")
    data['chain_id'] = 'morpheus-apollo-3'

    # Set the new genesis time to 24th October 2022, 08:00 UTC
    print("Setting new genesis time")
    data['genesis_time'] = '2022-10-24T08:00:00Z'

    # Store the migrated state as the genesis state
    genesis_state = data

# Dump the genesis state to the proper file
with open(output_file, 'w') as f:
    print("Exporting state")
    json.dump(data, f)
