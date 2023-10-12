import threading
import socket

host = '127.0.0.1' #localhost
port = 55555 #use a solid common port

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #initialise a socket server

server.bind((host,port)) # connect server to your port and localhost

server.listen()

clients = [] #store id of players that will interact in the chat
nicknames = [] #store names of the members of the chat
data = []  #store the data for the database in the way [message, sender_name, sender_id]

#Function to send a message to all clients in the server
#parameter message: the message to be sent

def broadcast(message):
    for client in clients:
        client.send(message)

#function to handle a specific client at a time
#parameter client: the client to handle by the server
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

            index = clients.index(client)
            interaction = [message,client,index]
            data.append(interaction)
            #print(interaction)
            #print(exportData())

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = nicknames[index]
            broadcast(f'{name} left the chat'.encode(ascii))
            nicknames.remove(name)
            break

#main function to receive messages in the server
def receive():
    while True:
        # in this case the address is constant as it works in one computer but in a different server it might change
        client, address = server.accept()
        print(f'connected with {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')

        nicknames.append(nickname)
        clients.append(client)

        print(f'Just connected: {nickname }')
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('You are connected to the server'.encode('ascii'))

        #Now we implement threads to handle all clients roughly at the same time
        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

 #method to retrieve the data of the chat as a list of [message,name,id]  
def exportData():
    return data

#run the main method
print("server is working")
receive()

