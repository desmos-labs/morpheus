#######
# This script allows you to rollback to morpheus-4001 after you have updated to another chain version
#######

# Copy your private validator key to a safe place
cp ~/.desmosd/config/priv_validator_key.json ~/priv_validator_key.json

# Delete the validator key to avoid double signature
rm ~/.desmosd/config/priv_validator_key.json

# Reset your node
desmosd unsafe-reset-all

# Copy the chain genesis file
curl https://raw.githubusercontent.com/desmos-labs/morpheus/master/5000/genesis.json > ~/.desmosd/config/genesis.json

# Copy the ZIP file into your ~/.desmosd/data folder an unzip it
cd ~/.desmosd/data
curl https://ipfs.desmos.network/ipfs/QmefdkfymvZ23VNz563YNqknd3zUqLsL4kVGJzKw6Dyvw5 > ~/.desmosd/data/data.zip
unzip data.zip

# Start the node
desmosd start

# Once the node has correctly synced, then stop it and restore your validator key
cp ~/priv_validator_key ~/.desmosd/config/priv_validator_key.json

# Start the node again
desmosd start
