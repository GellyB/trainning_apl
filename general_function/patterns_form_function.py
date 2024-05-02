from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow

class patterns_func(QMainWindow):
    def __init__(self, number_page, ui, windows, win):
        super().__init__()

        self.ui = ui
        self.win = win

        self.ui.pattern_form.setCurrentIndex(number_page)

        self.ui.comboBox.activated[str].connect(self.onComboActiovated)

        windows.show()
        self.win.exec()

    def onComboActiovated(self, text):
        if text == "Фабричный метод":
            self.ui.pattern_form.setCurrentIndex(0)
        elif text == "Абстрактная фабрика":
            self.ui.pattern_form.setCurrentIndex(1)
        elif text == "Строитель":
            self.ui.pattern_form.setCurrentIndex(2)

    def init_ui(self):

        self.ui._to_fabric_two.clicked.connect(self._to_fabric_one)
        self.ui._to_fabric_one.clicked.connect(self._to_fabric_zero)

    def _to_fabric_one(self):
        self.fabric_pages.setCurrentIndex(1)

    def _to_fabric_zero(self):
        self.fabric_pages.setCurrentIndex(0)