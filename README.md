# Morpheus testnets
> Official repository containing all the [Desmos](https://github.com/desmos-labs/desmos) testnets' data.

## Latest running testnet

### Chain data
| Data | Value | 
| :--- | :---: |
| Genesis file |  [genesis file](genesis.json) |
| Chain ID | `morpheus-10000` |
| Genesis time | `2020-10-06T06:00:00Z` |

### Desmos Version
```sh
$ desmosd version --long
name: Desmos
server_name: desmosd
client_name: desmoscli
version: 0.12.2
commit: 53442e1c9a6065a7b1fc8eacbb03011fbbe48128
build_tags: netgo ledger
go: go version go1.15.2 linux/amd64
```

To checkout this version run: 

```
git checkout tags/v0.12.2
```

### Genesis state
The genesis state was exported from `morpheus-8000` at height [`513,570`](https://morpheus-8000.desmos.network/blocks/513570).

### Genesis file hash
You can verify the validity of the genesis file by running:

```sh
jq -S -c -M '' genesis.json | shasum -a 256
```

It should return: 

```
bc38f21a896688f06e82b315032a6197bfa07a586d60256e64851c2470a1b5e4  -
```

### Seed Nodes
```sh
08c7b07000675ed6c0872f9a95075e5e9bc2e619@18.162.149.156:26656
```

### Persistent Peers
```sh
7fed5624ca577eb0333d3631b5e4f16ba1736979@54.180.98.75:26656
5077b7964d71d8758f7fc01cac01d0e2d55b8c18@18.196.238.210:26656
bdd98ec74fe56146f08e886239e52373f6821ce3@51.15.113.208:26656
e30d9bb713d17d1e4380b2e2a6df4b5c76c73eb1@34.212.106.82:26656
```

### Parameters

#### Slashing
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

### Tokens
__Staking__ : `udaric` \
__Fee__ : `upotin`

### Faucet
https://faucet.desmos.network
