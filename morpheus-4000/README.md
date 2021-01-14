# Morpheus-4000

## Chain ID
```sh
morpheus-4000
```

## Genesis Time
```sh
2020-04-25T10:00:00Z
```

## Desmos Version
```sh
v0.4.0
```

```sh
desmosd version --long
name: Desmos
server_name: desmosd
client_name: desmoscli
version: 0.4.0-6-g7c7caa9
commit: 7c7caa9295bfb0320d06eb3be47d4c4fed15975b 
build_tags: netgo ledger
go: go version go1.13.5 darwin/amd64
```

## Genesis state
Genesis state was exported from `morpheus-3000` at height [`845600`](https://morpheus-3000.desmos.network/blocks/845600).

## Genesis file hash
You can verify with the sorted genesis file.

```sh
jq -S -c -M '' genesis.json | shasum -a 256
dc6bcadf360f037450066bfad89bc54c467810240ac93a317bf5f26cab80079f  -
```

## Persistent Peers
```sh
e30d9bb713d17d1e4380b2e2a6df4b5c76c73eb1@34.212.106.82:26656
```

## Parameters

### Slashing

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

## Tokens
__Staking__ : `udaric` \
__Fee__ : `upotin`

## Faucet
https://faucet.desmos.network
