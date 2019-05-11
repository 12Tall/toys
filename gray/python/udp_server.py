import socket

svr_host = "127.0.0.1"
svr_port = 8342

svr = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
svr.bind((svr_host,svr_port))
while True:
    data,addr = svr.recvfrom(1024)
    print("Client Address %s:%s"%addr)
    print("> %s "%data)
    svr.sendto(b"OK",addr)