from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

class CurrencyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        rates = {"RUB": 92.5, "EUR": 0.92}
        
        amount = query.get("amount", [None])[0]
        curr = query.get("curr", [None])[0]

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        if amount and curr in rates:
            res = float(amount) * rates[curr]
            data = {"status": "success", "result": res}
            print(f"LOG: Processed {amount} to {curr}") # Выполнение требования по логам
        else:
            data = {"status": "error", "message": "Invalid params"}
        
        self.wfile.write(json.dumps(data).encode())

if __name__ == "__main__":
    print("Server started at http://localhost:8000")
    HTTPServer(('localhost', 8000), CurrencyHandler).serve_forever() 
