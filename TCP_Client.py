import socket

target_host = "www.google.com"   #Website you want to connect with
target_port = 80                #Target site port which is open for data transfer
#creating a socket object for data transfer
client =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# The AF_INET parameter is saying we are going to use IPv4 protocol address not IPv6 and SOCK_STREAM is showing we are going to use TCP client not UDP.
# Main difference between UDP and TCP client is TCP receives acknowlegment whether data is sent or received like it rechecks the data for errors while UDP don't. UDP just throws the data at you whether you want it not.

client.connect((target_host,target_port))
#sending data
client.send('GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')

#The GET method means retrieve whatever information (in the form of an entity) is identified by the Request-URI. If the Request-URI refers to a data-producing process, it is the produced data which shall be returned as the entity in the response and not the source text of the process, unless that text happens to be the output of the process.
#Now these are the basic minimum for HTTP request
#if the request is: "GET / HTTP/1.0\r\n\r\n" then the response contains header as well as body, and the connection closes after the response.
#if the request is:"GET / HTTP/1.1\r\nHost: host:port\r\nConnection: close\r\n\r\n" then the response contains header as well as body, and the connection closes after the response.
#if the request is:"GET / HTTP/1.1\r\nHost: host:port\r\n\r\n" then the response contains header as well as body, and the connection will not close even after the response.
#if your request is: "GET /\r\n\r\n" then the response contains no header and only body, and the connection closes after the response.
#if your request is: "HEAD / HTTP/1.0\r\n\r\n" then the response contains only header and no body, and the connection closes after the response.
#if the request is: "HEAD / HTTP/1.1\r\nHost: host:port\r\nConnection: close\r\n\r\n" then the response contains only header and no body, and the connection closes after the response.
#if the request is: "HEAD / HTTP/1.1\r\nHost: host:port\r\n\r\n" then the response contains only header and no body, and the connection will not close after the response.

#---------------receive some data
response = client.recv(4096)
print (response)