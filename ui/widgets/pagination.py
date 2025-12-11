from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit


class Pagination(QWidget):
    """分页组件"""
    page_changed = Signal(int)

    def __init__(self, page=1, total=1):
        super().__init__()
        self.page = page
        self.total = total
        self.init_ui()

    def init_ui(self):
        """初始化布局"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        # 上一页按钮
        self.btn_pre = QPushButton("上一页")
        self.btn_pre.clicked.connect(self.pre_page)
        layout.addWidget(self.btn_pre)

        # 页码
        self.num_label = QLabel(f"{self.page} / {self.total}")
        layout.addWidget(self.num_label)

        # 下一页按钮
        self.btn_next = QPushButton("下一页")
        self.btn_next.clicked.connect(self.next_page)
        layout.addWidget(self.btn_next)

        # 跳转输入框
        self.input_jump = QLineEdit()
        self.input_jump.setFixedWidth(50)
        self.input_jump.setPlaceholderText("跳转")
        self.input_jump.returnPressed.connect(self.jump_page)
        layout.addWidget(self.input_jump)

        layout.addStretch()
        self.update_ui()

    def update_ui(self):
        self.num_label.setText(f"{self.page}/{self.total}")
        self.btn_pre.setEnabled(self.page > 1)
        self.btn_next.setEnabled(self.page < self.total)

    def pre_page(self):
        """上一页事件"""
        if self.page > 1:
            self.page -= 1
            self.page_changed.emit(self.page)
            self.update_ui()

    def next_page(self):
        """下一页事件"""
        if self.page < self.total:
            self.page += 1
            self.page_changed.emit(self.page)
            self.update_ui()

    def jump_page(self):
        """跳转页事件"""
        try:
            num = int(self.input_jump.text())
        except:
            return
        if 1 <= num <= self.total:
            self.page = num
            self.page_changed.emit(self.page)
            self.update_ui()
