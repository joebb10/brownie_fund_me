from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "ChainX",
]  # "uranus" = UranX testnet. uranus chainid = 14
# para apagar a network é so ir em-->[build - deployments e deletar as chains id que desejar(lembre de apagar ela no map.son file tbm )]
# Se tiver alguma duvida sobre, volte para o tempo 5:42(horas) e reveja o processo

DECIMALS = 8
STARTING_PRICE = 200000000000

# "brownie networks list" on terminal to find the network you need
# "brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=1337" adding a network on brownie
# what to change?
# -- You can change everything after "add" to connect to the blockchain you want
# "brownie networks add UranX URX-Mainnet host=http://127.0.0.1:8545 chainid=13" creating your own mainnet(network), blockchain and chain id using brownie
# Aprenda a fazer a sua propria network e uso o codigo na linha de cima para adicionar ela ao brownie; aprenda a fazer a sua chainId também


def get_account():

    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is{network.show_active()}")
    print(f"Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS,
            Web3.toWei(STARTING_PRICE, "ether"),
            {
                "from": get_account()
            },  # the "toWei" gonna add 18 decimals to the number inside the ()
        )
        print("Mocks Deployed!")
