from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt5.QtGui import QFont, QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer
import cv2


class RightPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.camera = None
        self._setupUi()
        self._initCamera()

    def _setupUi(self):
        vLayout = QVBoxLayout(self)
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.setSpacing(10)

        # --- CAMERA HÌNH ẢNH ---
        titleCameraLabel = QLabel("CAMERA HÌNH ẢNH")
        titleCameraLabel.setObjectName("TitleLabel")
        vLayout.addWidget(titleCameraLabel, alignment=Qt.AlignTop | Qt.AlignRight)

        # Khung hiển thị camera lớn
        self.cameraLargeLabel = QLabel()
        self.cameraLargeLabel.setFixedSize(350, 300)
        self.cameraLargeLabel.setStyleSheet("background-color: black; border: 2px solid #3498db;")
        self.cameraLargeLabel.setAlignment(Qt.AlignCenter)
        vLayout.addWidget(self.cameraLargeLabel)

        # Khung camera nhỏ (preview)
        self.cameraSmallLabel = QLabel()
        self.cameraSmallLabel.setFixedSize(150, 100)
        self.cameraSmallLabel.setStyleSheet("background-color: black; border: 2px solid #e74c3c;")
        self.cameraSmallLabel.setAlignment(Qt.AlignCenter)

        hFrame = QFrame()
        hLayout = QHBoxLayout(hFrame)
        hLayout.setContentsMargins(0, 0, 0, 0)
        hLayout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        hLayout.addWidget(self.cameraSmallLabel)
        vLayout.addWidget(hFrame, alignment=Qt.AlignRight)

        vLayout.addSpacerItem(QSpacerItem(0, 10))

        # --- CÁC LƯỢT VÀO RA GẦN ĐÂY ---
        titleHistoryLabel = QLabel("CÁC LƯỢT VÀO RA GẦN ĐÂY")
        titleHistoryLabel.setObjectName("TitleLabel")
        vLayout.addWidget(titleHistoryLabel)

        # Bảng
        historyTable = QTableWidget()
        historyTable.setRowCount(10)
        historyTable.setColumnCount(4)
        historyTable.setHorizontalHeaderLabels(["Biển số", "TG Vào", "TG Ra", "Trạng thái"])

        # Thiết lập style cho bảng
        historyTable.setStyleSheet("""
            QTableWidget {
                gridline-color: #34495e;
                background-color: #2c3e50;
                color: #ecf0f1;
                border: 1px solid #34495e;
            }
            QHeaderView::section {
                background-color: #34495e;
                color: #f1c40f;
                padding: 4px;
                border: 1px solid #34495e;
            }
        """)

        # Căn chỉnh kích thước cột
        historyTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        historyTable.verticalHeader().setVisible(False)

        # Ví dụ dữ liệu mẫu
        data_rows = [
            ("20A-123.45", "17:00", "17:05", "Đã ra"),
            ("30B-678.90", "17:01", "---", "Đang đỗ"),
            ("51C-111.22", "17:05", "17:06", "Đã ra"),
        ]

        for row, row_data in enumerate(data_rows):
            for col, item in enumerate(row_data):
                historyTable.setItem(row, col, QTableWidgetItem(item))

        vLayout.addWidget(historyTable)


        # Logo
        vdiLogoLabel = QLabel("VDI")
        vdiLogoLabel.setFont(QFont('Arial', 20, QFont.Bold))
        vdiLogoLabel.setStyleSheet("color: #3498db;")
        vLayout.addWidget(vdiLogoLabel, alignment=Qt.AlignBottom | Qt.AlignRight)

    def _initCamera(self):
        self.camera = cv2.VideoCapture(0)  # 0 = Webcam default
        self.timer = QTimer()
        self.timer.timeout.connect(self._updateFrame)
        self.timer.start(30)  # 30ms ~ 33 FPS

    def _updateFrame(self):
        if not self.camera:
            return

        ret, frame = self.camera.read()
        if not ret:
            return

        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Chuyển frame vào camera lớn
        bigImg = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        bigPixmap = QPixmap.fromImage(bigImg).scaled(self.cameraLargeLabel.size(), Qt.KeepAspectRatio)
        self.cameraLargeLabel.setPixmap(bigPixmap)

        # Camera nhỏ
        smallPixmap = QPixmap.fromImage(bigImg).scaled(self.cameraSmallLabel.size(), Qt.KeepAspectRatio)
        self.cameraSmallLabel.setPixmap(smallPixmap)

    def closeEvent(self, event):
        if self.camera:
            self.timer.stop()
            self.camera.release()
        super().closeEvent(event)
