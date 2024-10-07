from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json
import os

ALLOWED_ORIGINS = os.environ.get('ALLOWED_ORIGINS', '*').split(',')

class handler(BaseHTTPRequestHandler):

    def get_allowed_origin(self):
        origin = self.headers.get('Origin')
        if origin in ALLOWED_ORIGINS:
            return origin
        return ALLOWED_ORIGINS[0] if ALLOWED_ORIGINS else '*'

    def do_GET(self):
        message = f"Hello from the backend! Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        response_data = json.dumps({"message": message})

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', self.get_allowed_origin())
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.send_header('Cache-Control', 's-maxage=1, stale-while-revalidate')
        self.end_headers()
        self.wfile.write(response_data.encode('utf-8'))
        return

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.end_headers()
        return
