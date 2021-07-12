import json
import sys

with open(sys.argv[1], 'r') as genesis:
    data = json.load(genesis)
    app_state = data['app_state']

    # Get all the profiles addresses
    profiles = []
    for account in app_state['auth']['accounts']:
        # Delete ContinuousVestingAccount implementations since they are not exported properly
        if 'ContinuousVestingAccount' in account['@type']:
            app_state['auth']['accounts'].remove(account)

        elif 'Profile' in account['@type']:
            # Replace moniker -> nickname
            account['nickname'] = account['moniker']
            del account['moniker']

            account_data = account['account']
            if 'PeriodicVestingAccount' in account_data['@type']:
                account_data = account_data['base_vesting_account']['base_account']

            profiles.append(account_data['address'])

    # Delete the relationships that do not involve two profiles
    relationships = []
    for relationship in app_state['profiles']['relationships']:
        if relationship['creator'] in profiles and relationship['recipient'] in profiles:
            relationships.append(relationship)
    app_state['profiles']['relationships'] = relationships

    # -----------------------------
    # Fix the profiles parameters
    profiles_params = app_state['profiles']['params']

    # Change the moniker params to nickname params
    profiles_params['nickname'] = {
        'min_length': profiles_params['moniker_params']['min_moniker_length'],
        'max_length': profiles_params['moniker_params']['max_moniker_length']
    }
    del profiles_params['moniker_params']

    profiles_params['dtag'] = {
        'reg_ex': profiles_params['dtag_params']['reg_ex'],
        'min_length': profiles_params['dtag_params']['min_dtag_length'],
        'max_length': profiles_params['dtag_params']['max_dtag_length']
    }
    del profiles_params['dtag_params']

    profiles_params['bio'] = {
        'max_length': profiles_params['max_bio_length']
    }
    del profiles_params['max_bio_length']

    # Add the oracle params
    profiles_params['oracle'] = {
        'script_id': 32,
        'ask_count': 10,
        'min_count': 6,
        'prepare_gas': 50000,
        'execute_gas': 200000,
        'fee_payer': '',
        'fee_amount': []
    }

    # -----------------------------
    # Update the profiles state

    # Add the IBC port to the profiles state
    app_state['profiles']['ibc_port_id'] = 'ibc-profiles'

    # -----------------------------
    # Fix the IBC state
    app_state['ibc']['channel_genesis']['next_channel_sequence'] = str(
        len(app_state['ibc']['channel_genesis']['channels']))
    app_state['ibc']['client_genesis']['next_client_sequence'] = str(
        len(app_state['ibc']['client_genesis']['clients']))
    app_state['ibc']['connection_genesis']['next_connection_sequence'] = str(
        len(app_state['ibc']['connection_genesis']['connections']))

    # -----------------------------
    # Update chain data
    data['chain_id'] = 'morpheus-apollo-2'
    data['genesis_time'] = '2021-07-13T08:00:00Z'

    with open('morpheus-apollo-2.json', 'w') as f:
        json.dump(data, f)
