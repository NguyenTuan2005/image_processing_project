"""
Unified CSS Styles cho toàn bộ ứng dụng.
Dùng chung cho cả Admin và Employee.

Color Scheme:
- Primary: #2c3e50 (Dark Blue)
- Accent: #3498db (Light Blue)
- Warning: #f39c12 (Orange)
- Danger: #e74c3c (Red)
- Success: #27ae60 (Green)
- Text: #ecf0f1 (Light Gray)
"""


def getGlobalStyle():
    """
    Trả về CSS stylesheet cho toàn bộ ứng dụng.
    
    Returns:
        str: CSS string
    """
    return """
        /* === MAIN WINDOW === */
        QMainWindow {
            background-color: #2c3e50;
        }
        
        /* === DEFAULT TEXT === */
        QLabel {
            color: #ecf0f1;
            font-size: 14px;
        }
        
        /* === FRAMES === */
        QFrame#StatusFrame, QFrame#FeeFrame, QFrame#CardInfoFrame {
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #34495e;
        }
        
        QFrame#VideoFrame {
            border: 2px solid #3498db;
            border-radius: 5px;
            background-color: #000000;
        }
        
        /* === TITLE LABELS === */
        QLabel#TitleLabel {
            font-size: 18px;
            font-weight: bold;
            color: #f39c12;
            border-bottom: 2px solid #f39c12;
            padding-bottom: 5px;
            margin-bottom: 10px;
        }
        
        /* === SPECIAL LABELS === */
        QLabel#ParkingLogo {
            font-size: 24px;
            font-weight: bold;
            color: #3498db;
        }
        
        QLabel#BigNumber {
            font-size: 36px;
            font-weight: bold;
            color: #e74c3c;
        }
        
        /* === INPUT FIELDS === */
        QLineEdit {
            padding: 5px;
            border: 1px solid #3498db;
            border-radius: 4px;
            background-color: #34495e;
            color: #ecf0f1;
        }
        
        QLineEdit:focus {
            border: 2px solid #3498db;
            background-color: #2c3e50;
        }
        
        /* === BUTTONS === */
        QPushButton {
            background-color: #3498db;
            color: white;
            border-radius: 4px;
            padding: 5px 10px;
            font-weight: bold;
            border: none;
        }
        
        QPushButton:hover {
            background-color: #2980b9;
        }
        
        QPushButton:pressed {
            background-color: #1b5a7a;
        }
        
        /* === TABLES === */
        QTableWidget {
            background-color: #34495e;
            color: #ecf0f1;
            border: 1px solid #2c3e50;
            gridline-color: #2c3e50;
        }
        
        QTableWidget::item {
            padding: 4px;
            border: none;
        }
        
        QTableWidget::item:selected {
            background-color: #3498db;
        }
        
        QHeaderView::section {
            background-color: #2c3e50;
            color: #f39c12;
            padding: 4px;
            border: 1px solid #34495e;
            font-weight: bold;
        }
        
        /* === MENUS === */
        QMenuBar {
            background-color: #34495e;
            color: #ecf0f1;
            border-bottom: 1px solid #2c3e50;
        }
        
        QMenuBar::item:selected {
            background-color: #3498db;
        }
        
        QMenu {
            background-color: #34495e;
            color: #ecf0f1;
            border: 1px solid #2c3e50;
        }
        
        QMenu::item:selected {
            background-color: #3498db;
        }
        
        /* === TAB WIDGET === */
        QTabWidget::pane {
            border: 1px solid #34495e;
        }
        
        QTabBar::tab {
            background-color: #34495e;
            color: #ecf0f1;
            padding: 5px 15px;
            border: 1px solid #2c3e50;
        }
        
        QTabBar::tab:selected {
            background-color: #3498db;
            color: white;
        }
        
        QTabBar::tab:hover {
            background-color: #2980b9;
        }
    """
