import socket              
import subprocess
import os
s = socket.socket()         
host = socket.gethostname()
stat1='KO'
stat2='KO'
stat3='KO'
print "\t <<Server Started>> \n"
print "\n Hostname :",host,"\n"
port = 10000               
s.bind((host, port))       
s.listen(3)                 
while True:
   c, addrs = s.accept()    
   print "\nIncoming connection from :", addrs,"\n"

#Receiving command from client

   a=c.recv(1024)
   print "Command received :",a,"\n"

#Executing received command from client

   print "\nExecuting received command... \n"
   d=subprocess.Popen(a,stdout=subprocess.PIPE)
   d_out, d_err = d.communicate()

#Transmitting the output of command execution back to client

   c.send(d_out)

#Receiving file from client

   print "\n"
   fl_name=c.recv(1024)
   c.send('OK')
   print "File name received :",fl_name,"\n"
   fl_size=c.recv(1024)
   size_int=int(fl_size)
   c.send('OK')
   print "\n File size :",fl_size,"\n"
   data=c.recv(size_int)
   c.send('OK')
   f=open('/home/vejesh/Received/'+fl_name,'w')
   f.write(data)
   f.close()
   f=open('/home/vejesh/Received/'+fl_name,'r')
   d=f.read()
   f.close()
   print "Content of file created :\n"
   print d
   
#Transmitting file to client

   fl_name='serverfile.txt'
   fl_len=os.path.getsize('serverfile.txt')
   f=open(fl_name,'r')
   data=f.read()
   f.close()
   while not stat1=='OK':
     c.send(fl_name)
     stat1=c.recv(4)
   while not stat2=='OK':
     c.send(str(fl_len))
     stat2=c.recv(4)
   while not stat3=='OK':
     c.sendall(data)
     stat3=c.recv(4)

   c.close()
