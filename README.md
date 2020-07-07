# Morpheus testnets
> Official repository containing all the [Desmos](https://github.com/desmos-labs/desmos) testnets' data.

## Latest running testnet

### Chain data
| Data | Value | 
| :--- | :---: |
| Genesis file |  [genesis file](genesis.json) |
| Chain ID | `morpheus-4001` |
| Genesis time | `2020-05-20T10:00:00Z` |

### Desmos Version
```sh
$ desmosd version --long
name: Desmos
server_name: desmosd
client_name: desmoscli
version: 0.5.3
commit: 4af60f6b12a6f8de50b0873974efaf6e4630b592
build_tags: netgo ledger
go: go version go1.14.4 linux/amd64
```

To checkout this version run: 

```
git checkout tags/v0.5.3
```

### Genesis state
The genesis state was exported from `morpheus-4000` at height [`380000`](https://morpheus-4000.desmos.network/blocks/380000).

### Genesis file hash
You can verify with the sorted genesis file.

```sh
jq -S -c -M '' genesis.json | shasum -a 256
f15c917929e670f0d8aa45aba95122ba39aaba52d6f1a921a7ae25a88c9f7281  -
```

### Persistent Peers
```sh
7fed5624ca577eb0333d3631b5e4f16ba1736979@54.180.98.75:26656
```

### Parameters

#### Slashing
```json
{
  "downtime_jail_duration": "600000000000",
  "max_evidence_age": "120000000000",
  "min_signed_per_window": "0.050000000000000000",
  "signed_blocks_window": "720", // approximately 1 hour with 5 seconds block
  "slash_fraction_double_sign": "0.050000000000000000", // validator will be jailed for downtime if missing 684 blocks in 1 hour
  "slash_fraction_downtime": "0.010000000000000000"
}
```

### Tokens
__Staking__ : `udaric` \
__Fee__ : `upotin`

### Faucet
https://faucet.desmos.network
