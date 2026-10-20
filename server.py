#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Server for App Tạo Đề Thi Theo CV 7991
Chạy máy chủ cục bộ và tự động mở trình duyệt
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import socket

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and disable aggressive caching for local dev
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def guess_type(self, path):
        if path.endswith('.js') or path.endswith('.mjs'):
            return 'application/javascript; charset=utf-8'
        if path.endswith('.css'):
            return 'text/css; charset=utf-8'
        if path.endswith('.html'):
            return 'text/html; charset=utf-8'
        if path.endswith('.json'):
            return 'application/json; charset=utf-8'
        return super().guess_type(path)

def find_available_port(start_port):
    port = start_port
    while port < start_port + 50:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
            port += 1
    return start_port

def run():
    os.chdir(DIRECTORY)
    port = find_available_port(PORT)
    url = f"http://localhost:{port}"

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), CustomHTTPHandler) as httpd:
        print("\n" + "="*60)
        print("  🎉 ỨNG DỤNG TẠO ĐỀ THI THEO CÔNG VĂN 7991 ĐANG CHẠY!")
        print("="*60)
        print(f"  👉 Truy cập ứng dụng tại: {url}")
        print("  🔑 Cấu hình API Key: Nhấn vào biểu tượng Bánh răng (Cài đặt) ở góc phải")
        print("  ⚡ Tính năng đầy đủ: Tạo đề CV 7991, Tạo đề tương tự, Sinh 3 đề biến thể")
        print("  🛑 Nhấn Ctrl+C để dừng máy chủ")
        print("="*60 + "\n")

        # Open web browser automatically
        try:
            webbrowser.open(url)
        except Exception:
            pass

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nĐã dừng máy chủ. Tạm biệt!")
            sys.exit(0)

if __name__ == "__main__":
    run()
