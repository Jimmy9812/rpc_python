
from concurrent import futures
import grpc
import sys
import os

# Agrega la ruta raíz al sistema de búsqueda
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import hello_pb2
import hello_pb2_grpc


class GreeterService(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f"Hola, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port("[::]:50051")
    print("Servidor escuchando en el puerto 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
