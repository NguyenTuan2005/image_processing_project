def getGlobalStyle():
    """
    Thiết lập CSS Style cho toàn bộ ứng dụng (dựa trên tông màu tối).
    """
    return """
        QMainWindow {
            background-color: #2c3e50; /* Màu nền xanh đậm */
        }
        QLabel {
            color: #ecf0f1; /* Màu chữ trắng sáng */
            font-size: 14px;
        }
        QFrame#StatusFrame, QFrame#FeeFrame, QFrame#CardInfoFrame {
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #34495e;
        }
        QFrame#VideoFrame {
            border: 2px solid #3498db; /* Viền xanh dương cho camera */
            border-radius: 5px;
            background-color: #000000;
        }
        QLabel#TitleLabel {
            font-size: 18px;
            font-weight: bold;
            color: #f39c12; /* Màu vàng cam cho tiêu đề */
            border-bottom: 2px solid #f39c12;
            padding-bottom: 5px;
            margin-bottom: 10px;
        }
        QLabel#ParkingLogo {
            font-size: 24px;
            font-weight: bold;
            color: #3498db; /* Màu xanh dương cho logo */
        }
        QLabel#BigNumber {
            font-size: 36px;
            font-weight: bold;
            color: #e74c3c; /* Màu đỏ cho số tiền lớn */
        }
        QLineEdit {
            padding: 5px;
            border: 1px solid #3498db;
            border-radius: 4px;
            background-color: #34495e;
            color: white;
        }
    """
