import socket

bind_ip = "127.0.0.1"
bind_port = 20001

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((bind_ip, bind_port))

print (" Listening on %s : %d" % (bind_ip,bind_port))

while True:
    msg = server.recvfrom(4096)
    clientMsg = "Message from client :{}".format(msg[0])
    clientIP = "CLient IP Address :{}".format(msg[1])

    print (clientMsg)
    print (clientIP)

    server.sendto(str.encode("Succesful connection"), msg[1])
    exit()
    