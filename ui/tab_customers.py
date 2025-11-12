from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import Qt


class CustomerTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title = QLabel("QUẢN LÝ KHÁCH HÀNG")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:22px; font-weight:bold; color:#2E86C1;")
        layout.addWidget(title)

        search_layout = QHBoxLayout()
        search_box = QLineEdit()
        search_box.setPlaceholderText("Nhập tên khách hàng...")

        search_layout.addWidget(search_box)
        search_layout.addWidget(QPushButton("Tìm kiếm"))
        search_layout.addWidget(QPushButton("Làm mới"))
        layout.addLayout(search_layout)

        table = QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels([
            "Mã KH", "Tên khách hàng", "Số điện thoại", "Email", "Ghi chú"
        ])
        layout.addWidget(table)

        data = [
            ("KH001", "Nguyễn Minh Trí", "0987654321", "tri@example.com", ""),
            ("KH002", "Trần Văn B", "0912345678", "vanb@example.com", "")
        ]

        table.setRowCount(len(data))
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                table.setItem(r, c, QTableWidgetItem(str(val)))

        btns = QHBoxLayout()
        for t in ["Thêm KH", "Chỉnh sửa", "Xóa KH", "Xem chi tiết"]:
            btns.addWidget(QPushButton(t))

        layout.addLayout(btns)
        self.setLayout(layout)
