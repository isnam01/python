import os
import socket
recv_ip="127.0.0.1"
recv_port=4444 # 0-1024  free udp port can be checked using netstat -nulp

#creating udp socket
#             ip type ipv4    ,udp                              
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 2>1 :
 a=input("Enter message")
 if len(a)>150:
  print("error")
 else:
  if a=="exit":   
   s.close()
  else:
   a=str.encode(a)
   s.sendto(a,(recv_ip,recv_port))
   data=s.recvfrom(100)
   print("receiver:",str(data[0]))
