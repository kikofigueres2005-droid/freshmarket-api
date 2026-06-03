from http.server import HTTPServer, BaseHTTPRequestHandler
import json, os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        with open('precios.json', 'r', encoding='utf-8') as f:
            self.wfile.write(f.read().encode())
    def log_message(self, format, *args):
        pass

port = int(os.environ.get('PORT', 8000))
HTTPServer(('0.0.0.0', port), Handler).serve_forever()
