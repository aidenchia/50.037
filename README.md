# 50.037
Blockchain Technology Module Exercises

## Question 1
__Connect Web3py to Ganache__

```
ganache_url = "http://127.0.0.1:7545
web3 = Web3(Web3.HTTPProvider(ganache_url))
```

__Make transactions between Ganache accounts__

Create a nonce as it is a required field in transaction to prevent double spending  
`nonce = web3.eth.getTransactionCount(account_1)`

Create the transaction as a dict

```
tx = {
	'nonce': nonce,
	'to': account_2,
	'value': web3.toWei(1, 'ether'),
	'gas': 2000000,
	'gasPrice': web3.toWei('50', 'gwei')
}

```

Sign and send the tx    

```
signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
```

__Get information of latest block__  

`info = web3.eth.getBlock('latest')`

For this latest block, 
* number: 1481
* gasLimit: 6721975
* gasUsed: 21000

__Get and print receipt of conducted tx__
```
print(web3.eth.getTransactionReceipt(tx_hash))
```

## Question 2
__Compile and deploy smart contract__

I was unable to compile with `solc` despite numerous tries. I tried	`sudo npm install -g` and `npm install` and set path but still kept getting permission errors and other errors. In the end, decided to simply compile with Remix and get the abi and bytecode values directly from there.

```
abi = json.loads(open('abi.json', 'r').read())
bytecode = json.loads(open('bytecode.json', 'r').read())['object']
```

Create the smart contract object and deploy it  
```
Fib = web3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = Fib.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
```

__Which Fibonacci function is more efficient in terms of gas cost?__
Instantiate the smart contract at specified address  
`contract = web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)`

















