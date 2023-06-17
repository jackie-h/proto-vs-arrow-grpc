

To generate the protobufs run:

python -m grpc_tools.protoc -I protobuf/ --python_out=protobuf/src/main/python --pyi_out=protobuf/src/main/python --grpc_python_out=protobuf/src/main/python protobuf/orders.proto