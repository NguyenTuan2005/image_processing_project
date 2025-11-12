from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import Qt


class VehicleTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title = QLabel("QUẢN LÝ PHƯƠNG TIỆN")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:22px; font-weight:bold; color:#2E86C1;")
        layout.addWidget(title)

        search = QHBoxLayout()
        box = QLineEdit()
        box.setPlaceholderText("Nhập biển số phương tiện...")
        search.addWidget(box)

        for t in ["Tìm kiếm", "Làm mới"]:
            search.addWidget(QPushButton(t))

        layout.addLayout(search)

        table = QTableWidget()
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels([
            "Biển số", "Loại phương tiện", "Ngày xe vào", "Ngày xe ra",
            "Số ngày gửi", "Phí gửi xe", "Ghi chú"
        ])

        layout.addWidget(table)

        data = [
            ("70-F1 666.66", "Xe máy", "2025-11-01", "2025-11-03", 2, 20000, ""),
            ("30B-678.90", "Ô tô", "2025-11-02", "2025-11-05", 3, 50000, "")
        ]

        table.setRowCount(len(data))
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                table.setItem(r, c, QTableWidgetItem(str(val)))

        btns = QHBoxLayout()
        for t in ["Thêm phương tiện", "Chỉnh sửa", "Xóa phương tiện", "Xem chi tiết"]:
            btns.addWidget(QPushButton(t))

        layout.addLayout(btns)

        self.setLayout(layout)
