import binascii

from DappleySdk.lib.protobuf import transaction_pb2, rpc_pb2
from DappleySdk.model.Transaction import Transaction
from DappleySdk.rpcnet.RPCClient import RPCClient


def test_get_version():
    print ("==============test get version start=========")
    rpc = RPCClient("127.0.0.1", "50050")
    version_info = rpc.get_version("1.0.0")
    print (version_info)
    print ("==============test get version end===========\n")


def test_get_balance():
    print ("==============test get balance start=========")
    rpc = RPCClient("127.0.0.1", "50050")
    balance = rpc.get_balance("dastXXWLe5pxbRYFhcyUq8T3wb5srWkHKa")
    print ("balance:{}".format(balance))
    print ("==============test get balance end===========\n")


def test_get_block_chain_info():
    print ("==============test get block chain info start=========")
    rpc = RPCClient("127.0.0.1", "50050")
    block_chain_info = rpc.get_block_chain_info()
    print ("block_chain_info:{}".format(block_chain_info))
    print ("==============test get block chain info end===========\n")


def test_get_utxos():
    print ("==============test get utxos start=========")
    rpc = RPCClient("127.0.0.1", "50050")
    utxos = rpc.get_utxos("dastXXWLe5pxbRYFhcyUq8T3wb5srWkHKa")
    print ("utxos len:{}".format(len(utxos)))
    print ("==============test get utxos end===========\n")


def test_get_blocks():
    print ("==============test get blocks start=========")
    rpc = RPCClient("127.0.0.1", "50050")
    blocks = rpc.get_blocks("821fe48f468eca9800a4d15ff2091b20cc76732b18e25eef349013509e1d3868", 2)
    print ("blocks :{}".format(blocks))
    print ("==============test get blocks end===========\n")


def test_get_block_by_hash():
    print ("==============test get block by hash start=========")
    rpc = RPCClient("127.0.0.1", "50050")
    block = rpc.get_block_by_hash(binascii.a2b_hex("821fe48f468eca9800a4d15ff2091b20cc76732b18e25eef349013509e1d3868"))
    print ("block :{}".format(block))
    print ("==============test get block by hash end===========\n")


def test_get_block_by_height():
    print("==============test get block by height start=========")
    rpc = RPCClient("127.0.0.1", "50050")
    block = rpc.get_block_by_height(1)
    print ("block :{}".format(block))
    print ("==============test get block by height end===========\n")


def test_get_gas_price():
    print("==============test get gas_price start=========")
    rpc = RPCClient("127.0.0.1", "50050")
    gas_price = rpc.get_gas_price()
    print ("gas_price :{}".format(binascii.hexlify(gas_price)))
    print ("==============test get gas_price end===========\n")


def test_send_transaction():
    print("==============test send_transaction start=========")
    rpc = RPCClient("127.0.0.1", "50050")
    transaction = Transaction()
    transaction.gas_limit = 0
    data = transaction.to_proto()
    send_transaction = rpc.send_transaction(data)
    print ("send_transaction :{}".format(send_transaction))
    print ("==============test send_transaction end===========\n")


def test_all_run():
    test_get_version()
    test_get_balance()
    test_get_block_chain_info()
    test_get_utxos()
    test_get_blocks()
    test_get_block_by_hash()
    test_get_block_by_height()
    test_get_gas_price()
    test_send_transaction()


if __name__ == '__main__':
    print ("start to test rpc client and each api")
    test_all_run()
    print ("test rpc client end")
