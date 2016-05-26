# BENCHMARK GRPC

The purpose of this project is to benchmark grpc serializer/deserializer in python and java.
And also the end-to-end rpc calls between Java Client - Java Server against Java Client - Python Server.
The Java implementation in another repo, [here](https://github.com/thuy616/grpc-benchmark-test) .

In this repo:
 - Python server implementation
 - The service is define in protos/movieservice.proto

## Setup
Create a new virtual environment. Activate this virtuaenv then do
 ```
 pip install grpcio
 ```
 ```
 pip install protobuf
 ```

The generated client and server python stubs for the movieservice.proto is included, you don't need to do code generation.
If you modify this proto file, you need to install protoc with a special grpc python plugin.
Follow these [instructions](https://github.com/grpc/grpc/blob/release-0_14/INSTALL.md)

## Run
 - Run the serialization tests in python/movieservice:
    python serialization_test.py
 - Run the server:
    python movie_service_server.py


