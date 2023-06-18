

from __future__ import print_function

import asyncio
import logging

from grpclib.client import Channel
import time

from protobuf.src.main.python import OrderRequest, OrdersStub, TablesStub, TableRequest


async def get_orders(stub:OrdersStub):
    request = OrderRequest()
    print("-------------- GetOrders --------------")
    for i in range(0, 5):
        start = time.time()
        response = await stub.get_orders(request)
        end = time.time()
        print(end - start)

    print(len(response.orders))

    request = OrderRequest()
    print("-------------- GetOrdersStream --------------")
    for i in range(0, 5):
        start = time.time()
        i = 0
        async for order in stub.get_orders_stream(request):
            i = i + 1
        end = time.time()
        print(end - start)
    print(i)


async def get_tables(stub:TablesStub):
    request = TableRequest()

    print("-------------- GetRowTable --------------")
    for i in range(0, 1):
        start = time.time()
        response = await stub.get_row_table(request)
        end = time.time()
        print(end - start)
    print(len(response.rows))

    print("-------------- GetColumnTable --------------")
    for i in range(0, 5):
        start = time.time()
        response = await stub.get_column_table(request)
        end = time.time()
        print(end - start)
    print(len(response.cols[0].int_column.values))


async def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    channel = Channel(host="127.0.0.1",port=50052)
    try:
        stub = OrdersStub(channel)
        print("-------------- GetOrders --------------")
        await get_orders(stub)
        stub = TablesStub(channel)
        print("-------------- GetTables --------------")
        await get_tables(stub)
    finally:
        channel.close()


if __name__ == '__main__':
    logging.basicConfig()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
