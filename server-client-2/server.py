import socket
import time
import datetime

IP_SERVER = "localhost"
PORT = 9999
ADDRESS = (IP_SERVER, PORT)

def recvUser():
	msg = int(connection.recv(1024).decode("utf-8"))

	if msg == 1:
		print(f"USER requested time, Successfully send time for user.......")
		connection.send(f"TIME -> {time.ctime()}".encode("utf-8"))
	elif msg == 2:
		print(f"USER requested date, Successfully send date for user.......")
		connection.send(f"DATE -> {datetime.datetime.now()}".encode("utf-8"))
	else:
		print(f"user requested unknown service......, FAIL!")
		connection.send(f"your request is not included in our service!....".encode("utf-8"))




serverSocket = socket.socket()

serverSocket.bind(ADDRESS)

print(f"SERVER IS STARTED!............")

serverSocket.listen(3)

lstofQuestion = ["What time it is", "What is today's Date"]

while True:
	connection, address = serverSocket.accept()

	print(f"USER Connected --> {address}")

	connection.send(f"Hello Client, Ask the following questions\n{lstofQuestion}".encode("utf-8"))

	recvUser()










