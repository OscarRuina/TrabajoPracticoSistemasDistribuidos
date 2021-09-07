cd C:\Users\thesi\Desktop\PruebaExample

python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/helloworld.proto