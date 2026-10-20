#!/bin/bash
# Script khởi chạy ứng dụng Tạo Đề Thi Theo CV 7991

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

echo "========================================================"
echo "  Khởi động ứng dụng Tạo Đề Thi Theo CV 7991..."
echo "========================================================"

if command -v python3 &>/dev/null; then
    python3 server.py
elif command -v python &>/dev/null; then
    python server.py
else
    echo "Lỗi: Không tìm thấy Python trên máy tính của bạn."
    echo "Bạn vẫn có thể mở trực tiếp file 'index.html' bằng trình duyệt Chrome hoặc Safari."
    open index.html
fi
