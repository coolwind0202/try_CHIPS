from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import http.cookies


class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # ユーザーのCookieを標準出力に出力
        if 'Cookie' in self.headers:
            cookie = http.cookies.SimpleCookie(self.headers['Cookie'])
            for name, value in cookie.items():
                print(f"Received cookie: {name}={value.value}")

        # レスポンスの準備
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        
        # レスポンスの送信
        self.end_headers()
        # レスポンスの送信

        # HTMLコンテンツの書き込み
        html_content = b'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Embedded iframe</title>
            </head>
            <body>
                <h1>Embedded iframe Example</h1>
                <iframe src="https://7a3b-240d-18-38-8f00-20b5-231c-7cee-2603.ngrok-free.app/" width="800" height="600"></iframe>
            </body>
            </html>
        '''
        self.wfile.write(html_content)

def run():
    host = 'localhost'
    port = 7000

    server = HTTPServer((host, port), SimpleRequestHandler)
    print(f'Starting server on {host}:{port}...')

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print('Server stopped.')


if __name__ == '__main__':
    run()
