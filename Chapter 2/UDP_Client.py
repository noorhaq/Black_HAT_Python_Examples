import socket

target_host = "127.0.0.1"
#Target host IP in this case localhost
target_port = 20001
#any open port in this case 80. Could be any open port
client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# The AF_INET parameter is saying we are going to use IPv4 protocol address not IPv6 and SOCK_STREAM is showing we are going to use TCP client not UDP.
# Main difference between UDP and TCP client is TCP receives acknowlegment whether data is sent or received like it rechecks the data for errors while UDP don't. UDP just throws the data at you whether you want it not.

#client.bind((target_host,target_port))
#Bind() function in socket programming is used to associate the socket with local address i.e. IP Address, port and address family.
#For more info https://www.interviewsansar.com/tcp-udp-bind-function/
message = str.encode("Pleae Connect")
client.sendto(message,(target_host,target_port))
#Sending data
data, addr = client.recvfrom(4096)
#Data received
#Addr data received from ie IP and local address
#receiving response
print (data)
print (addr)