@echo off
chcp 65001 > nul
title Tạo Đề Thi Theo CV 7991
echo ========================================================
echo   Khởi động ứng dụng Tạo Đề Thi Theo CV 7991...
echo ========================================================

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python server.py
    goto end
)

where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    py server.py
    goto end
)

echo Không tìm thấy Python. Đang mở trực tiếp file index.html...
start index.html

:end
pause
