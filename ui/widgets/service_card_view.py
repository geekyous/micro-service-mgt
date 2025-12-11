from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class ServiceCardView(QWidget):
    def __init__(self):
        super().__init__()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(5)
        layout.setContentsMargins(10, 10, 10, 10)

        # 所属组别
        group_label = QLabel("妇幼大数据管控系统")
        layout.addWidget(group_label)
