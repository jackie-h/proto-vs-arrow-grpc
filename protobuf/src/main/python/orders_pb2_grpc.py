# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import orders_pb2 as orders__pb2


class OrdersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOrders = channel.unary_unary(
                '/Orders/GetOrders',
                request_serializer=orders__pb2.OrderRequest.SerializeToString,
                response_deserializer=orders__pb2.OrderResponse.FromString,
                )
        self.GetOrdersStream = channel.unary_stream(
                '/Orders/GetOrdersStream',
                request_serializer=orders__pb2.OrderRequest.SerializeToString,
                response_deserializer=orders__pb2.Order.FromString,
                )


class OrdersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetOrders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrdersStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrdersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrders,
                    request_deserializer=orders__pb2.OrderRequest.FromString,
                    response_serializer=orders__pb2.OrderResponse.SerializeToString,
            ),
            'GetOrdersStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetOrdersStream,
                    request_deserializer=orders__pb2.OrderRequest.FromString,
                    response_serializer=orders__pb2.Order.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Orders', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Orders(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Orders/GetOrders',
            orders__pb2.OrderRequest.SerializeToString,
            orders__pb2.OrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrdersStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Orders/GetOrdersStream',
            orders__pb2.OrderRequest.SerializeToString,
            orders__pb2.Order.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
