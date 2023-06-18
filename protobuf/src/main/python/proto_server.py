

from concurrent import futures
import logging

import grpc
import orders_pb2
import orders_pb2_grpc
import pandas as pd
import table_pb2
import table_pb2_grpc


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

    def GetOrdersStream(self, request, context):
        columns = self.orders
        for tup in self.orders.itertuples():
            order = orders_pb2.Order()
            for c in columns:
                setattr(order, c, getattr(tup,c))
            yield order


class TablesServicer(table_pb2_grpc.TablesServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        self.orders = pd.read_csv("../../../../data/orders1000.csv")
        # self.db = route_guide_resources.read_route_guide_database()

    def GetRowTable(self, request, context):
        response = table_pb2.RowBasedTable()
        columns = self.orders
        for c in columns:
            response.columnNames.append(c)

        for tup in self.orders.itertuples():
            row = table_pb2.Row()
            for c in columns:
                cell = table_pb2.Cell()
                type = self.orders[c].dtypes
                if type == 'float':
                    cell.floatVal = getattr(tup,c)
                elif type == 'int':
                    cell.intVal = getattr(tup,c)
                else:
                    cell.stringVal = getattr(tup,c)
                row.values.append(cell)
            response.rows.append(row)
        return response

    def GetColumnTable(self, request, context):
        response = table_pb2.ColumnBasedTable()
        columns = self.orders
        for c in columns:
            col = self.orders[c]
            type = col.dtypes
            if type == 'float':
                val = table_pb2.FloatColumn(values=self.orders[c].values)
                column = table_pb2.Column(floatColumn=val)
            elif type == 'int':
                val = table_pb2.IntColumn(values=self.orders[c].values)
                column = table_pb2.Column(intColumn=val)
            elif type == 'string':
                val = table_pb2.StringColumn(values=self.orders[c].values)
                column = table_pb2.Column(stringColumn=val)
            elif type == 'object':
                val = table_pb2.StringColumn(values=self.orders[c].values)
                column = table_pb2.Column(stringColumn=val)
            else:
                raise NotImplementedError('type not implemented yet =' + str(type))

            response.cols.append(column)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orders_pb2_grpc.add_OrdersServicer_to_server(
        OrdersServicer(), server)
    table_pb2_grpc.add_TablesServicer_to_server(
        TablesServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()