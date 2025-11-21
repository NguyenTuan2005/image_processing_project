from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng nhập hệ thống")
        self.setGeometry(500, 200, 400, 250)
        self.setStyleSheet("background-color: #f0f2f5;")
        self.accept_login = False
        self.user_type = None  # 'admin' hoặc 'user'
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        # Tiêu đề
        title = QLabel("HỆ THỐNG QUẢN LÝ BÃI XE")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setStyleSheet("color: #2E86C1;")
        layout.addWidget(title)

        # Username
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Tên đăng nhập")
        self.username_input.setFixedHeight(40)
        self.username_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #ccc;
                border-radius: 10px;
                padding-left: 10px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #2E86C1;
            }
        """)
        layout.addWidget(self.username_input)

        # Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Mật khẩu")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedHeight(40)
        self.password_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #ccc;
                border-radius: 10px;
                padding-left: 10px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #2E86C1;
            }
        """)
        layout.addWidget(self.password_input)

        # Nút đăng nhập
        login_btn = QPushButton("Đăng nhập")
        login_btn.setFixedHeight(40)
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #2E86C1;
                color: white;
                border-radius: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1B4F72;
            }
        """)
        login_btn.clicked.connect(self.check_login)
        layout.addWidget(login_btn)

        # Ghi chú
        note = QLabel("Admin: admin/12345 | User: user/user")
        note.setAlignment(Qt.AlignmentFlag.AlignCenter)
        note.setStyleSheet("color: #555; font-size: 12px;")
        layout.addWidget(note)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == "admin" and password == "12345":
            self.accept_login = True
            self.user_type = "admin"
            self.close()
        elif username == "user" and password == "user":
            self.accept_login = True
            self.user_type = "user"
            self.close()
        else:
            QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")
