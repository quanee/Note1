import socket
'''
阻塞IO
非阻塞IO
Mutiplexing I/O 多路复用
信号驱动I/O
Asynchronous I/O
'''

print(socket.socket())

sk = socket.socket()

sk.bind()

sk.listen(3)
# sk.setblocking()
conn, addr = sk.accept()

conn.recv()