# Morpheus-13000

## Chain data
| Data | Value | 
| :--- | :---: |
| Genesis file |  [genesis file](genesis.json) |
| Chain ID | `morpheus-13000` |
| Genesis time | `2021-01-19T07:00:00Z` |

## Desmos Version
```sh
$ desmosd version --long
name: Desmos
server_name: desmos
version: dea597f3
commit: dea597f397e3e06dc9d31180b049e788e74b5c29
build_tags: netgo ledger,
go: go version go1.15.6 linux/amd64
```

To checkout this version run: 

```
git checkout tags/v0.15.0
```

## Genesis state
The genesis state was exported from `morpheus-10000` at height [`1,427,500`](https://morpheus-10000.desmos.network/blocks/1427500).

## Genesis file hash
You can verify the validity of the genesis file by running:

```sh
jq -S -c -M '' genesis.json | shasum -a 256
```

It should return:

```
dab31b5a4018f075f5dfbc8e3c9d915b0b3cd87acd0424761284ee56f20c1313  -
```

## Seed Nodes
```sh
e4dfaa271c71f99c6d59bdd179e72373683dab99@seed-1.morpheus.desmos.network:26656
fc4714d15629e3b016847c45d5648230a30a50f1@seed-2.morpheus.desmos.network:26656
edf8602b37af0831ea37fc522f89f57c583c0e4f@seed-3.morpheus.desmos.network:26656
fda7a014490a89c06a4babf0976385891625b8cf@seed-4.morpheus.desmos.network:26656
d40bcb9c71af25c5208dad470e05656490fc2cd3@seed-5.morpheus.desmos.network:26656
```

## Persistent Peers
```sh
7fed5624ca577eb0333d3631b5e4f16ba1736979@54.180.98.75:26656
5077b7964d71d8758f7fc01cac01d0e2d55b8c18@18.196.238.210:26656
bdd98ec74fe56146f08e886239e52373f6821ce3@51.15.113.208:26656
e30d9bb713d17d1e4380b2e2a6df4b5c76c73eb1@34.212.106.82:26656
feb7bb0a271f18092d1058cea4a1ee001875e0fc@176.58.125.142:26656 //Witval
e4bfed146e475dda7dc48a5bf166770d156fb935@172.105.244.118:26656
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
