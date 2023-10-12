import socket
import threading

nickname = input("choose your chat nickname: ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1' #localhost
port = 55555 #use a solid common port

client.connect((host,port))

#main method of the client
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error happened... ")
            client.close()
            break

#function for the client to write a message
def write():
    while True:
        message = f'{nickname}:  {input("")}'
        client.send(message.encode('ascii'))

#we work with threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()