from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QStackedWidget,
    QLabel,
)

from ui.utils import path
from ui.widgets.nav_sidebar import NavSidebar
from ui.widgets.service_manage_page import ServiceManagePage


class MainWindow(QMainWindow):
    """主窗口"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("微服务管理系统")
        self.resize(800, 600)

        # 主布局
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)

        # 左侧导航栏
        self.nav_sidebar = NavSidebar()
        self.nav_sidebar.add_group("服务管理")
        self.nav_sidebar.add_entry("服务进程", path.resource_path("icons/server.png"))
        self.nav_sidebar.add_entry("资源监控", path.resource_path("icons/monitor.png"))

        self.nav_sidebar.add_group("系统选项")
        self.nav_sidebar.add_entry("设置", path.resource_path("icons/settings.png"))
        self.nav_sidebar.currentRowChanged.connect(self.switch_page)
        main_layout.addWidget(self.nav_sidebar)

        # 右侧内容区
        self.stack = QStackedWidget()

        self.page_services = ServiceManagePage(self)
        self.page_monitor = QLabel("📊 资源监控页面")
        self.page_settings = QLabel("⚙ 系统设置页面")

        self.stack.addWidget(self.page_services)
        self.stack.addWidget(self.page_monitor)
        self.stack.addWidget(self.page_settings)

        main_layout.addWidget(self.stack)

        # 默认选中首页
        self.nav_sidebar.setCurrentRow(0)

    def switch_page(self, index):
        """切换页面"""
        self.stack.setCurrentIndex(0)
