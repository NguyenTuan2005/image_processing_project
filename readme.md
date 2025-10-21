Demo chạy tạo ảnh
-
Link demo colab: https://colab.research.google.com/drive/1XKmuoU3nSeXVx2kdOq-xGpPbCRACuk_M

**Lưu ý:** Thay đổi Runtime type sang T4 GPU trên colab và tải các thư viện trong file <code>requirements.txt</code> trc khi chạy demo.

**Bước 1:** Chạy colab 
- Sau khi chạy 2 cells sẽ lấy được đường dẫn public:
 <code> your url is: https://xx-xx-xx.loca.lt </code>
- Lưu ý: đừng dừng cell thứ 2 trong quá trình tạo ảnh vì sẽ phải lấy lại đường dẫn public mới.

**Bước 2:** Ở project tạo file .env ở root
- Nội dung file .env: <code>COLAB_API_URL=https://xx-xx-xx.loca.lt/generate-image</code> (thay đổi thành đường dẫn lấy từ colab).

**Bước 3:** Chạy project và truy cập vào <code>http://127.0.0.1:8000/generate</code>
- Nhập prompt và chờ ảnh về.
- Lưu ý: Ảnh có thể nặng và chờ một lúc để xuất hiện trên webapp tụi mình.

Nếu mn có phương pháp nào hay hơn mình xin lắng nghe nhé vì cách này đang phải lấy url mới mỗi lần dùng colab.
