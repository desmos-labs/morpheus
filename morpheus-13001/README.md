# Morpheus-13001

## Chain data
| Data | Value | 
| :--- | :---: |
| Genesis file |  [genesis file](genesis.json) |
| Chain ID | `morpheus-13001` |
| Genesis time | `2021-01-20T07:00:00Z` |

## Desmos Version
```sh
$ desmos version --long
name: Desmos
server_name: desmos
version: 71da1ea3
commit: 71da1ea3e0292d27047b628afefcff783694e4d8
build_tags: netgo ledger,
go: go version go1.15.6 linux/amd64
```

To checkout this version run: 

```
git checkout tags/v0.15.1
```

## Genesis state
The genesis state was exported from `morpheus-10000` at height [`1,496,100`](https://morpheus-10000.desmos.network/blocks/1496100).

## Genesis file hash
You can verify the validity of the genesis file by running:

```sh
jq -S -c -M '' genesis.json | shasum -a 256
```

It should return:

```
e890563bdd5338743759cc028b118b5ee1825241a3157468f5772993bca19d87  -
```

## Seed Nodes
```sh
```

## Persistent Peers
```sh
1d9cc23eedb2d812d30d99ed12d5c5f21ff40c23@seed-3.morpheus.desmos.network:26656
```

## Parameters

### Slashing
| Parameter | Value | Description |
| :-------: | :---: | :---------- |
| `downtime_jail_duration` | `600000000000` | 10 minutes |
| `max_evidence_age` |  `1200000000000` | 20 minutes |
| `min_signed_per_window` |  `0.050000000000000000` | |
| `signed_blocks_window` |  `720` | Validator will be jailed for downtime if  missing 720 blocks, approximately 1 hour with 5 seconds block |
| `slash_fraction_double_sign` |  `0.050000000000000000` | 5% |
| `slash_fraction_downtime` |  `0.010000000000000000` | 1% |

JSON:
```json
{
  "downtime_jail_duration": "600000000000",
  "max_evidence_age": "120000000000",
  "min_signed_per_window": "0.050000000000000000",
  "signed_blocks_window": "720",
  "slash_fraction_double_sign": "0.050000000000000000",
  "slash_fraction_downtime": "0.010000000000000000"
}
```

## Tokens
__Staking__ : `udaric` \
__Fee__ : `upotin`

## Faucet
https://faucet.desmos.network
