import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Conexao de {address} foi feita")
	clientsocket.send(bytes(input("diga algo agora!!!!"), "utf-8"))
	clientsocket.close()