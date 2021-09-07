# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import helloworld_pb2 as helloworld__pb2


class GreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/helloworld.Greeter/SayHello',
                request_serializer=helloworld__pb2.HelloRequest.SerializeToString,
                response_deserializer=helloworld__pb2.HelloReply.FromString,
                )
        self.ListaMedicamento = channel.unary_unary(
                '/helloworld.Greeter/ListaMedicamento',
                request_serializer=helloworld__pb2.Medicamento.SerializeToString,
                response_deserializer=helloworld__pb2.DatosList.FromString,
                )
        self.AltaMedicamento = channel.unary_unary(
                '/helloworld.Greeter/AltaMedicamento',
                request_serializer=helloworld__pb2.Medicamento.SerializeToString,
                response_deserializer=helloworld__pb2.HelloReply.FromString,
                )
        self.AltaTipo = channel.unary_unary(
                '/helloworld.Greeter/AltaTipo',
                request_serializer=helloworld__pb2.Tipo.SerializeToString,
                response_deserializer=helloworld__pb2.HelloReply.FromString,
                )
        self.EliminarTipo = channel.unary_unary(
                '/helloworld.Greeter/EliminarTipo',
                request_serializer=helloworld__pb2.Tipo.SerializeToString,
                response_deserializer=helloworld__pb2.HelloReply.FromString,
                )
        self.ListaTipo = channel.unary_unary(
                '/helloworld.Greeter/ListaTipo',
                request_serializer=helloworld__pb2.Tipo.SerializeToString,
                response_deserializer=helloworld__pb2.TipoList.FromString,
                )
        self.BuscarMedicamentoId = channel.unary_unary(
                '/helloworld.Greeter/BuscarMedicamentoId',
                request_serializer=helloworld__pb2.Tipo.SerializeToString,
                response_deserializer=helloworld__pb2.DatosList.FromString,
                )
        self.BuscarMedicamentoNombre = channel.unary_unary(
                '/helloworld.Greeter/BuscarMedicamentoNombre',
                request_serializer=helloworld__pb2.Medicamento.SerializeToString,
                response_deserializer=helloworld__pb2.DatosList.FromString,
                )
        self.ListaProducto = channel.unary_unary(
                '/helloworld.Greeter/ListaProducto',
                request_serializer=helloworld__pb2.Producto.SerializeToString,
                response_deserializer=helloworld__pb2.ProductoList.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.
    """

    def SayHello(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListaMedicamento(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AltaMedicamento(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AltaTipo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EliminarTipo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListaTipo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BuscarMedicamentoId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BuscarMedicamentoNombre(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListaProducto(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=helloworld__pb2.HelloRequest.FromString,
                    response_serializer=helloworld__pb2.HelloReply.SerializeToString,
            ),
            'ListaMedicamento': grpc.unary_unary_rpc_method_handler(
                    servicer.ListaMedicamento,
                    request_deserializer=helloworld__pb2.Medicamento.FromString,
                    response_serializer=helloworld__pb2.DatosList.SerializeToString,
            ),
            'AltaMedicamento': grpc.unary_unary_rpc_method_handler(
                    servicer.AltaMedicamento,
                    request_deserializer=helloworld__pb2.Medicamento.FromString,
                    response_serializer=helloworld__pb2.HelloReply.SerializeToString,
            ),
            'AltaTipo': grpc.unary_unary_rpc_method_handler(
                    servicer.AltaTipo,
                    request_deserializer=helloworld__pb2.Tipo.FromString,
                    response_serializer=helloworld__pb2.HelloReply.SerializeToString,
            ),
            'EliminarTipo': grpc.unary_unary_rpc_method_handler(
                    servicer.EliminarTipo,
                    request_deserializer=helloworld__pb2.Tipo.FromString,
                    response_serializer=helloworld__pb2.HelloReply.SerializeToString,
            ),
            'ListaTipo': grpc.unary_unary_rpc_method_handler(
                    servicer.ListaTipo,
                    request_deserializer=helloworld__pb2.Tipo.FromString,
                    response_serializer=helloworld__pb2.TipoList.SerializeToString,
            ),
            'BuscarMedicamentoId': grpc.unary_unary_rpc_method_handler(
                    servicer.BuscarMedicamentoId,
                    request_deserializer=helloworld__pb2.Tipo.FromString,
                    response_serializer=helloworld__pb2.DatosList.SerializeToString,
            ),
            'BuscarMedicamentoNombre': grpc.unary_unary_rpc_method_handler(
                    servicer.BuscarMedicamentoNombre,
                    request_deserializer=helloworld__pb2.Medicamento.FromString,
                    response_serializer=helloworld__pb2.DatosList.SerializeToString,
            ),
            'ListaProducto': grpc.unary_unary_rpc_method_handler(
                    servicer.ListaProducto,
                    request_deserializer=helloworld__pb2.Producto.FromString,
                    response_serializer=helloworld__pb2.ProductoList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/SayHello',
            helloworld__pb2.HelloRequest.SerializeToString,
            helloworld__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListaMedicamento(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/ListaMedicamento',
            helloworld__pb2.Medicamento.SerializeToString,
            helloworld__pb2.DatosList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AltaMedicamento(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/AltaMedicamento',
            helloworld__pb2.Medicamento.SerializeToString,
            helloworld__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AltaTipo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/AltaTipo',
            helloworld__pb2.Tipo.SerializeToString,
            helloworld__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EliminarTipo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/EliminarTipo',
            helloworld__pb2.Tipo.SerializeToString,
            helloworld__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListaTipo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/ListaTipo',
            helloworld__pb2.Tipo.SerializeToString,
            helloworld__pb2.TipoList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BuscarMedicamentoId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/BuscarMedicamentoId',
            helloworld__pb2.Tipo.SerializeToString,
            helloworld__pb2.DatosList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BuscarMedicamentoNombre(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/BuscarMedicamentoNombre',
            helloworld__pb2.Medicamento.SerializeToString,
            helloworld__pb2.DatosList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListaProducto(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/ListaProducto',
            helloworld__pb2.Producto.SerializeToString,
            helloworld__pb2.ProductoList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
