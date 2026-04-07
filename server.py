#!/usr/bin/env python3
"""Minimal HTTP server that returns 'Gutentag, World!'.

Run: python3 server.py
Fetch: curl http://localhost:8000/
"""
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b'Gutentag, World!'
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass  # suppress request logs


if __name__ == '__main__':
    server = HTTPServer(('', 8000), Handler)
    print('Serving on http://localhost:8000')
    server.serve_forever()
