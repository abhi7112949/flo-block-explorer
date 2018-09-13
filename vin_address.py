from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:17313"%("abhijeet", "abhijeetPassword"))
passphrse = rpc_connection.walletpassphrase("My name is Abhijeet" , 60000)

#transaction_id =input("Enter a transaction id: ")

transaction_id = '9af9e9259ee1ff677b155864867c219b4516fe429e935b8739599a2e0ffdf579'
txindex=1
raw_transaction = rpc_connection.getrawtransaction(transaction_id, txindex)

''' To ge the 'Receiving Addresses' for a transaction '''
for tx in raw_transaction['vin']:
    txi = tx['txid']
    vout_number =tx['vout']
    #print(v_out)
    vin_transaction_id = rpc_connection.getrawtransaction(txi, 1)
    a = vin_transaction_id['vout']
    b = a[vout_number]
    address = b['scriptPubKey']['addresses'][0]
    amount = b['value']
    print(f'{address} : {amount}')
