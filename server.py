#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from sys import argv

class Reading_server(BaseHTTPRequestHandler):

    def do_GET(self):
        request_line = self.requestline
        print("Got a GET request with request line={}".format(request_line))
        self.send_response(200)
        self.end_headers()
        #codes:
            #successful: 200
            #client error: 400

def run(server_class=HTTPServer, handler_class=Reading_server, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        print("Reading server: starting server")
        print("Reading server: listening on port {}".format(str(port)))
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Reading server: closed successfully")

if __name__ == "__main__":
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
