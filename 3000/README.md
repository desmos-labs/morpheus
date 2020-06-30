# Morpheus Testnets

This is the repositary for all the Morpheus testnets of Desmos.

## Latest Testnet

The latest [genesis file](3000/genesis.json).

### Chain ID

```sh
morpheus-3000
```

### Genesis Time

```sh
2020-03-01T00:00:00Z
```

### Desmos Version

```sh
v0.3.0
```

```sh
desmosd version --long
name: Desmos
server_name: desmosd
client_name: desmoscli
version: 0.3.0
commit: ec77e479eb1bbde3b506de7bd17b520cc9a2143b
build_tags: netgo ledger
go: go version go1.13.5 darwin/amd64
```

### Genesis file hash

You can verify with the sorted genesis file.

```sh
jq -S -c -M '' genesis.json | shasum -a 256
24494bd9d0800332c4ffdee43b9ef5702cd52bc52c907726197a55990ce5600c  -
```

### Seed node

```sh
8307c16191e249d6d3871ce764262d40d9cf249f@34.74.131.47:26656
```

### Persistent Peers

```sh
89f913e84b58da594eb449fca7b0fcb540e52d05@35.240.254.97:26656
5ebcf26295e966c4d705ce5f42e78203c94ad98d@34.76.79.154:26656
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
