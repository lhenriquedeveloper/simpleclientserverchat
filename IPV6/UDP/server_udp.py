import socket

udp_ip = ""
udp_port = int(input("Digite a porta do server: "))
fd = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
fd.bind((udp_ip, udp_port))

while True:
    r = fd.recvfrom(1024)
    print("client : %s", (r[0]))
    reply = input("server : ")
    client_address = r[1]
    fd.sendto(reply.encode(), client_address)
