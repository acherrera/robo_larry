import socket
import socketserver
import pickle
import numpy as np

# Boy do I love classes - just hacking this together

class MyTCPServer(socketserver.TCPServer):
    """
        Have to do this in order to resuse the existing port. Just overriding the default class
    """

    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):

        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.data = pickle.loads(self.data)
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        print(type(self.data))
        # Just acknowledge something
        self.request.sendall(b'Got it')

        # If received len == 1, add to key_input_list
        if len(self.data) == 1:
            self.key_input_list.append(self.data)
            print(self.key_input_list)

            if len(self.key_input_list) > 10:
                self.key_input_list = list()
                print("Resetting input key list")

        # If received len > 10, do some math to get which key to use for input
        # Append [input_img, controls] to master array
        # reset key_input_list
        # If master array % 500 == 0 save master array to file again



if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = MyTCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
