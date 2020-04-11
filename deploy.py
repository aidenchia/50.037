from web3 import Web3 
import json

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Compiled by Remix
abi = json.loads(open('abi.json', 'r').read())
bytecode = json.loads(open('bytecode.json', 'r').read())['object']

# Set default account
web3.eth.defaultAccount = web3.eth.accounts[0]

# Create smart contract object
Fib = web3.eth.contract(abi=abi, bytecode=bytecode)

# Deploy smart contract
tx_hash = Fib.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Instantiate the smart contract at specified address
contract = web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Call functions in smart contract
tx_hash = contract.functions.fibonacciB(4).transact()

# Wait for tx to be mined
web3.eth.waitForTransactionReceipt(tx_hash)

# Print receipt
print(web3.eth.getTransactionReceipt(tx_hash)['gasUsed'])














