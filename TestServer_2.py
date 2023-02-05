"""Varun Communication Server-side test script"""
import grpc
import Message_2_pb2
import Message_2_pb2_grpc
from concurrent import futures
import random


#format: f"{ipaddress}:" f"{port number}" *note the prt number must be the same on both client and server side
#here we will add the ip adress of the client device
client_ip = f"{'0.0.0.0'}:" f"{'50051'}"

class CommunicationService(Message_2_pb2_grpc.CommunicationServiceServicer):
    def Input(self, request, context):
        #Printing out the request from the client
        print("Server received data:", request.data_array)

        #Sending the Null response(to close the communication loop)
        return Message_2_pb2.Null()
    
def starting_server():
    server_1 = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Message_2_pb2_grpc.add_CommunicationServiceServicer_to_server(CommunicationService(),server_1)
    server_1.add_insecure_port(client_ip)
    server_1.start()
    server_1.wait_for_termination()


if __name__ == '__main__':
    starting_server()