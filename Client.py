import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = 'localhost'    # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

# convert len of msg into two-byte array
# I am assuming the max size of msg is 65536
buf = bytearray([len(msg) & 255, len(msg) >> 8])
sock.sendall(buf)
sock.sendall(msg)

with open('received_file', 'wb') as f:
    print ('file opened')
    while True:
                # convert len of msg into two-byte array
        # I am assuming the max size of msg is 65536
        buf = bytearray([len(msg) & 255, len(msg) >> 8])
        s.sendall(buf)
        s.sendall(msg)
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')

