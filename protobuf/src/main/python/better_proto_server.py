import asyncio
from concurrent import futures
import logging

from grpclib.server import Server
import pandas as pd

from protobuf.src.main.python import Order,OrderResponse,OrdersBase
from protobuf.src.main.python import TablesBase,Row,RowBasedTable,Cell,ColumnBasedTable,Column,IntColumn,StringColumn,FloatColumn


class OrdersService(OrdersBase):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        self.orders = pd.read_csv("../../../../data/orders1000.csv")
        # self.db = route_guide_resources.read_route_guide_database()

    async def get_orders(self, request):
        response = OrderResponse()
        columns = self.orders
        for tup in self.orders.itertuples():
            order = Order()
            for c in columns:
                setattr(order, c, getattr(tup,c))
            response.orders.append(order)
        return response

    async def get_orders_stream(self, request):
        columns = self.orders
        for tup in self.orders.itertuples():
            order = Order()
            for c in columns:
                setattr(order, c, getattr(tup,c))
            yield order


class TablesService(TablesBase):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        self.orders = pd.read_csv("../../../../data/orders1000.csv")
        # self.db = route_guide_resources.read_route_guide_database()

    async def get_row_table(self, request):
        response = RowBasedTable()
        columns = self.orders
        for c in columns:
            response.column_names.append(c)

        for tup in self.orders.itertuples():
            row = Row()
            for c in columns:
                cell = Cell()
                type = self.orders[c].dtypes
                if type == 'float':
                    cell.float_val = getattr(tup,c)
                elif type == 'int':
                    cell.int_val = getattr(tup,c)
                else:
                    cell.string_val = getattr(tup,c)
                row.values.append(cell)
            response.rows.append(row)
        return response

    async def get_column_table(self, request):
        response = ColumnBasedTable()
        columns = self.orders
        for c in columns:
            col = self.orders[c]
            type = col.dtypes
            if type == 'float':
                val = FloatColumn()
                val.values=self.orders[c].values.tolist()
                column = Column()
                column.float_column = val
            elif type == 'int':
                val = IntColumn()
                val.values = self.orders[c].values.tolist()
                column = Column()
                column.int_column = val
            elif type == 'string':
                val = StringColumn()
                val.values = self.orders[c].values.tolist()
                column = Column()
                column.string_column = val
            elif type == 'object':
                val = StringColumn()
                val.values=self.orders[c].values.tolist()
                column = Column()
                column.string_column = val
            else:
                raise NotImplementedError('type not implemented yet =' + str(type))

            response.cols.append(column)
        return response


async def serve():
    server = Server([OrdersService(), TablesService()])
    await server.start("localhost", 50052)
    await server.wait_closed()


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(serve())