import binascii
import grpc
from DappleySdk.lib.protobuf import rpc_pb2_grpc, rpc_pb2


class RPCClient:
    def __init__(self, host, port):
        self._host = host
        self._port = port

    def shut_down_chanel(self, channel):
        channel.close()

    def get_channel(self):
        channel = grpc.insecure_channel('{}:{}'.format(self._host, self._port))
        return channel

    def get_rpc_client(self, channel):
        stub = rpc_pb2_grpc.RpcServiceStub(channel)
        return stub

    def get_version(self, proto_version):
        channel = grpc.insecure_channel('{}:{}'.format(self._host, self._port))
        stub = rpc_pb2_grpc.RpcServiceStub(channel)
        response = stub.RpcGetVersion(rpc_pb2.GetVersionRequest(proto_version=proto_version))
        message = "{}'protocolVersion':{},'serverVersion':{}{}".format("{", response.proto_version,
                                                                       response.server_version, "}")
        channel.close()
        return message

    def get_balance(self, address):
        channel = grpc.insecure_channel('{}:{}'.format(self._host, self._port))
        stub = rpc_pb2_grpc.RpcServiceStub(channel)
        response = stub.RpcGetBalance(rpc_pb2.GetBalanceRequest(address=address))
        channel.close()
        return response.amount

    def get_block_chain_info(self):
        channel = grpc.insecure_channel('{}:{}'.format(self._host, self._port))
        stub = rpc_pb2_grpc.RpcServiceStub(channel)
        response = stub.RpcGetBlockchainInfo(rpc_pb2.GetBlockchainInfoRequest())
        channel.close()
        return {"tailBlockHash": binascii.hexlify(response.tail_block_hash), "blockHeight": response.block_height,
                "producers": response.producers}

    def get_utxos(self, address):
        channel = grpc.insecure_channel('{}:{}'.format(self._host, self._port))
        stub = rpc_pb2_grpc.RpcServiceStub(channel)
        response = stub.RpcGetUTXO(rpc_pb2.GetUTXORequest(address=address))
        channel.close()
        return response.utxos

    def get_blocks(self, start_block_hashes, max_count):
        channel = grpc.insecure_channel('{}:{}'.format(self._host, self._port))
        stub = rpc_pb2_grpc.RpcServiceStub(channel)
        response = stub.RpcGetBlocks(
            rpc_pb2.GetBlocksRequest(start_block_hashes=start_block_hashes, max_count=max_count))
        channel.close()
        return response.blocks

    def get_block_by_hash(self, byte_hash):
        channel = grpc.insecure_channel('{}:{}'.format(self._host, self._port))
        stub = rpc_pb2_grpc.RpcServiceStub(channel)
        response = stub.RpcGetBlockByHash(rpc_pb2.GetBlockByHashRequest(hash=byte_hash))
        channel.close()
        return response.block

    def get_block_by_height(self, height):
        channel = grpc.insecure_channel('{}:{}'.format(self._host, self._port))
        stub = rpc_pb2_grpc.RpcServiceStub(channel)
        response = stub.RpcGetBlockByHeight(rpc_pb2.GetBlockByHeightRequest(height=height))
        channel.close()
        return response.block

    def send_transaction(self, transaction):
        channel = grpc.insecure_channel('{}:{}'.format(self._host, self._port))
        stub = rpc_pb2_grpc.RpcServiceStub(channel)
        try:
            response = stub.RpcSendTransaction(rpc_pb2.SendTransactionRequest(transaction=transaction))
            channel.close()
            return {"code": 0, "message": response.generated_contract_address}
        except grpc.RpcError as e:
            return {"code": -1, "message": e.details()}

    def estimate_gas(self, transaction):
        channel = grpc.insecure_channel('{}:{}'.format(self._host, self._port))
        stub = rpc_pb2_grpc.RpcServiceStub(channel)
        response = stub.RpcEstimateGas(rpc_pb2.EstimateGasRequest(transaction=transaction))
        channel.close()
        return response.gas_count

    def get_gas_price(self):
        channel = grpc.insecure_channel('{}:{}'.format(self._host, self._port))
        stub = rpc_pb2_grpc.RpcServiceStub(channel)
        response = stub.RpcGasPrice(rpc_pb2.GasPriceRequest())
        channel.close()
        return response.gas_price

    def contract_query(self, contract_address, key, value):
        channel = grpc.insecure_channel('{}:{}'.format(self._host, self._port))
        stub = rpc_pb2_grpc.RpcServiceStub(channel)
        response = stub.RpcContractQuery(
            rpc_pb2.ContractQueryRequest(contract_addr=contract_address, key=key, value=value))
        channel.close()
        return {"key": response.key, "value": response.value}
