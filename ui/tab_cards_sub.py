from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import Qt
from datetime import datetime


class CardSubTabLuot(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title = QLabel("QUẢN LÝ THẺ LƯỢT")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:22px; font-weight:bold; color:#2E86C1;")
        layout.addWidget(title)

        search_layout = QHBoxLayout()
        search_box = QLineEdit()
        search_box.setPlaceholderText("Nhập biển số hoặc tên khách hàng...")

        search_layout.addWidget(search_box)
        for t in ["Tìm kiếm", "Làm mới"]:
            search_layout.addWidget(QPushButton(t))
        layout.addLayout(search_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "Mã thẻ", "Biển số", "Khách hàng", "Ngày sử dụng",
            "Số lượt/Phí", "Trạng thái", "Loại thẻ", "Ghi chú"
        ])

        layout.addWidget(self.table)

        data = [
            ("L001", "70-F1 666.66", "Khách vãng lai", "2025-11-09", "20000", "Đã sử dụng", "Thẻ lượt", ""),
            ("L002", "30B-678.90", "Khách vãng lai", "2025-11-09", "15000", "Chưa sử dụng", "Thẻ lượt", "")
        ]

        self.table.setRowCount(len(data))
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                if c == 5:
                    if "Đã sử dụng" in val:
                        item.setBackground(Qt.GlobalColor.red)
                        item.setForeground(Qt.GlobalColor.white)
                    else:
                        item.setBackground(Qt.GlobalColor.green)
                        item.setForeground(Qt.GlobalColor.white)
                self.table.setItem(r, c, item)

        btn_layout = QHBoxLayout()
        for t in ["Thêm thẻ mới", "Chỉnh sửa", "Xóa thẻ", "Xem chi tiết"]:
            btn_layout.addWidget(QPushButton(t))

        layout.addLayout(btn_layout)
        self.setLayout(layout)


class CardSubTabThang(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def calculate_status(self, expiry_date):
        today = datetime.today().date()
        exp = datetime.strptime(expiry_date, "%Y-%m-%d").date()
        d = (exp - today).days

        if d < 0:
            return d, "Đã hết hạn"
        elif d <= 7:
            return d, f"Sắp hết hạn ({d} ngày)"
        return d, f"Còn hạn ({d} ngày)"

    def initUI(self):
        layout = QVBoxLayout()

        title = QLabel("QUẢN LÝ THẺ THÁNG")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:22px; font-weight:bold; color:#2E86C1;")
        layout.addWidget(title)

        table = QTableWidget()
        table.setColumnCount(9)
        table.setHorizontalHeaderLabels([
            "Mã thẻ", "Biển số", "Khách hàng", "Ngày bắt đầu", "Ngày hết hạn",
            "Số ngày còn lại", "Trạng thái", "Loại thẻ", "Ghi chú"
        ])

        data = [
            ("C101", "51C-111.22", "Lê Thị C", "2025-05-01", "2025-10-01", "", "", "Thẻ tháng", ""),
            ("C102", "49K1-999.99", "Nguyễn Minh Trí", "2025-10-01", "2025-11-09", "", "", "Thẻ tháng", "")
        ]

        table.setRowCount(len(data))

        for r, item in enumerate(data):
            card_id, plate, customer, start, end, _, _, card_type, note = item
            days, status = self.calculate_status(end)

            values = [card_id, plate, customer, start, end, str(days), status, card_type, note]

            for c, val in enumerate(values):
                cell = QTableWidgetItem(val)

                if c == 6:
                    if "hết hạn" in val:
                        cell.setBackground(Qt.GlobalColor.red)
                    elif "sắp hết hạn" in val:
                        cell.setBackground(Qt.GlobalColor.yellow)
                    else:
                        cell.setBackground(Qt.GlobalColor.green)

                table.setItem(r, c, cell)

        layout.addWidget(table)

        btns = QHBoxLayout()
        for t in ["Thêm thẻ mới", "Chỉnh sửa", "Xóa thẻ", "Xem chi tiết"]:
            btns.addWidget(QPushButton(t))

        layout.addLayout(btns)
        self.setLayout(layout)
