import socket

IP_SERVER = "localhost"
PORT = 9999
ADDRESS = (IP_SERVER, PORT)

clientSocket = socket.socket()

clientSocket.connect(ADDRESS)

print(f"Client Connected!")

msg = clientSocket.recv(1024).decode("utf-8")

print(msg)


while True:
	try:
		userInput = int(input("Choose a Question (1/2): "))
		clientSocket.send(str(userInput).encode("utf-8"))
		break
	except:
		print("Invalid Input, Please Input 1 or 2 ")


print(f'server response -> {clientSocket.recv(1024).decode("utf-8")}')




