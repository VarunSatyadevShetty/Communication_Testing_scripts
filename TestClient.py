"""Varun communication Cliebnt-Side test script"""
import grpc
import Message_pb2
import Message_pb2_grpc


#format: f"{ipaddress}:" f"{port number}" *note the prt number must be the same on both client and server side
#here we will add the ip adress of the server device
server_ip = f"{'0.0.0.0'}:" f"{'50051'}"

def Send_client_request():
    with grpc.insecure_channel(server_ip, options=(('grpc.enable_http_proxy',0), )) as channel:
        try:
            stub = Message_pb2_grpc.CommunicationServiceStub(channel)
            response = stub.Input(Message_pb2.Request(sendcommandflag= "Send Data = True"))
            print("Client received data: ", response.data_array)
        except grpc.RpcError as e:
            print("Error",e)

if __name__ == '__main__':
    Send_client_request()