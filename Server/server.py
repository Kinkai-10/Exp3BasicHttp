from http.server import BaseHTTPRequestHandler, HTTPServer
from time import gmtime, strftime

address = ('localhost', 8080)

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'Hello: BasicHttp!\n')

        date = strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
        print("Date : {}".format(date))
        print("Content-Type : {}\n".format(self.headers["content-type"]))
        print(self.client_address[0])

    def do_POST(self):

        content_length = int(self.headers['content-length'])

        self.send_response(200)
        self.send_header("Content-Length", str(content_length))
        self.send_header('Content-Type', 'text/plain; charset=utf-8\n')
        self.send_header('ip address', self.address_string())
        self.wfile.write(b'Hello: BasicHttp!\n')
        self.end_headers()

with HTTPServer(address, MyHTTPRequestHandler) as server:
    server.serve_forever()
