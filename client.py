#one way communication
'''import socket
#1900-port number start(0-65535)
s = socket.socket()
host = socket.gethostname()
port = 5555

s.connect((host,port))
#s.send(b"hai goodmorning")
print(s.recv(1024))

s.close()'''


#two way communication client
import socket

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 7000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input
#.lower().strip()
    while message != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

client_program()
