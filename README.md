# Morpheus Testnets

This is the repositary for all the Morpheus testnets of Desmos.

## Latest Testnet

The latest [genesis file](4001/genesis.json).

### Chain ID

```sh
morpheus-4001
```

### Genesis Time

```sh
2020-05-20T10:00:00Z
```

### Desmos Version

```sh
v0.5.1
```

```sh
desmosd version --long
name: Desmos
server_name: desmosd
client_name: desmoscli
version: 0.5.1
commit: fba4226f61b0a2224c013362fb41d65bd3b663a9
build_tags: netgo ledger
go: go version go1.14.3 linux/amd64
```

### Genesis state

Genesis state was exported from `morpheus-4000` at height [`380000`](https://morpheus-4000.desmos.network/blocks/380000).

### Genesis file hash

You can verify with the sorted genesis file.

```sh
jq -S -c -M '' genesis.json | shasum -a 256
f15c917929e670f0d8aa45aba95122ba39aaba52d6f1a921a7ae25a88c9f7281  -
```

### Persistent Peers

```sh
e30d9bb713d17d1e4380b2e2a6df4b5c76c73eb1@34.212.106.82:26656
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
