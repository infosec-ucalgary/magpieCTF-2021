
import sys, socket

def main():

  if (len(sys.argv) <= 3):
    print("Usage: " + sys.argv[0] + " <intercept_port> <challenge_host> <challenge_port>")
    exit(1)

  my_port = int(sys.argv[1])
  challenge_site = sys.argv[2]
  challenge_port = int(sys.argv[3])

  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversocket.bind(('0.0.0.0', my_port))
  serversocket.listen(5)

  while True:
    print("Waiting for connection on port " + str(my_port) + "...")
    (clientsocket, address) = serversocket.accept()
    
    print("Client connected. Waiting to receive data...")
    msg_byte = clientsocket.recv(1024)
    
    print("Connecting to " + challenge_site + " on port " + str(challenge_port) + "..." )
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((challenge_site, challenge_port))
    
    print("Sending request from proxy...")
    s.send(msg_byte)

    print("Waiting to recieve data...")
    data = s.recv(1024)
    print("\n" + data.decode() + "\n")

    print("Closing connection...")
    clientsocket.close()
    s.close()

main()
