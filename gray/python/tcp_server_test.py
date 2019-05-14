import socket

host_ip = "0.0.0.0"
host_port = 9999

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host_ip,host_port))
client.send(b"12tall")
response = client.recv(1024)
print(response)

