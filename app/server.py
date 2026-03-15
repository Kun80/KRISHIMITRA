#!/usr/bin/env python3
"""
Simple HTTP Server that serves index.html by default
"""
import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # If the path is just /, serve index.html
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

os.chdir('/Users/kundanathreya/vscode/krishimitra/app')

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    print(f"Open your browser and go to: http://localhost:{PORT}")
    httpd.serve_forever()
