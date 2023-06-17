

from concurrent import futures
import logging

import grpc
import orders_pb2
import orders_pb2_grpc
import pandas as pd


class OrdersServicer(orders_pb2_grpc.OrdersServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        self.orders = pd.read_csv("../../../../data/orders1000.csv")
        # self.db = route_guide_resources.read_route_guide_database()

    def GetOrders(self, request, context):
        response = orders_pb2.OrderResponse()
        columns = self.orders
        for tup in self.orders.itertuples():
            order = orders_pb2.Order()
            for c in columns:
                setattr(order, c, getattr(tup,c))
            response.orders.append(order)
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