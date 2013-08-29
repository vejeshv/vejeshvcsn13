import socket            
import os
s=socket.socket()         
host=socket.gethostname()
port=10000                
stat1='KO'
stat2='KO'
stat3='KO'
s.connect((host, port))

#Giving ls command to server and receiving the output

s.send('ls')
print s.recv(2048)

#Transmitting file to server

fl_name='file.txt'
fl_len=os.path.getsize('file.txt')
f=open(fl_name,'r')
data=f.read()
f.close()
while not stat1=='OK':
  s.send(fl_name)
  stat1=s.recv(4)
while not stat2=='OK':
  s.send(str(fl_len))
  stat2=s.recv(4)
while not stat3=='OK':
  s.sendall(data)
  stat3=s.recv(4)

#Receiving file from server 

fl_name=s.recv(1024)
s.send('OK')
print "File name received :",fl_name,"\n"
fl_size=s.recv(1024)
size_int=int(fl_size)
s.send('OK')
print "\n File size :",fl_size,"\n"
data=s.recv(size_int)
s.send('OK')
f=open('/home/vejesh/Received/'+fl_name,'w')
f.write(data)
f.close()
f=open('/home/vejesh/Received/'+fl_name,'r')
d=f.read()
f.close()
print "Content of file created :\n"
print d
s.close
