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

Sign the tx
`signed_tx = web3.eth.account.signTransaction(tx, private_key)`


Send the tx
`tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)`





