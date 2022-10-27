import http.server
from prometheus_client import start_http_server
from prometheus_client import Counter

REQUESTS = Counter("index_total_requests", "Index page requested")

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello")

if __name__ == "__main__":
    start_http_server(8080)
    server  = http.server.HTTPServer(('localhost',8001), MyHandler)
    server.serve_forever()
