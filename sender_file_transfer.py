#!/usr/bin/pyth2on2
import socket
recv_ip="127.0.0.1"
recv_port=4444 #0-1024 are free
#creating udp socket
#ip type v4,soceket protocol udp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sending data to receiver
choice=input("press 1 for chat :: press 2 for file transfer --> ")
s.sendto(str.encode(choice),(recv_ip,recv_port))
if choice == '1':
	while 4 > 2:
		msg = input("Enter your message: ")
		s.sendto(str.encode(msg),(recv_ip,recv_port))
		if msg=='exit':
			s.close()
			break
		data=s.recvfrom(150)
		if data[0].decode() == 'exit':
			print("exit from other host")
			s.close()
			break
		else:	
                
			print("Reply from reciever : ",data[0].decode())
if choice == '2':
	file=input("enter file name : ")
	s.sendto(str.encode(file),(recv_ip,recv_port))
	buf=3000
	f=open(file,"rb")
	data=f.read(buf)
	while data :
		s.sendto(data,(recv_ip,recv_port))
		data=f.read(buf)
	s.close()

