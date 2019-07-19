import socket
from threading import Thread


class ClientThread(Thread):
    def __init__(self, ip, port,conn):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn

    def run(self):
        while True:
            data = self.conn.recv(1024)
            print "Ip: %s connected port: %d" %(ip,port)
            print "Server received: ", data
            conn.send(data)
            break

TCP_IP = '127.0.0.1'
TCP_PORT = 2004
BUFFER_SIZE = 20

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_server.bind((TCP_IP, TCP_PORT))
threads = []

tcp_server.listen(1000) 
while True: 
    print "Multithreaded Python server : Waiting for connections from TCP clients..." 
    (conn, (ip,port)) = tcp_server.accept() 
    newthread = ClientThread(ip,port,conn) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 
