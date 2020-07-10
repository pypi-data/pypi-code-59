# coding: utf-8

import logging
import os
import sys
import traceback
try:
    from urllib.parse import urlparse
except:
    from urlparse import urlparse
import grpc
from future.utils import raise_
from NASFileGrpcSystem.code_dict import code_dict
from NASFileGrpcSystem.grpc_create_file import _gen_file
from .proto import files_pb2
from .proto.files_pb2_grpc import FileWorkerStub
if sys.version.startswith("2."):
    FileNotFoundError = IOError


def describe_file(remote_full_path, req_url, local_full_path=None,
                  recovery_full_path=None, return_file=True, timeout=3, logger=logging):
    """
    返回文件信息
    :param remote_full_path: 远程文件存储路径及完整文件名称，全地址
    :param recovery_full_path: 容灾目录文件，当非正常错误发生时，读取此文件
    :param req_url: 请求服务的 ip:port
    :param local_full_path: 下载的文件本地存储路径包含文件名，全地址
    :param return_file: 是否需要将文件流返回, 如不返回则需要传入local_full_path，同时返回""
    :param timeout: 超时时间
    :param logger: 日志对象
    :return:
    """
    code, err, ret_file = None, None, " "
    try:
        logger = logger if logger else logging
        if not remote_full_path or not req_url:
            code = 128502
            return code, code_dict.get(str(code)), ""
        if req_url.startswith("http"):
            req_url = urlparse(req_url).netloc
        if recovery_full_path and not os.path.isfile(recovery_full_path):
            code = 128506
            return code, code_dict.get(str(code)), ""
        if not return_file:
            if not local_full_path:
                code = 128502
                return code, code_dict.get(str(code)), ""
            else:
                if os.path.exists(local_full_path):
                    code = 128507
                    return code, code_dict.get(str(code)), ""
                if not str(os.path.split('./demo.py')[-1]).split(".")[1]:
                    code = 128503
                    return code, code_dict.get(str(code)), ""
        with grpc.insecure_channel(req_url) as channel:
            stub = FileWorkerStub(channel)
            try:
                response = stub.FilesDownload(files_pb2.DownloadRequest(
                    locate_file=remote_full_path.encode('utf-8')), timeout=timeout)
            except grpc.RpcError as e:
                status_code = e.code()
                if grpc.StatusCode.DEADLINE_EXCEEDED == status_code:
                    # 请求超时
                    code, err, ret_file = 128512, code_dict.get("128512"), ""
                elif grpc.StatusCode.UNAVAILABLE == status_code:
                    # 服务短时不可用，重试一次
                    try:
                        response = stub.FilesDownload(files_pb2.DownloadRequest(
                            locate_file=remote_full_path.encode('utf-8')), timeout=timeout)
                    except grpc.RpcError as e:
                        logger.error("Grpc 重试依然返回异常，%s, details=%s", status_code, e.details())
                        code = 1
                        err = "请求失败"
                        ret_file = b""
                    else:
                        code = response.code
                        err = response.err
                        ret_file = response.file
                        if code == 0 and local_full_path:
                            if not os.path.exists(local_full_path):
                                try:
                                    with open(local_full_path, "wb") as f:
                                        f.write(ret_file)
                                except IOError:
                                    code = 128513
                                    return code, code_dict.get(str(code)), ""
                            else:
                                code = 128507
                                return code, code_dict.get(str(code)), ""
                elif grpc.StatusCode.INVALIDARGUMENT == status_code:
                    # 参数异常
                    code = 128501
                    return code, code_dict.get(str(code)), ""
                else:
                    logger.error("Grpc 请求异常，%s, details=%s", status_code, e.details())
                    code = 1
                    err = "请求失败"
                    ret_file = b""
            else:
                code = response.code
                err = response.err
                ret_file = response.file
                if code == 0 and local_full_path:
                    if not os.path.exists(local_full_path):
                        try:
                            with open(local_full_path, "wb") as f:
                                f.write(ret_file)
                        except IOError:
                            code = 128513
                            return code, code_dict.get(str(code)), ""
                    else:
                        code = 128507
                        return code, code_dict.get(str(code)), ""
                ret_file = ret_file if return_file else ""
    except Exception as exc:
        logger.error(traceback.format_exc())
        raise_(Exception, exc)
    finally:
        try:
            if (code in [128509, 128512, 1] or not code_dict.get(str(code), None)) and recovery_full_path:
                code, err, ret_file = _recovery_handle(recovery_full_path, local_full_path, return_file, logger)
        except Exception as exc:
            logger.error(traceback.format_exc())
            raise_(Exception, exc)
    return code, err, ret_file


def _recovery_handle(recovery_full_path, local_full_path, return_file, logger):
    try:
        recovery_file = _gen_file(recovery_full_path)
        if local_full_path:
            if not os.path.exists(local_full_path):
                with open(local_full_path, "wb") as f:
                    for fc in recovery_file:
                        f.write(fc)
            else:
                return 128507, code_dict.get("128507"), ""
        code = 0
        err = '操作成功'
        if return_file:
            with open(recovery_full_path, "rb") as f:
                ret_file = f.read()
        else:
            ret_file = ""
        return code, err, ret_file
    except FileNotFoundError:
        return 128505, code_dict.get("128505"), ""
    except IOError:
        return 128513, code_dict.get("128513"), ""
    except Exception as exc:
        logger.error(traceback.format_exc())
        raise_(Exception, exc)