import socket
import sys
import time
import pickle
import numpy as np

HOST, PORT = "localhost", 9999

for i in range(10,20):
    data = np.array([j for j in range(0,i)])
    data = pickle.dumps(data)
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(data)

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        time.sleep(2)

        print("Sent:     {}".format(data))
        print("Received: {}".format(received))
