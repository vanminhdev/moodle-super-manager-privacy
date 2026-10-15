# Chính sách quyền riêng tư — Moodle Super Manager
# Privacy Policy — Moodle Super Manager

Cập nhật lần cuối / Last updated: 15/10/2026

Phiên bản / Version: 1.1

---

## Tiếng Việt

Moodle Super Manager là tiện ích trình duyệt dành cho giảng viên Trường Đại học Xây dựng Hà Nội, hoạt động trên hệ thống LMS (lms.huce.edu.vn) và e-office (eoffice.huce.edu.vn) của trường.

### Dữ liệu cá nhân mà tiện ích truy cập
Khi giảng viên dùng một tính năng, tiện ích đọc (và khi được yêu cầu thì ghi) dữ liệu của **chính các khóa học mà giảng viên đang có quyền quản lý**, gồm: họ tên, mã sinh viên và email của sinh viên trong lớp, điểm số, bài nộp, bài làm quiz, nhật ký truy cập quiz (kèm địa chỉ IP do LMS ghi lại) và bảng điểm trên e-office. Dữ liệu này chỉ được dùng để hiển thị bảng điểm, báo cáo chuẩn đầu ra (CLO), cảnh báo bất thường khi chấm thi và nhập điểm, đúng mục đích giảng dạy và đánh giá.

### Dữ liệu được gửi đi đâu
- **Chỉ giữa trình duyệt của giảng viên và hai máy chủ của trường** (lms.huce.edu.vn, eoffice.huce.edu.vn), bằng phiên đăng nhập sẵn có của giảng viên — giống như giảng viên tự thao tác.
- **Tác giả tiện ích không có máy chủ nào nhận dữ liệu.** Tiện ích không thu thập, không bán, không chia sẻ dữ liệu cho tác giả hay bên thứ ba, không dùng quảng cáo, công cụ phân tích hay theo dõi.
- Cấu hình chuẩn đầu ra, điểm chấm chi tiết và dấu cấm thi / gian lận / vắng thi do giảng viên nhập được **lưu ngay trong khóa học trên LMS của trường** (trang ẩn với sinh viên), không lưu ở nơi nào khác.

### Dữ liệu lưu trên máy giảng viên
Trạng thái bật/tắt tính năng, tab đang xem, bộ lọc đã chọn và bản nháp tạm được lưu bằng bộ nhớ của trình duyệt (`chrome.storage`, `localStorage`, `sessionStorage`). Gỡ tiện ích hoặc xóa dữ liệu trình duyệt sẽ xóa các dữ liệu này. Tiện ích không đọc và không lưu mật khẩu.

### Tính năng "Kết nối AI" (tùy chọn, tắt mặc định)
Nếu giảng viên tự bật, tiện ích chỉ nói chuyện với một chương trình cầu nối **chạy trên chính máy đó** (địa chỉ 127.0.0.1) để một trợ lý AI mà giảng viên đã tự cài đặt có thể đọc hoặc thay đổi dữ liệu khóa học theo yêu cầu của giảng viên. Tiện ích không gửi dữ liệu đến máy chủ nào của tác giả. Dữ liệu mà trợ lý AI nhận được tuân theo chính sách của nhà cung cấp trợ lý AI mà giảng viên chọn; giảng viên nên cân nhắc trước khi cho phép AI xem thông tin sinh viên. Mức quyền ghi của AI (chỉ gợi ý / hỏi trước / tự làm) do giảng viên đặt.

### Mã chạy trong tiện ích
Toàn bộ mã nằm trong gói cài đặt; tiện ích không tải hay chạy mã từ bên ngoài.

### Câu hỏi và thay đổi chính sách
Câu hỏi về chính sách này: mở một mục (Issue) tại https://github.com/vanminhdev/moodle-super-manager-privacy/issues. Vì tác giả không lưu dữ liệu nào của giảng viên hay sinh viên nên không có dữ liệu để yêu cầu xóa; dữ liệu nằm trong LMS và e-office của trường (liên hệ nhà trường). Nếu chính sách thay đổi, nội dung mới sẽ được đăng tại địa chỉ này kèm ngày cập nhật.

---

## English

Moodle Super Manager is a browser extension for instructors of Hanoi University of Civil Engineering. It works only on the university's LMS (lms.huce.edu.vn) and e-office (eoffice.huce.edu.vn).

### Personal information the extension accesses
When an instructor uses a feature, the extension reads (and, when asked, writes) data of **the courses the instructor is already authorised to manage**: students' names, student IDs and email addresses, grades, submissions, quiz attempts, quiz access logs (including IP addresses recorded by the LMS) and e-office grade tables. This data is used only to display grade tables and learning-outcome (CLO) reports, to highlight anomalies when grading, and to enter grades — for teaching and assessment purposes.

### Where data goes
- **Only between the instructor's browser and the university's two servers**, using the instructor's existing login session, exactly as if the instructor did the actions by hand.
- **The extension's author operates no server that receives data.** The extension does not collect, sell or share data with the author or any third party, and uses no advertising, analytics or tracking.
- CLO configuration, detailed marks and exam-ban / cheating / absence flags entered by the instructor are **stored inside the course on the university's LMS** (in a page hidden from students), and nowhere else.

### Data stored on the instructor's device
Feature switches, the selected tab, filters and temporary drafts are kept in browser storage (`chrome.storage`, `localStorage`, `sessionStorage`). Uninstalling the extension or clearing browser data removes them. The extension does not read or store passwords.

### "AI connection" feature (optional, off by default)
If the instructor turns it on, the extension talks only to a bridge program **running on the same computer** (127.0.0.1), so that an AI assistant the instructor has installed can read or change course data at the instructor's request. The extension sends nothing to any server of the author. Whatever the AI assistant receives is governed by the policy of the AI provider the instructor chose; instructors should consider this before letting an AI see student information. The AI's write permission level (suggest only / ask first / act) is set by the instructor.

### Code
All code ships inside the package; the extension does not download or run remote code.

### Questions and policy changes
Questions about this policy: open an Issue at https://github.com/vanminhdev/moodle-super-manager-privacy/issues. Because the author stores no data about instructors or students, there is no data held by the author to delete; data lives in the university's LMS and e-office (contact the university). If this policy changes, the new version will be posted at this address with the update date.
