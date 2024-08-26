import socket
s = socket.socket()
print('Scoket successfully created')
port = 5555
s.bind(('', port))
print(f'socket binded to {port}')
s.listen(5)
print('socket is listening')
while True:
    c, addr = s.accept()
    print(f'Got connection from{addr}')
    message = ('Thank U for connecting...')
    c.send(message.encode())
    c.close()
    