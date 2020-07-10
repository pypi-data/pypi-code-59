# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import device_pb2 as device__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DeviceCategoryServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListDeviceCategoryKinds = channel.unary_unary(
        '/apiserver.v2.DeviceCategoryService/ListDeviceCategoryKinds',
        request_serializer=device__pb2.ListDeviceCategoryKindsReq.SerializeToString,
        response_deserializer=device__pb2.ListDeviceCategoryKindsRes.FromString,
        )
    self.ListDeviceCategories = channel.unary_unary(
        '/apiserver.v2.DeviceCategoryService/ListDeviceCategories',
        request_serializer=device__pb2.ListDeviceCategoriesReq.SerializeToString,
        response_deserializer=device__pb2.ListDeviceCategoriesRes.FromString,
        )
    self.GetDeviceCategory = channel.unary_unary(
        '/apiserver.v2.DeviceCategoryService/GetDeviceCategory',
        request_serializer=device__pb2.GetDeviceCategoryReq.SerializeToString,
        response_deserializer=device__pb2.DeviceCategory.FromString,
        )
    self.CreateDeviceCategory = channel.unary_unary(
        '/apiserver.v2.DeviceCategoryService/CreateDeviceCategory',
        request_serializer=device__pb2.CreateDeviceCategoryReq.SerializeToString,
        response_deserializer=device__pb2.DeviceCategory.FromString,
        )
    self.UpdateDeviceCategory = channel.unary_unary(
        '/apiserver.v2.DeviceCategoryService/UpdateDeviceCategory',
        request_serializer=device__pb2.UpdateDeviceCategoryReq.SerializeToString,
        response_deserializer=device__pb2.DeviceCategory.FromString,
        )
    self.RemoveDeviceCategory = channel.unary_unary(
        '/apiserver.v2.DeviceCategoryService/RemoveDeviceCategory',
        request_serializer=device__pb2.RemoveDeviceCategoryReq.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class DeviceCategoryServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ListDeviceCategoryKinds(self, request, context):
    """List device kinds
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListDeviceCategories(self, request, context):
    """List device categories with given kind
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDeviceCategory(self, request, context):
    """Get device category detail
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateDeviceCategory(self, request, context):
    """Create new device category
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateDeviceCategory(self, request, context):
    """Update device category detail
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveDeviceCategory(self, request, context):
    """Remove device category
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DeviceCategoryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListDeviceCategoryKinds': grpc.unary_unary_rpc_method_handler(
          servicer.ListDeviceCategoryKinds,
          request_deserializer=device__pb2.ListDeviceCategoryKindsReq.FromString,
          response_serializer=device__pb2.ListDeviceCategoryKindsRes.SerializeToString,
      ),
      'ListDeviceCategories': grpc.unary_unary_rpc_method_handler(
          servicer.ListDeviceCategories,
          request_deserializer=device__pb2.ListDeviceCategoriesReq.FromString,
          response_serializer=device__pb2.ListDeviceCategoriesRes.SerializeToString,
      ),
      'GetDeviceCategory': grpc.unary_unary_rpc_method_handler(
          servicer.GetDeviceCategory,
          request_deserializer=device__pb2.GetDeviceCategoryReq.FromString,
          response_serializer=device__pb2.DeviceCategory.SerializeToString,
      ),
      'CreateDeviceCategory': grpc.unary_unary_rpc_method_handler(
          servicer.CreateDeviceCategory,
          request_deserializer=device__pb2.CreateDeviceCategoryReq.FromString,
          response_serializer=device__pb2.DeviceCategory.SerializeToString,
      ),
      'UpdateDeviceCategory': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateDeviceCategory,
          request_deserializer=device__pb2.UpdateDeviceCategoryReq.FromString,
          response_serializer=device__pb2.DeviceCategory.SerializeToString,
      ),
      'RemoveDeviceCategory': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveDeviceCategory,
          request_deserializer=device__pb2.RemoveDeviceCategoryReq.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'apiserver.v2.DeviceCategoryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
