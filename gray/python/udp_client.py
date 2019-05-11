import socket
target_host = "127.0.0.1"
target_port = 80

# init a connection
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# no need connect before send data
# must trans data into byte[]
client.sendto(b"AABBCC",(target_host,target_port))

# receive data
data,addr = client.recvfrom(6)

print(data)

