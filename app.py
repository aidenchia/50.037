from web3 import Web3 

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = '0xdb7BD110BeDadbb3DF35dd0907C0369E4412DBBD' 
account_2 = '0xe0D49AA4Bab0b0af92F0F16c72BF3d610Ddb1F5f'
private_key = '39f86dabeed31f945362790582d87641ae35b309a44ffbf998161ed083806c4c'

nonce = web3.eth.getTransactionCount(account_1)

tx = {
	'nonce': nonce,
	'to': account_2,
	'value': web3.toWei(1, 'ether'),
	'gas': 2000000,
	'gasPrice': web3.toWei('50', 'gwei')
}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# send transaction to the network
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# print to stdout the hash of the transaction
print(web3.toHex(tx_hash))

# get latest block
info = web3.eth.getBlock('latest')
print('number: {}'.format(info['number']))
print('gasLimit: {}'.format(info['gasLimit']))
print('gasUsed: {}'.format(info['gasUsed']))






















