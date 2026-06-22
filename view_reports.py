#!/usr/bin/env python3
"""Simple HTTP server to view test reports"""
import http.server
import socketserver
import os
import sys

PORT = 8000

# Change to framework directory
if os.path.exists('framework'):
    os.chdir('framework')

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

try:
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"\n🌎 Server running at http://localhost:{PORT}")
        print(f"\n📊 View Reports:")
        print(f"   Combined Cucumber: http://localhost:{PORT}/tests/reports/")
        print(f"   API Reports: http://localhost:{PORT}/tests/api/reports/")
        print(f"   UI Reports: http://localhost:{PORT}/tests/bdd/reports/")
        print(f"\nPress Ctrl+C to stop\n")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\nServer stopped.")
    sys.exit(0)
