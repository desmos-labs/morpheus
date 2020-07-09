# Morpheus testnets
> Official repository containing all the [Desmos](https://github.com/desmos-labs/desmos) testnets' data.

## Latest running testnet

### Chain data
| Data | Value | 
| :--- | :---: |
| Genesis file |  [genesis file](genesis.json) |
| Chain ID | `morpheus-7001` |
| Genesis time | `2020-07-09T10:00:00Z` |

### Desmos Version
```sh
$ desmosd version --long
name: Desmos
server_name: desmosd
client_name: desmoscli
version: 0.8.2
commit: 7d8c261272aba3692fe205d5e473cd469a814de1
build_tags: netgo ledger
go: go version go1.14.4 linux/amd64
```

To checkout this version run: 

```
git checkout tags/v0.8.2
```

### Genesis state
The genesis state was exported from `morpheus-4001` at height [`760000`](https://morpheus-4001.desmos.network/blocks/760000).

### Genesis file hash
You can verify with the sorted genesis file.

```sh
jq -S -c -M '' genesis.json | shasum -a 256
d58db84eb3978e1c290a0fbd4a0606e5d7249fa9543e0643313b86c694cd02f6  -
```

### Persistent Peers
```sh
7fed5624ca577eb0333d3631b5e4f16ba1736979@54.180.98.75:26656
```

### Parameters

#### Slashing
| Parameter | Value | Description |
| :-------: | :---: | :---------- |
| `downtime_jail_duration` | `600000000000` | |
| `downtime_jail_duration` |  `600000000000` | |
| `max_evidence_age` |  `120000000000` | |
| `min_signed_per_window` |  `0.050000000000000000` | |
| `signed_blocks_window` |  `720` | Approximately 1 hour with 5 seconds block |
| `slash_fraction_double_sign` |  `0.050000000000000000` | Validator will be jailed for downtime if  missing 684 blocks in 1 hour
| `slash_fraction_downtime` |  `0.010000000000000000` | |

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

### Tokens
__Staking__ : `udaric` \
__Fee__ : `upotin`

### Faucet
https://faucet.desmos.network
