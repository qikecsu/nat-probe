#encoding:utf-8
import socket, select
 
 
if __name__ == "__main__":
     
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 5000
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", PORT))
    server_socket.listen(10)
 
 
    print "Chat server started on port " + str(PORT)
 
   
    sockfd, addr = server_socket.accept()
    print "Client (%s, %s) connected" % addr

    
    
    server_socket.close()