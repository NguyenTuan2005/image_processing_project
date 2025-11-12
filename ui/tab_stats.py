from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt


class StatsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title = QLabel("THỐNG KÊ BÃI XE")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:22px; font-weight:bold; color:#2E86C1;")
        layout.addWidget(title)

        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels([
            "Loại thẻ", "Số lượng thẻ", "Số xe hiện tại", "Doanh thu dự kiến"
        ])

        layout.addWidget(table)

        data = [
            ("Thẻ lượt", 20, 15, 5000000),
            ("Thẻ tháng", 10, 8, 12000000)
        ]

        table.setRowCount(len(data))
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                table.setItem(r, c, QTableWidgetItem(str(val)))

        self.setLayout(layout)
