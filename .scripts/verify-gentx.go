package main

import (
	"encoding/json"
	"fmt"
	"github.com/cosmos/cosmos-sdk/client"
	"github.com/cosmos/cosmos-sdk/codec"
	"github.com/cosmos/cosmos-sdk/x/auth/tx"
	desmosapp "github.com/desmos-labs/desmos/app"
	"github.com/gogo/protobuf/proto"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
	"strings"

	tmtypes "github.com/tendermint/tendermint/types"
	"io/fs"
	"os"
	"path"
	"path/filepath"

	cryptotypes "github.com/cosmos/cosmos-sdk/crypto/types"
	txtypes "github.com/cosmos/cosmos-sdk/types/tx"
	authsigning "github.com/cosmos/cosmos-sdk/x/auth/signing"
	authtypes "github.com/cosmos/cosmos-sdk/x/auth/types"
	stakingtypes "github.com/cosmos/cosmos-sdk/x/staking/types"
	tmjson "github.com/tendermint/tendermint/libs/json"

	sdk "github.com/cosmos/cosmos-sdk/types"
)

func main() {
	dirPath := os.Args[1]

	// Configure logger
	log.Logger = log.Output(zerolog.ConsoleWriter{Out: os.Stderr})

	// Configure Cosmos SDK
	cfg := sdk.GetConfig()
	desmosapp.SetupConfig(cfg)
	cfg.Seal()

	cdc, _ := desmosapp.MakeCodecs()
	encodingConfig := desmosapp.MakeTestEncodingConfig()

	// Get genesis
	genesis, err := getGenesis(dirPath)
	if err != nil {
		log.Fatal().Err(err).Msg("Error while reading genesis file")
	}

	err = validateGenesis(genesis, cdc, encodingConfig.TxConfig)
	if err != nil {
		log.Fatal().Err(err).Msgf("Error while validating genesis")
	}

	var genesisState desmosapp.GenesisState
	if err = tmjson.Unmarshal(genesis.AppState, &genesisState); err != nil {
		panic(err)
	}

	// Validate genesis transactions
	genTxs, err := getGenTxsFiles(dirPath)
	if err != nil {
		panic(err)
	}

	for _, genTxPath := range genTxs {
		err = validateGenTx(genTxPath, genesis, genesisState, cdc)
		if err != nil {
			log.Fatal().Err(err).Msgf("Error while validating %s", genTxPath)
		}
	}

	log.Info().Msg("All genesis transactions validates successfully")
}

// getGenesis returns the genesis doc reading it from the "genesis.json" file located inside the provided dir.
func getGenesis(dir string) (*tmtypes.GenesisDoc, error) {
	bz, err := os.ReadFile(path.Join(dir, "genesis.json"))
	if err != nil {
		return nil, err
	}

	var state tmtypes.GenesisDoc
	if err = tmjson.Unmarshal(bz, &state); err != nil {
		return nil, err
	}
	return &state, nil
}

// validateGenesis validates the given genesis and returns any error
func validateGenesis(genesis *tmtypes.GenesisDoc, cdc codec.JSONMarshaler, txConfig client.TxEncodingConfig) error {
	var genState map[string]json.RawMessage
	if err := json.Unmarshal(genesis.AppState, &genState); err != nil {
		return fmt.Errorf("error unmarshalling genesis doc: %s", err.Error())
	}
	return desmosapp.ModuleBasics.ValidateGenesis(cdc, txConfig, genState)
}

// getGenTxsFiles returns the path to all the genesis transactions files located inside the given dir
func getGenTxsFiles(dir string) ([]string, error) {
	var files []string
	err := filepath.Walk(path.Join(dir, "gentxs"), func(path string, info fs.FileInfo, err error) error {
		if !info.IsDir() && strings.HasSuffix(info.Name(), ".json") {
			files = append(files, path)
		}
		return nil
	})
	if err != nil {
		return nil, err
	}
	return files, nil
}

// validateGenTx validates the genesis transaction file located at the given path
func validateGenTx(
	path string, genesis *tmtypes.GenesisDoc, genesisState desmosapp.GenesisState, cdc codec.Marshaler,
) error {
	log.Info().Msgf("Validating %s", path)

	bz, err := os.ReadFile(path)
	if err != nil {
		return err
	}

	var stdTx txtypes.Tx
	if err = cdc.UnmarshalJSON(bz, &stdTx); err != nil {
		return err
	}

	err = stdTx.ValidateBasic()
	if err != nil {
		return err
	}

	if len(stdTx.Body.Messages) != 1 {
		return fmt.Errorf(`Invalid genesis transaction.
The transaction should have exactly 1 message`)
	}

	msgCreateValidator, ok := stdTx.Body.Messages[0].GetCachedValue().(*stakingtypes.MsgCreateValidator)
	if !ok {
		return fmt.Errorf(`Invalid genesis transaction. 
The included message should be of type MsgCreateValidator`)
	}

	for i, sig := range stdTx.AuthInfo.SignerInfos {
		account, err := getGenesisAccount(msgCreateValidator.DelegatorAddress, genesisState, cdc)
		if err != nil {
			return err
		}

		data := authsigning.SignerData{
			ChainID:       genesis.ChainID,
			AccountNumber: account.AccountNumber,
			Sequence:      account.Sequence,
		}

		bodyBytes, err := proto.Marshal(stdTx.Body)
		if err != nil {
			return err
		}

		authInfoBz, err := proto.Marshal(stdTx.AuthInfo)
		if err != nil {
			return err
		}

		sigBz, err := tx.DirectSignBytes(bodyBytes, authInfoBz, data.ChainID, data.AccountNumber)
		if err != nil {
			return err
		}

		pubKey, ok := sig.PublicKey.GetCachedValue().(cryptotypes.PubKey)
		if !ok {
			return fmt.Errorf("invalid pub key")
		}

		valid := pubKey.VerifySignature(sigBz, stdTx.Signatures[i])
		if !valid {
			return fmt.Errorf(`Invalid signature.
Make sure you have not changed anything inside the genesis file (such as the genesis-time, chain-id or the app state.`)
		}
	}

	log.Info().Msgf("%s is valid", path)
	return nil
}

// getGenesisAccount returns the genesis account that has the given address
func getGenesisAccount(
	address string, genesis desmosapp.GenesisState, cdc codec.Marshaler,
) (*authtypes.BaseAccount, error) {
	var authState authtypes.GenesisState
	if err := cdc.UnmarshalJSON(genesis[authtypes.ModuleName], &authState); err != nil {
		return nil, err
	}

	for _, account := range authState.Accounts {
		baseAccount, ok := account.GetCachedValue().(*authtypes.BaseAccount)
		if !ok {
			return nil, fmt.Errorf("account should be of type BaseAccount")
		}

		if baseAccount.Address == address {
			return baseAccount, nil
		}

	}

	return nil, fmt.Errorf(`Account %s not found.
Make sure you have run "desmos add-genesis-account" and committed the updated genesis state as well.`, address)
}
