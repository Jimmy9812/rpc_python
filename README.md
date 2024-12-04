# RPC in Python
## Description
This project implements a basic Remote Procedure Call (RPC) service using gRPC in Python. The service allows a client to send a "Hello" request to a server and receive a "Hello, World" response.

## Technologies Used
- Python 3.x: Programming language used for the project.
- gRPC: A high-performance RPC framework.
- Protocol Buffers (Protobuf): Used for defining the service and message structures.
## Requirements
- Python 3.x or higher.
- pip for installing dependencies.
- gRPC tools for generating Python code from .proto files.
## Installation
1. Clone the repository
Clone the repository to your local machine:
```bash
git clone https://github.com/Jimmy9812/rpc_python.git
```
2. Navigate to the project directory
Change to the project directory:
```bash
cd rpc_python
```
3. Create a virtual environment (optional, but recommended)
Create a virtual environment for the project:
```bash
python -m venv venv
```
Activate the virtual environment:
On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```
4. Install dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```
5. Generate gRPC code from .proto files
Compile the .proto file to generate the gRPC client and server code:
```bash
python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. hello.proto
```
## Running the Application
1. Run the gRPC server
Start the server by executing:
```bash
python server/server.py
```
You should see the server listening on port 50051.
2. Run the gRPC client
In a new terminal window, start the client:
```bash
python client/client.py
```
The client will send a "Hello" request to the server, and you should see a response like:
```bash
Response from server: Hello, World!
```
