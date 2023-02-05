"""Varun Communication Server-side test script"""
import grpc
import Message_pb2
import Message_pb2_grpc
from concurrent import futures
import random


#format: f"{ipaddress}:" f"{port number}" *note the prt number must be the same on both client and server side
#here we will add the ip adress of the client device
client_ip = f"{'0.0.0.0'}:" f"{'50051'}"

class CommunicationService(Message_pb2_grpc.CommunicationServiceServicer):
    def Input(self, request, context):
        #Printing out the request from the client
        print("Server received request:", request.sendcommandflag)
        
        #Creating a Dummy array, Replace this by your data passing script
        number = random.randint(0,10)
        number_array = list(range(0,number))

        #Sending the response(i.e the data array)
        return Message_pb2.Response(data_array= number_array)
    
def starting_server():
    server_1 = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Message_pb2_grpc.add_CommunicationServiceServicer_to_server(CommunicationService(),server_1)
    server_1.add_insecure_port(client_ip)
    server_1.start()
    server_1.wait_for_termination()


if __name__ == '__main__':
    starting_server()