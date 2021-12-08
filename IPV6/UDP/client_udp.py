import socket

fd = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
udp_ip = str(input("Digite o host: "))
udp_port = int(input("Digite a porta do server: "))
while True:
    message = input("Client:")
    fd.sendto(message.encode(), (udp_ip, udp_port))
    reply = fd.recvfrom(1024)
    print("server: %s ", (reply))
