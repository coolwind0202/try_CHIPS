from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import http.cookies


class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # ユーザーのCookieを標準出力に出力
        print(self.path)
        if self.path != "/":
            self.send_response(200)
            return
        
        if 'Cookie' in self.headers:
            cookie = http.cookies.SimpleCookie(self.headers['Cookie'])
            for name, value in cookie.items():
                print(f"Received cookie: {name}={value.value}")
        else:
            print("Cookie is empty")

        # レスポンスの準備
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        
        # _Host-lastAccessというCookieに現在時刻を設定
        current_time = datetime.now().isoformat(timespec='seconds')
        cookie_header = f'_Host-lastAccess={current_time}; Secure; SameSite=None; HttpOnly; Partitioned'
        self.send_header('Set-Cookie', cookie_header)

        # レスポンスの送信
        self.end_headers()
        self.wfile.write(b'<!DOCTYPE html>\n')
        self.wfile.write(b'<html>\n')
        self.wfile.write(b'<head><title>Simple Server</title></head>\n')
        self.wfile.write(b'<body>\n')
        self.wfile.write(b'<p>content</p>\n')
        self.wfile.write(b'</body>\n')
        self.wfile.write(b'</html>\n')


def run():
    host = 'localhost'
    port = 8000

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
