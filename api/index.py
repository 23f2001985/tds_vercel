import json
import os
from http.server import BaseHTTPRequestHandler
import urllib.parse

def load_data():
    with open(os.path.join(os.path.dirname(__file__), '..', 'q-vercel-python.json'), 'r') as file:
        return json.load(file)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        names = query.get("name", [])
        data = load_data()

        result = {"marks": []}
        for name in names:
            for entry in data:
                if entry["name"] == name:
                    result["marks"].append(entry["marks"])

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        self.wfile.write(json.dumps(result).encode())
