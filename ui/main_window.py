from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from ui.tab_cards import CardTab
from ui.tab_customers import CustomerTab
from ui.tab_vehicles import VehicleTab
from ui.tab_stats import StatsTab


class ParkingManagementApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hệ thống quản lý bãi xe")
        self.setGeometry(200, 100, 1200, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tabs.addTab(CardTab(), "Quản lý thẻ")
        self.tabs.addTab(CustomerTab(), "Quản lý khách hàng")
        self.tabs.addTab(VehicleTab(), "Quản lý phương tiện")
        self.tabs.addTab(StatsTab(), "Thống kê")

        layout.addWidget(self.tabs)
        self.setLayout(layout)
