import socket


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)


while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    msg = "Hey there!!!"
    msg = f'{len(msg):<{HEADERSIZE}}'  + msg
    ## this was we can be sure that first 10 char will contain len of 
    ## the following message

    clientsocket.send(bytes(msg,"utf-8"))

