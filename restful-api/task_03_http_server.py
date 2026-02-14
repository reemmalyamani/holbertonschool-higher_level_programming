#!/usr/bin/python3
"""
Task 03: Simple API using Python's http.server
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom request handler for our simple API"""

    def do_GET(self):
        """Handle GET requests"""

        # Root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Status endpoint
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Data endpoint (JSON)
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))

        # Undefined endpoint
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Start the HTTP server"""
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Serving on http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

