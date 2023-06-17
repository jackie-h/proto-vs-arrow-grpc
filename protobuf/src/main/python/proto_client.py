

from __future__ import print_function

import logging

import grpc
import orders_pb2
import orders_pb2_grpc
import time


def get_orders(stub:orders_pb2_grpc.OrdersStub):
    request = orders_pb2.OrderRequest()
    for i in range(0, 20):
        start = time.time()
        response = stub.GetOrders(request)
        end = time.time()
        print(end - start)

    print(len(response.orders))
    #for order in response.orders:
    #    print(order)
    request = orders_pb2.OrderRequest()
    for i in range(0, 20):
        start = time.time()
        orders = stub.GetOrdersStream(request)
        i = 0
        for o in orders:
            i = i + 1
        end = time.time()
        print(end - start)

    print(i)


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = orders_pb2_grpc.OrdersStub(channel)
        print("-------------- GetOrders --------------")
        get_orders(stub)



if __name__ == '__main__':
    logging.basicConfig()
    run()