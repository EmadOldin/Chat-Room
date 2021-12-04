import socket

server_IP = "127.0.0.1"
server_PORT = 12543

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_IP, server_PORT))
server.listen(3)
print("Start server. . .")

server, addr = server.accept()
while True:
    message_server = input("[+] Enter your message : ")
    server.send(message_server.encode())
    messgae_client = server.recv(1048)
    print(f"[-] Client message : {messgae_client.decode()}")
