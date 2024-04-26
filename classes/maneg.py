from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTreeWidgetItem
import sys
from classes.post_connect import *
from general_function.patterns_form_function import patterns_func

class _manag_stack():
    def __init__(self, ui, windows, win, n_ui, l_n_ui, date):

        self.ui = ui
        self.win = win

        self.ui._name_3.setText(n_ui)
        self.ui._l_name.setText(l_n_ui)
        self.ui._date_f_birth.setText(date)

        self.ui._themes.textActivated.connect(self.on_change_selection)
        self.ui._prac_id.textActivated.connect(self.on_change_practice)

        self.ui._clear.clicked.connect(self.clear)
        self.ui._into.clicked.connect(self.insert)

        self.ui._clr.clicked.connect(self.clear_test)
        self.ui._inst.clicked.connect(self.get_insert)

        self.items_in_tree()

        self.items = []
        for i in got_items():
            for j in i:
                self.items.append(str(j))

        self.prac_items = []
        for i in got_prac_items():
            for j in i:
                self.prac_items.append((str(j)))

        self.ui._prac_id.addItems(self.prac_items)
        self.ui._themes.addItems(self.items)

        self.group_functions = groups_tab_functions()
        self.group_functions.add_isp9_420ap()

        windows.show()
        self.win.exec()

    def clear(self):
        self.ui._name.clear()
        self.ui._theme_4.clear()
        self.ui._cont.clear()

    def clear_test(self):
        self.ui._name_f_test.clear()
        self.ui._theme_5.clear()
        self.ui._o_question.clear()
        self.ui._t_question.clear()
        self.ui._tr_question.clear()
        self.ui._f_question.clear()

    def insert(self):
        name = self.ui._name.text()
        cont = self.ui._cont.toPlainText()
        theme = self.ui._theme_4.text()
        insert_prac(name, cont, theme)
        self.ui._okay.setText('Задание добавлена')

    def get_insert(self):

        name = self.ui._name_f_test.text()
        theme = self.ui._theme_5.text()

        _one_q = self.ui._o_question.text()
        _two_q = self.ui._t_question.text()
        _three_q = self.ui._tr_question.text()
        _four_q = self.ui._f_question.text()

        insert_tasks(name, theme, _one_q, _two_q, _three_q, _four_q)

        self.ui._okay_2.setText('Тест добавлен')

    def on_change_selection(self, text):

        head = got_head(text)
        head = str(head[0])
        # head = head[0]
        self.ui._theme.setText(head)

        con = got_content(text)
        conc = str(con[0])
        # text = "".join(text)

        self.ui._content.clear()
        self.ui._content.append(conc)

        conc = got_conclusion(text)
        conc = str(conc[0])
        # conc = "".join(conc)
        self.ui._conc.append(conc)

    def on_change_practice(self, text):
        self.ui._name_prac.clear()
        self.ui._practice.clear()
        _name = get_prac_name(text)
        _name = str(_name[0])
        self.ui._name_prac.append(_name)

        _prac = get_practice(text)
        _prac = str(_prac[0])
        self.ui._practice.append(_prac)

    def items_in_tree(self):
        # _test = got_tree_tests()
        for i in got_tree_tests():
            item = QTreeWidgetItem(self.ui.treeWidget)
            item.setText(0, i)

        _count = _count_id = 0

        id_s = got_tree_id()

        id_for_change = id_s[0]

        for sutimes in got_tree_tasks():

            parent_item = self.ui.treeWidget.topLevelItem(_count)
            subitem = QTreeWidgetItem(parent_item)
            subitem.setText(0, sutimes)

            # Проблема!!!
            # Число count_id, когда становиться равным двум,
            if id_s[_count_id] != id_for_change:
                _count += 1
            else:
                _count_id += 1