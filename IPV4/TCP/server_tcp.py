import socket

tcp_ip = ""
tcp_port = int(input("Digite a porta do server: "))
fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
fd.bind((tcp_ip, tcp_port))

while True:
    r = fd.recvfrom(1024)
    print("client : %s", (r[0]))
    reply = input("server : ")
    client_address = r[1]
    fd.sendto(reply.encode(), client_address)
