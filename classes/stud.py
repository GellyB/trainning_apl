from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTreeWidgetItem, QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QMetaObject, Qt
from classes.post_connect import *
from general_function.patterns_form_function import patterns_func

class _kurs_stack():
    def __init__(self, ui, windows, win, login, email):

        self.ui = ui
        self.win = win
        self.windows = windows

        self.ui._nic_3.setText(login)
        self.ui._email_3.setText(email)

        self.ui._themes_2.textActivated.connect(self.on_change_selection)
        self.ui.comboBox_2.textActivated.connect(self.on_change_practice)

        self.set_picture()

        # Отсюда идёт часть с инициализацией окна паттернов

        self.Form_pattern, self.Windows_pattern = uic.loadUiType("graphic/patterns_form.ui")

        self.windows_pattern = self.Windows_pattern()

        self.ui_pattern = self.Form_pattern()
        self.ui_pattern.setupUi(self.windows_pattern)


        self.items_in_tree()

        self.items = []
        for i in got_items():
            for j in i:
                self.items.append(str(j))

        self.prac_items = []
        for i in got_prac_items():
            for j in i:
                self.prac_items.append((str(j)))


        self.ui.comboBox_2.addItems(self.prac_items)
        self.ui._themes_2.addItems(self.items)

        # Здесь кнопки открытия формы паттернов

        self.ui._fabric_button.clicked.connect(lambda: self.open_patterns_form(0))

        #patterns_functions = patterns_func(self.ui)

        self.windows.show()
        self.win.exec()

    # Функция по добавлению картинок на кнопки.
    # Нужна потому, что в Qt designer они постоянно отваливаются

    def set_picture(self):

        # Кнопки каталога "Порождающие"
        self.ui._fabric_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/gen_images/fabric.png'))
        self.ui._abstract_method.setIcon(QIcon('screens_for_diplom/screens_for_diplom/gen_images/absctract_fabric.png'))
        self.ui._builder_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/gen_images/builder.png'))
        self.ui._prototype_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/gen_images/prototipe.png'))
        self.ui._singlton_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/gen_images/singlton.png'))

        # Кнопки каталога "Структурные"
        self.ui.adapter_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/struct_images/adapter.png'))
        self.ui._bridge_buttom.setIcon(QIcon('screens_for_diplom/screens_for_diplom/struct_images/bridge.png'))
        self.ui._composite_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/struct_images/composite.png'))
        self.ui._decorator_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/struct_images/decorator.png'))
        self.ui._facade_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/struct_images/facade.png'))
        self.ui._flyweight_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/struct_images/flyweight.png'))
        self.ui._proxy_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/struct_images/proxy.png'))

        # Кнопки каталога "Поведенческие"
        self.ui._chain_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/behavior_images/chain.png'))
        self.ui._command_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/behavior_images/command.png'))
        self.ui._iterator_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/behavior_images/iterator.png'))
        self.ui._mediator_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/behavior_images/mediator.png'))
        self.ui._memento_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/behavior_images/memento.png'))
        self.ui._observer_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/behavior_images/observer.png'))
        self.ui._state_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/behavior_images/state.png'))
        self.ui._strategy_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/behavior_images/strategy.png'))
        self.ui._template_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/behavior_images/template.png'))
        self.ui._bisitor_button.setIcon(QIcon('screens_for_diplom/screens_for_diplom/behavior_images/visitor.png'))


    def open_patterns_form(self, number_page):

        open_pattern_form = patterns_func(number_page, self.ui_pattern, self.windows_pattern, self.win)
        self.windows.hide()

    def on_change_selection(self, text):

        head = got_head(text)
        head = str(head[0])
        # head = head[0]
        self.ui._theme_2.setText(head)

        con = got_content(text)
        conc = str(con[0])
        # text = "".join(text)

        self.ui._content_2.clear()
        self.ui._content_2.append(conc)

        conc = got_conclusion(text)
        conc = str(conc[0])
        self.ui._conc_2.setText(conc)


    def on_change_practice(self, text):
        self.ui._name_prac.clear()
        self.ui.textBrowser_2.clear()
        _name = get_prac_name(text)
        _name = str(_name[0])
        self.ui._name_prac.append(_name)

        _prac = get_practice(text)
        _prac = str(_prac[0])
        self.ui.textBrowser_2.append(_prac)

    def items_in_tree(self):
        #_test = got_tree_tests()
        for i in got_tree_tests():
            item = QTreeWidgetItem(self.ui.treeWidget_2)
            item.setText(0, i)

        _count = _count_id = 0

        id_s = got_tree_id()

        id_for_change = id_s[0]

        for sutimes in got_tree_tasks():

            parent_item = self.ui.treeWidget_2.topLevelItem(_count)
            subitem = QTreeWidgetItem(parent_item)
            subitem.setText(0, sutimes)

            # Проблема!!!
            # Число count_id, когда становиться равным двум,
            #
            if id_s[_count_id] != id_for_change:
                _count+=1
            else:
                _count_id+=1