# Morpheus testnets
> Official repository containing all the [Desmos](https://github.com/desmos-labs/desmos) testnets' data.

## Latest running testnet

### Chain data
| Data | Value | 
| :--- | :---: |
| Genesis file |  [genesis file](genesis.json) |
| Chain ID | `morpheus-5000` |
| Genesis time | `2020-06-08T11:00:00.000Z` |

### Desmos Version
```sh
$ desmosd version --long
name: Desmos
server_name: desmosd
client_name: desmoscli
version: 0.6.2
commit: b28e87a2488b51c84b3268a5ea4236d97d00e246
build_tags: netgo ledger
go: go version go1.14.4 linux/amd64
```

### Genesis state
The genesis state was exported from `morpheus-4001` at height [`300000`](https://morpheus-4001.desmos.network/blocks/300000).

### Genesis file hash
You can verify with the sorted genesis file.

```sh
jq -S -c -M '' genesis.json | shasum -a 256
8f8c8c82ff773ef543484124b7cf49467a4e88cf03eab095e869f134ad3eac1e  -
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
