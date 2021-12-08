import socket

fd = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
tcp_ip = str(input("Digite o host: "))
tcp_port = int(input("Digite a porta do server: "))
while True:
    message = input("Client:")
    fd.sendto(message.encode(), (tcp_ip, tcp_port))
    reply = fd.recvfrom(1024)
    print("Server:%s", (reply))
