from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:17313"%("abhijeet", "abhijeetPassword"))
passphrse = rpc_connection.walletpassphrase("My name is Abhijeet" , 60000)

transaction_id =input("Enter a transaction id: ")
#Coinbase- f86339ad64dad07e2a9fef812a82a2aac415754cebf27fec19139e4acaaf9934
# 9af9e9259ee1ff677b155864867c219b4516fe429e935b8739599a2e0ffdf579
#transaction_id = '27e5538b67613b8fa09b0c3fa46869297e192d730af4466ced5389c007e04df5'
txindex=1
raw_transaction = rpc_connection.getrawtransaction(transaction_id, txindex)

''' To ge the 'Receiving Addresses' for a transaction '''

print("Following are the Addresses, from where input money for this transaction is taken:  ")
if raw_transaction['vin'][0]['sequence'] == 0:
    print("NOTE- Only Coinbase Transaction. So,no other input transactions.")
else:
    for tx in raw_transaction['vin']:
        vin_txi = tx['txid']
        vout_number =tx['vout']
        #print(v_out)
        vin_transaction_id = rpc_connection.getrawtransaction(vin_txi, 1)
        a = vin_transaction_id['vout']
        b = a[vout_number]
        vin_address = b['scriptPubKey']['addresses'][0]
        vin_amount = b['value']
        print(f'{vin_address} : {vin_amount}')

print("X----------------------X")

''' To ge the 'Sending Addresses' of a transaction '''
txn_vout = raw_transaction['vout']
print("Sending addresses for this transaction: ")
if raw_transaction['vin'][0]['sequence'] == 0:
    addr = txn_vout[1]['scriptPubKey']['addresses']
    amount = txn_vout[1]['value']
    print(f'{addr} : {amount}')
else:
    for item in txn_vout:
        vout_adrress = item['scriptPubKey']['addresses'][0]
        vout_amount = item['value']
        print(f'{vout_adrress} : {vout_amount}')
