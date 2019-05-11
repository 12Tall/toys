import socket
target_host = "www.baidu.com"
target_port = 80

# create a connection
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect
client.connect((target_host,target_port))

# send data
client.send(b"GET / HTTP/1.1\r\nHost:baidu.com\r\n\r\n")

# receive data
response = client.recv(4096)

print(response)

