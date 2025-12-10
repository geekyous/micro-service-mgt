from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QListWidget, QListWidgetItem


class NavSidebar(QListWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(200)
        self.setSpacing(2)
        self.setMouseTracking(True)
        self.setStyleSheet("""
                    QListWidget {
                        background-color: #f5f5f5;
                        border: none;
                        padding: 8px;
                    }
                    QListWidget::item:hover {
                        background-color: #e9efff;
                    }
                    QListWidget::item:selected {
                        background-color: #e9efff;
                        border-left: 4px solid #0078d4;
                        color: #0078d4;
                        font-weight: bold;
                    }
                """)

    def add_group(self, text):
        """添加分组"""
        item = QListWidgetItem(text)
        item.setFlags(Qt.ItemFlag.NoItemFlags)
        item.setSizeHint(QSize(248, 28))
        font = QFont()
        font.setBold(True)
        item.setFont(font)
        self.addItem(item)

    def add_entry(self, text, icon_path):
        icon = QIcon(icon_path)
        item = QListWidgetItem(icon, text)
        item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.addItem(item)
