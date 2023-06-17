

from concurrent import futures
import logging

import grpc
import orders_pb2
import orders_pb2_grpc


class OrdersServicer(orders_pb2_grpc.OrdersServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        self.data = []
        # self.db = route_guide_resources.read_route_guide_database()

    def GetOrders(self, request, context):
        response = orders_pb2.OrderResponse()
        for i in range(0,100):
            response.orders.append(orders_pb2.Order(col1=100000, col2="hello"))

        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orders_pb2_grpc.add_OrdersServicer_to_server(
        OrdersServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()