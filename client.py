import socket
import event

PORT_NUMBER = 54321
SERVER_IP = "127.0.0.1"

try:
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Client socket successfully created!")
except:
    print("Socket creation failed")

clientsocket.connect((SERVER_IP, PORT_NUMBER))

status = "CONNECTED"

while status != "GAME_OVER":
    status, message = event.unpack(str(clientsocket.recv(1024).decode()))

    if status == "GAME_STARTED":
        event.game_starting(message)

    elif status == "CHOOSE_NUMBER":
        event.select_number(clientsocket)

    elif status == "GAME_OVER":
        print("Game over. Result: " + message)

    else:
        print(status)






