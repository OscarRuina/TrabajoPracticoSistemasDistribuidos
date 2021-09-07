cd C:\Users\thesi\Documents\Bitbucket\DistribuidosGrpc\PruebaExample

python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/helloworld.proto