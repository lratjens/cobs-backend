from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = f"Hello from the backend! Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        response_data = json.dumps({"message": message})

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Cache-Control', 's-maxage=1, stale-while-revalidate')
        self.end_headers()
        self.wfile.write(response_data.encode('utf-8'))
        return
