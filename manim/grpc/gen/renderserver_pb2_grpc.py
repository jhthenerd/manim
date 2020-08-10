# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import renderserver_pb2 as renderserver__pb2


class RenderServerStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AnimationStatus = channel.unary_unary(
                '/renderserver.RenderServer/AnimationStatus',
                request_serializer=renderserver__pb2.AnimationStatusRequest.SerializeToString,
                response_deserializer=renderserver__pb2.AnimationStatusResponse.FromString,
                )
        self.ManimStatus = channel.unary_unary(
                '/renderserver.RenderServer/ManimStatus',
                request_serializer=renderserver__pb2.ManimStatusRequest.SerializeToString,
                response_deserializer=renderserver__pb2.ManimStatusResponse.FromString,
                )


class RenderServerServicer(object):
    """Missing associated documentation comment in .proto file"""

    def AnimationStatus(self, request, context):
        """Used to signal that a new animation is ready to be animated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ManimStatus(self, request, context):
        """Used to signal when manim starts and stops.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RenderServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AnimationStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.AnimationStatus,
                    request_deserializer=renderserver__pb2.AnimationStatusRequest.FromString,
                    response_serializer=renderserver__pb2.AnimationStatusResponse.SerializeToString,
            ),
            'ManimStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.ManimStatus,
                    request_deserializer=renderserver__pb2.ManimStatusRequest.FromString,
                    response_serializer=renderserver__pb2.ManimStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'renderserver.RenderServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RenderServer(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def AnimationStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/renderserver.RenderServer/AnimationStatus',
            renderserver__pb2.AnimationStatusRequest.SerializeToString,
            renderserver__pb2.AnimationStatusResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ManimStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/renderserver.RenderServer/ManimStatus',
            renderserver__pb2.ManimStatusRequest.SerializeToString,
            renderserver__pb2.ManimStatusResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
