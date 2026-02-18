#!/usr/bin/env python3
"""Simple health check server for Render.com deployment."""

import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class HealthHandler(BaseHTTPRequestHandler):
    def _send_health_response(self):
        """Send health check response."""
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            return True
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            return True
        else:
            self.send_response(404)
            self.end_headers()
            return False
    
    def do_GET(self):
        if self._send_health_response():
            self.wfile.write(b'OK')
    
    def do_HEAD(self):
        self._send_health_response()
    
    def log_message(self, format, *args):
        # Suppress logs
        pass

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    server = HTTPServer(('0.0.0.0', port), HealthHandler)
    print(f"Health check server running on port {port}")
    server.serve_forever()
