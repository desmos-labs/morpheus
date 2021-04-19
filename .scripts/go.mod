module .scripts

go 1.15

require (
	github.com/cosmos/cosmos-sdk v0.42.4
	github.com/desmos-labs/desmos v0.15.5-0.20210412060753-2462bd78379e
	github.com/gogo/protobuf v1.3.3
	github.com/rs/zerolog v1.20.0
	github.com/tendermint/tendermint v0.34.9
)

replace google.golang.org/grpc => google.golang.org/grpc v1.33.2

replace github.com/gogo/protobuf => github.com/regen-network/protobuf v1.3.3-alpha.regen.1
