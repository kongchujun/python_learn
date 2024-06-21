# simple_http_server.py
from http.server import SimpleHTTPRequestHandler, HTTPServer
# any request will return the same
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, this is the web server response!")

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8888), MyHandler)
    print("Server started at http://localhost:8888")
    httpd.serve_forever()
