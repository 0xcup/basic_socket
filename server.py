import socket

# create the server

print('starting socket server...')
socket_server = socket.socket()

host = socket.gethostbyname(socket.gethostname())
port =8081

socket_server.bind((host,port))


# listen for clients
socket_server.listen(1)
print('listening for clients...')

client, client_address = socket_server.accept()

if client:
	print(f'{client_address} connected to the server')

# send commands in an infinite loop
while True:
	command = input('> ')
	command = command.encode('utf-8')
	client.send(command)

	output = client.recv(1024)
	output =output.decode('utf-8')
	print(output)

