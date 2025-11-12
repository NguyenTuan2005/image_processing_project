from PyQt6.QtWidgets import QApplication
import sys

from ui.login_window import LoginWindow
from ui.main_window import ParkingManagementApp


if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginWindow()
    login.show()

    # Đợi user đóng login window
    while login.isVisible():
        app.processEvents()

    # Kiểm tra nếu đăng nhập thành công
    if login.accept_login:
        # Nếu là user thì vào giao diện dò biển số (MenuMain)
        if login.user_type == "user":
            from ui.MenuMain import MenuMain
            window = MenuMain()
            window.show()
            sys.exit(app.exec())
        # Nếu là admin thì vào giao diện quản lý
        elif login.user_type == "admin":
            window = ParkingManagementApp()
            window.show()
            sys.exit(app.exec())
    else:
        sys.exit()
