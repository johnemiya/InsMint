from web3 import Web3
from dotenv import load_dotenv
import os
load_dotenv()

private_key = os.environ.get('account_private_key')
adress = os.environ.get('account_address')

#需替换为项目方正式合约
contract='0x....' 

rpc_url = "https://avalanche.public-rpc.com"
web3 = Web3(Web3.HTTPProvider(rpc_url))

print(web3.is_connected())
print(Web3.from_wei(web3.eth.get_balance(adress),'ether'))
c=0
while True:
    nonce = web3.eth.get_transaction_count(adress)
    tx = {
        'nonce': nonce,
        'chainId': 43114,
        'to': contract,
        'from':adress,
        'data':0x646174613a2c7b2270223a226672632d3230222c226f70223a226d696e74222c227469636b223a2265717173222c22616d74223a2231303030227d, 
        'gasPrice': web3.eth.gas_price, #Web3.to_wei(35, 'gwei')
        'value': Web3.to_wei(0.1, 'ether')
    }
    try:
        gas = web3.eth.estimate_gas(tx)
        tx['gas'] = gas
        print(tx)
        signed_tx = web3.eth.account.sign_transaction(tx,private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(web3.to_hex(tx_hash))
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        if receipt.status == 1:
            c = c+1
            print("%s Mint Success!" %c)
            continue
        else:
            continue
    except Exception as e:
        print(e)
        break
