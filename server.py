#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from sys import argv

from number_reader import Portuguese_number_reader as number_reader

class Reading_server(BaseHTTPRequestHandler):

    def do_GET(self):
        print("Got a GET request with path = {}".format(self.path))
        try:
            number = int(self.path[1:])
            written_number = number_reader.read_number(number)
        except ValueError:
            self.send_response(400)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("Content-type", "MIME type: application/json")
        self.end_headers()
        json_key = number_reader.json_key
        response = {json_key: written_number}
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, Reading_server)
    try:
        print("Reading server: starting server")
        print("Reading server: listening on port {}".format(str(port)))
        print("Reading server: interrupt process to close server")
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
