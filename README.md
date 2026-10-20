# Ứng Dụng Tạo Đề Thi Theo Công Văn 7991 (Bộ GD&ĐT)

> Hệ thống thông minh hỗ trợ giáo viên và nhà trường xây dựng đề kiểm tra, ma trận, bản đặc tả và đề thi chuẩn định dạng Công văn số **7991/BGDĐT-GDTrH** mới nhất của Bộ Giáo dục & Đào tạo.
> Bộ mã nguồn này đã được tối ưu hóa hoàn chỉnh để bạn có thể **chạy online miễn phí trên GitHub Pages**, deploy lên **Vercel**, hoặc chạy trực tiếp trên máy tính.

---

## 🌐 HƯỚNG DẪN ĐƯA LÊN GITHUB & CHẠY ONLINE MIỄN PHÍ

### Bước 1: Tạo Repository mới trên GitHub
1. Đăng nhập vào tài khoản [GitHub](https://github.com/).
2. Nhấn vào nút **New** (Tạo repository mới) hoặc truy cập: [https://github.com/new](https://github.com/new).
3. Đặt tên Repository (Ví dụ: `taodethi-cv7991`).
4. Chọn chế độ **Public** (để sử dụng tính năng GitHub Pages miễn phí).
5. Nhấn **Create repository**.

### Bước 2: Đẩy (Push) mã nguồn lên GitHub
Mở Terminal trên máy tính tại thư mục chứa bộ mã nguồn này và chạy các lệnh sau:

```bash
cd /Users/hmac/.gemini/antigravity/scratch/taodethi-cv7991

# Khởi tạo git và commit
git init
git add .
git commit -m "Khởi tạo mã nguồn Tạo Đề Thi Theo CV 7991"

# Đổi nhánh chính sang main
git branch -M main

# Liên kết với repository GitHub của bạn (thay username và repo của bạn)
git remote add origin https://github.com/<USERNAME>/taodethi-cv7991.git

# Đẩy code lên
git push -u origin main
```

*(Nếu máy tính của bạn chưa có sẵn lệnh `git`, bạn chỉ cần vào repository trên web GitHub, nhấn **Add file** -> **Upload files**, sau đó kéo thả toàn bộ các file trong thư mục này lên và bấm Commit).*

### Bước 3: Kích hoạt GitHub Pages (Chỉ mất 30 giây)
1. Trong Repository trên GitHub của bạn, vào tab **Settings** (Cài đặt) ở thanh menu trên cùng.
2. Ở thanh bên trái, chọn mục **Pages**.
3. Tại phần **Build and deployment**:
   * **Source:** Chọn `Deploy from a branch` (hoặc `GitHub Actions` vì repo đã có sẵn file workflow tự động).
   * **Branch:** Chọn `main`, thư mục `/ (root)`, rồi nhấn **Save**.
4. Chờ khoảng 1 - 2 phút, GitHub sẽ hiển thị đường link trang web của bạn:
   👉 **`https://<USERNAME>.github.io/taodethi-cv7991/`**
5. Bạn có thể gửi đường link này cho đồng nghiệp hoặc truy cập từ bất kỳ thiết bị nào (máy tính, điện thoại, máy tính bảng)!

---

## ⚡ HƯỚNG DẪN DEPLOY LÊN VERCEL (Nếu muốn có link .vercel.app)

Nếu bạn muốn có một tên miền riêng dạng `https://ten-app.vercel.app` giống hệt trang gốc:
1. Đăng nhập vào [Vercel](https://vercel.com/) bằng tài khoản GitHub.
2. Nhấn **Add New...** -> **Project**.
3. Chọn Repository `taodethi-cv7991` vừa đẩy lên GitHub và bấm **Import**.
4. Nhấn **Deploy**. Chỉ sau 15 giây, bạn sẽ nhận được đường link online tốc độ cao!

---

## 💻 HƯỚNG DẪN CHẠY TRỰC TIẾP TRÊN MÁY TÍNH (OFFLINE)

Nếu không cần đưa lên mạng, bạn có thể chạy ngay trên máy cá nhân:

### Trên macOS / Linux:
```bash
./start.sh
# Hoặc: python3 server.py
```
> Trình duyệt sẽ tự động mở trang web tại địa chỉ: **`http://localhost:8080`**

### Trên Windows:
* Nhấp đúp vào file **`start.bat`**.

### Cách đơn giản nhất (Mọi hệ điều hành):
* Nhấp đúp chuột trực tiếp vào file **`index.html`** để mở bằng Chrome, Cốc Cốc, Edge hoặc Safari.

---

## 🔑 HƯỚNG DẪN CẤU HÌNH API KEY GOOGLE GEMINI

Để AI có thể tự động tạo ma trận, đặc tả và sinh câu hỏi:

1. Truy cập trang Google AI Studio để lấy API Key miễn phí:  
   👉 **[https://aistudio.google.com/api-keys](https://aistudio.google.com/api-keys)**
2. Nhấn nút **Create API key** và sao chép mã khóa (dạng `AIzaSy...`).
3. Trong giao diện ứng dụng, bấm vào biểu tượng **⚙️ Cài đặt** ở góc trên bên phải màn hình.
4. Dán API Key vào ô và nhấn **Lưu cấu hình**.
5. Bạn có thể chọn Model mong muốn:
   * `Gemini 2.5 Flash`: Cân bằng tốc độ và chất lượng đề thi tốt nhất.
   * `Gemini 3 Flash` / `Gemini 3.8 Flash`: Thế hệ model mới với khả năng suy luận sắc bén.
   * `Gemini 2.5 Pro`: Phù hợp nhất cho các đề thi học sinh giỏi hoặc bài toán vận dụng cao.

---

## 🌟 TÍNH NĂNG CHÍNH CỦA ỨNG DỤNG

### 1. Tạo Đề Theo CV 7991 (Quy trình 4 bước chuẩn)
* **Cấu hình đề thi:** Phân loại môn học (Toán, Lý, Hóa, Sinh, Văn, Sử, Địa, Anh, Tin, Công nghệ, GDCD/GDKT&PL, KHTN...), khối lớp từ 1 - 12.
* **Upload PPCT:** Tự động đọc file Kế hoạch dạy học / Phân phối chương trình (.docx, .pdf) để phân bổ số tiết và chương bài.
* **4 Mẫu Ma trận - Đặc tả:** Đầy đủ Mẫu chuẩn Phụ lục CV 7991, Mẫu 01, Mẫu 02 và Mẫu 03 (3 tầng header).
* **Chuẩn 4 dạng thức câu hỏi:**
  * Phần I: Trắc nghiệm 4 lựa chọn (0.25đ/câu).
  * Phần II: Trắc nghiệm Đúng / Sai (mỗi câu 4 ý a, b, c, d; tính điểm 0.1 - 0.25 - 0.5 - 1.0đ).
  * Phần III: Trắc nghiệm Trả lời ngắn.
  * Phần IV: Tự luận.
* **Lối tắt nhanh:** Cho phép tải lên file Ma trận hoặc Đặc tả có sẵn để nhảy thẳng tới bước tạo đề thi.

### 2. Tạo Đề Tương Tự
* Upload 1 đề mẫu có sẵn (Word, PDF, Ảnh chụp).
* AI phân tích ma trận và sinh 1 đề mới tương đương: giữ nguyên cấu trúc và độ khó, đổi mới số liệu và ngữ cảnh kèm đáp án chi tiết (Standard hoặc Deep Dive).

### 3. Sinh 3 Đề Biến Thể
* Upload 1 đề gốc -> AI streaming sinh tuần tự 3 mã đề khác nhau (Đề 1, Đề 2, Đề 3) để tổ chức kiểm tra chống gian lận, kèm lời giải chi tiết và xuất gộp 3 đề ra Word.

### 4. Bộ Vẽ Hình & Đồ Thị Toán Học Tự Động (4-Engine)
* `bbt`: Phân tích đạo hàm, cực trị và vẽ **Bảng biến thiên** chuẩn SGK.
* `graph`: Vẽ **Đồ thị hàm số** và hệ trục tọa độ $Ox$, $Oy$.
* `geo2d`: Vẽ **Hình học phẳng 2D** (tam giác, hình chữ nhật, hình bình hành, đường tròn, vector).
* `geo3d`: Vẽ **Hình học không gian 3D** (hình chóp đáy vuông/tam giác, lăng trụ, tứ diện, hình nón, trụ, cầu).

### 5. Xuất File Microsoft Word (.docx) Chuẩn Form
* Xuất đề thi, ma trận, bản đặc tả ra file `.docx` định dạng chuẩn in ấn (Font Times New Roman, cỡ 12-13pt, căn lề chuẩn theo thể thức văn bản giáo dục).

### 6. Mở Khóa VIP Không Giới Hạn
* Đã gỡ bỏ toàn bộ cơ chế khóa thử nghiệm và quảng cáo thu phí qua Zalo của bản gốc.
* Sử dụng không giới hạn, an toàn và riêng tư.

---

## 📁 CẤU TRÚC THƯ MỤC REPOSITORY

```text
taodethi-cv7991/
├── index.html                   # Giao diện chính của ứng dụng
├── assets/
│   ├── app.js                   # Mã nguồn logic (React 19 + Math Engine + Gemini Client)
│   └── app.css                  # Giao diện Teal, 3D Card, Glassmorphism, Dark Mode
├── .github/
│   └── workflows/
│       └── deploy.yml           # Tự động triển khai lên GitHub Pages khi push code
├── .nojekyll                    # Đảm bảo GitHub Pages phục vụ đúng định dạng assets
├── .gitignore                   # Loại trừ các file rác của hệ thống
├── vercel.json                  # Cấu hình triển khai 1-click lên Vercel
├── package.json                 # Metadata dự án
├── server.py                    # Server Python chạy cục bộ
├── start.sh                     # Script khởi động nhanh cho macOS / Linux
├── start.bat                    # Script khởi động nhanh cho Windows
└── README.md                    # Tài liệu hướng dẫn sử dụng và triển khai
```
