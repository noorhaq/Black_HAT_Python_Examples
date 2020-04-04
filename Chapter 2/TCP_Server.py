import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 10000

server =socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))
server.listen(5)

print (" Listening on %s : %d" % (bind_ip,bind_port))

#Client handling thread

def handle_client(client_socket):
    #Client Sending Data
    request = client_socket.recv(4026)

    print ("[*] Received: %s " %request)

    #Send back a packet for acknowledgment 
    client_socket.send(str.encode("ACK!"))

    client_socket.close()

while True:
    client, addr =server.accept()

    #print (" Accepted Connection from %s:%d" (addr[0],addr[1]))

    #spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
    exit()