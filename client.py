import socket

server_IP = "127.0.0.1"
server_PORT = 12543
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((server_IP, server_PORT))
    print("[+] You have successfully connected! ! !\n")

    while True:
        server_message = client.recv(1048)
        print(f"[-] Server message : {server_message.decode()}")
        client_message = input("[+] Enter your message : ")
        client.send(client_message.encode())

except:
    print("[!] Please check your connection or Check to make sure the port is open!")