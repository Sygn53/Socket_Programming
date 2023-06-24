import socket
import sys
import hashlib

s = socket.socket()
host = socket.gethostname()
port = 12345
buffer_size = 20 

if len(sys.argv):
  for each in sys.argv[1:]:
    if '=' in each:
      argument = each.split('=')
      if argument[0] == '--port':
        port = int(argument[1])

print ('host : ', host)
print ('port : ', port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))

incoming = 0

s.listen(5)


while True:
  c, addr = s.accept()
  print ('Got connection from', addr, '.')
  while True: 
    data = c.recv(buffer_size)  
    print("Client:", data.decode())
    c.send(data)  # echo
    data2 = c.recv(buffer_size)  
    print("Sha256 Key:", data2)
    c.send(data2)  # echo

    text = input("")
    c.send(text.encode('utf-8'))
    data3 = c.recv(buffer_size)

    result256 = hashlib.sha256(text.encode())
    c.send(result256.digest())
    data4 = c.recv(buffer_size)

    if text==b'bye':
        break

  
  with open('./uploads/file_'+str(incoming),'wb') as f:
    while True:
      print ('Receiving data ...')
      data =  c.recv(1024)
      if not data:
        break
      f.write(data)
  f.close()
  print('Done file transfer job.')
  c.close()
  print ('Connection ended.')
  incoming += 1

s.close()
