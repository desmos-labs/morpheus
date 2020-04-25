# Morpheus Testnets

This is the repositary for all the Morpheus testnets of Desmos.

## Latest Testnet

The latest [genesis file](4000/genesis.json).

### Chain ID

```sh
morpheus-4000
```

### Genesis Time

```sh
2020-04-25T10:00:00Z
```

### Desmos Version

```sh
v0.4.0
```

```sh
desmosd version --long
name: Desmos
server_name: desmosd
client_name: desmoscli
version: 0.4.0
commit: 17cea9ac894298cd1ebc8c0287447e6c5fd12ca7
build_tags: netgo ledger
go: go version go1.13.5 darwin/amd64
```

### Genesis state

Genesis state was exported from `morpheus-3000` at height `845600`.

### Genesis file hash

You can verify with the sorted genesis file.

```sh
jq -S -c -M '' genesis.json | shasum -a 256
65948c4ac43b8765b526a39316ac3dd57c36abad8bdff847f101d1d22249f2d7  -
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

https://faucet.desmos.networks
