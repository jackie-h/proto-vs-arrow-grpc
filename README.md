This project compares gRPC with protobufs against the Apache Arrow Flight gRPC protocol that internally uses flatbuffers 

To generate the protobufs run:

python -m grpc_tools.protoc -I protobuf/src/main/proto --python_out=protobuf/src/main/python --pyi_out=protobuf/src/main/python --grpc_python_out=protobuf/src/main/python protobuf/src/main/proto/*.proto


Better proto seems to be considerably slower.
https://github.com/danielgtaylor/python-betterproto/issues/153
https://github.com/danielgtaylor/python-betterproto/issues/314

For better proto
https://github.com/danielgtaylor/python-betterproto

Must install the -pre version if want the ServerBase

pip install --pre "betterproto[compiler]"

python -m grpc_tools.protoc -I protobuf/src/main/proto --python_betterproto_out=protobuf/src/main/python protobuf/src/main/proto/*.proto