#encoding: utf-8
import socket, select, string, sys
 

#main function
if __name__ == "__main__":
     
    if(len(sys.argv) < 3) :
        print 'Usage : python Client.py serverip port'
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host.'
    print s.recv(1024)
    s.close()
     