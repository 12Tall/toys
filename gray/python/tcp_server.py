import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

# create server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# bind ip and port
server.bind((bind_ip,bind_port))

# start listening
server.listen(5)

print("[*] Listening on %s:%d"%(bind_ip,bind_port))

# define client request handler
def handle_client(client_socket):
    # receive 1024 bytes data
    request = client_socket.recv(1024)
    print("[*] Received: %s"%request)
    # response
    client_socket.send(b"ACK!")
    client_socket.close()

# loop
while True:
    # accept connectiong from client
    client,addr = server.accept()
    print("[*] Accepted connection from: %s:%d"%(addr[0],addr[1]))
    # init a handler thread
    client_handler = threading.Thread(target=handle_client,args=(client,))
    # start thread
    client_handler.start()
