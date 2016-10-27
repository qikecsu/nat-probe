#encoding: utf-8
import socket, select, string, sys
 
 
if __name__ == "__main__":
     
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 30000
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)
    print "Chat server started on port " + str(PORT)
 
    while 1:
        sockft, addr1 = server_socket.accept()
        print "Client (%s, %s) connected" % addr1
        sockft.send("you connect first!")

        sockscd, addr2 = server_socket.accept()
        print "Client (%s, %s) connected" % addr2
        sockscd.send("you connect second!")

        messages = str(addr1[0])+'|'+str(addr1[1])+'|'+'s'
        messagec = str(addr2[0])+'|'+str(addr2[1])+'|'+'c'
        sockft.send(messagec)
        print "send messagec  " + messagec
        sockscd.send(messages)
        print "send messages  " + messages

        break

    server_socket.close()