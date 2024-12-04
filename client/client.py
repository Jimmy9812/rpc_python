
import grpc
import sys
import os

# Agrega la ruta raíz al sistema de búsqueda
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import hello_pb2
import hello_pb2_grpc

def run():
    # Crear el canal gRPC
    with grpc.insecure_channel("localhost:50051") as channel:
        # Crear un stub para interactuar con el servidor
        stub = hello_pb2_grpc.GreeterStub(channel)
        # Llamar al método remoto y pasar el mensaje
        response = stub.SayHello(hello_pb2.HelloRequest(name="Mundo"))
        # Imprimir la respuesta
        print(f"Respuesta del servidor: {response.message}")

if __name__ == "__main__":
    run()

