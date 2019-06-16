#!/usr/bin/python2
import socket
recv_ip="127.0.0.1"
recv_port=4444 #0-1024 are free
#creating udp socket
#ip type v4,soceket protocol udp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#fitting ip and port with udp socket
s.bind((recv_ip,recv_port))
#receive data from sender
#length u want to receive at once
buf=3000
data=s.recvfrom(10)
if data[0].decode()=='1':
	while 4 > 2:	
		data=s.recvfrom(150)  #length of data to recieve in one go
		if data[0].decode()=='exit':
			print("exit by other host")
			s.close()
			break
		print("Message from sender ",data[0].decode())
		reply=input("Your reply : ")
		s.sendto(str.encode(reply),data[1])	
		if reply=='exit':
			s.close()
			break
if data[0].decode()=='2':
        fname=s.recvfrom(buf)
        x=input("sender wants to send the file named "+fname[0].decode())
        f=open(x,"wb")
        data=s.recvfrom(buf)
        while data[0] :
	        s.settimeout(2)
	        f.write(data[0])
	        data=s.recvfrom(buf)
        s.close()
