# Morpheus testnets
> Official repository containing all the [Desmos](https://github.com/desmos-labs/desmos) testnets' data.

## Latest running testnet

### Chain data
| Data | Value | 
| :--- | :---: |
| Genesis file |  [genesis file](genesis.json) |
| Chain ID | `morpheus-8000` |
| Genesis time | `2020-08-25T05:30:00Z` |

### Desmos Version
```sh
$ desmosd version --long
name: Desmos
server_name: desmosd
client_name: desmoscli
version: 0.10.0
commit: fd8060a0651aec7e0059d63eecf58dc2a2a4a6e0
build_tags: netgo ledger
go: go version go1.14.7 linux/amd64
```

To checkout this version run: 

```
git checkout tags/v0.10.0
```

### Genesis state
The genesis state was exported from `morpheus-7001` at height [`733,000`](https://morpheus-7001.desmos.network/blocks/733000).

### Genesis file hash
You can verify with the sorted genesis file.

```sh
jq -S -c -M '' genesis.json | shasum -a 256
1c7c1cda03ea677b4320015af8e87b7b5c31ad95060cb3ef948c9de135331a81  -
```

### Seed Nodes
```sh
08c7b07000675ed6c0872f9a95075e5e9bc2e619@18.162.149.156:26656
```

### Persistent Peers
```sh
7fed5624ca577eb0333d3631b5e4f16ba1736979@54.180.98.75:26656
```
[A list of community peers](PEERS.md).

### Parameters

#### Slashing
| Parameter | Value | Description |
| :-------: | :---: | :---------- |
| `downtime_jail_duration` | `600000000000` | 10 minutes |
| `max_evidence_age` |  `1200000000000` | 20 minutes |
| `min_signed_per_window` |  `0.050000000000000000` | |
| `signed_blocks_window` |  `720` | Validator will be jailed for downtime if  missing 684 blocks, approximately 1 hour with 5 seconds block |
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
