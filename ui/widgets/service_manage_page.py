from typing import List

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from ui.widgets.pagination import Pagination


class ServiceManagePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cards_data: List[dict] = []
        self.init_ui()

    def init_ui(self):
        """初始化服务管理UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 工具栏
        self.toolbar = self._create_toolbar()
        layout.addWidget(self.toolbar)

        # 卡片容器
        self.card_container = QWidget()
        layout.addWidget(self.card_container, 1)

        # 分页栏
        self.pagination = Pagination()
        layout.addWidget(self.pagination)

    def _create_toolbar(self) -> QWidget:
        """创建工具栏"""
        toolbar = QWidget()
        toolbar.setFixedHeight(40)
        toolbar.setStyleSheet("background-color: #f8f9fa;border-bottom: 1px solid #dee2e6;")

        layout = QHBoxLayout(toolbar)
        layout.setContentsMargins(10, 5, 10, 5)

        # 搜索框
        search_label = QLabel("搜索:")
        layout.addWidget(search_label)

        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("输入关键字进行搜索...")
        self.search_field.textChanged.connect(self._on_search)
        layout.addWidget(self.search_field)

        # 填充布局
        layout.addStretch()

        # 刷新按钮
        self.refresh_btn = QPushButton("刷新")
        self.refresh_btn.clicked.connect(self._refresh)
        layout.addWidget(self.refresh_btn)
        return toolbar

    def _on_search(self, text: str):
        """搜索"""
        if text:
            QMessageBox.information(self, "搜索", f"{text}")

    def _refresh(self):
        """刷新函数"""
        QMessageBox.information(self, "刷新", f"点击了刷新")
