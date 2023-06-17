# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide server."""

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