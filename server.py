#one way communication
'''import socket
s = socket.socket()

host = socket.gethostname()
port = 5555

s.bind((host,port))

print("Waiting for connection.......")
s.listen(5)

while True:
    conn,addr = s.accept()
    print("Got Connection from ",addr)
    #print(conn.recv(1024))
    conn.send(b"good morning iam server")
    conn.close()'''
              


#two way communication server
import socket
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 7000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode() 
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


server_program()


    
