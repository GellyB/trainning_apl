from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem, QTableWidgetItem, QMainWindow, QAction
from PyQt5.QtGui import QIcon
import sys
from classes.post_connect import *
from general_function.patterns_form_function import patterns_func

class _manag_stack():

    def __init__(self, ui, windows, win, n_ui, l_n_ui, date, first_window):

        self.tables = []
        self.ui = ui
        self.windows = windows
        self.win = win

        self.first_window = first_window

        self.ui._name_3.setText(n_ui)
        self.ui._l_name.setText(l_n_ui)
        self.ui._date_f_birth.setText(date)

        self.ui.actionquit.triggered.connect(self._open_first_window)
        #self.ui.actionat_first_window.triggered.connect(win.close)

        self.tables.append(self.ui._isp9_420ap_table)
        self.tables.append(self.ui._isp11_320ap_table)
        self.tables.append(self.ui._isp9_220ap_table)
        self.tables.append(self.ui._9isp_ap420_table)
        self.tables.append(self.ui._isp_table)

        self.ui._create_row_isp9_420ap.clicked.connect(lambda pos, tw=self.tables[0]: self._create_new_row(tw, pos))

        self.ui._create_row_isp11_320ap.clicked.connect(lambda pos, tw=self.tables[1]: self._create_new_row(tw, pos))

        self.ui._create_row_isp9_220ap.clicked.connect(lambda pos, tw=self.tables[2]: self._create_new_row(tw, pos))

        self.ui._create_row_9isp_ap420.clicked.connect(lambda pos, tw=self.tables[3]: self._create_new_row(tw, pos))

        self.ui._create_row_isp.clicked.connect(lambda pos, tw=self.tables[4]: self._create_new_row(tw, pos))

        self.ui._themes.textActivated.connect(self.on_change_selection)
        self.ui._prac_id.textActivated.connect(self.on_change_practice)

        self.ui._clear.clicked.connect(self.clear)
        self.ui._into.clicked.connect(self.insert)

        self.ui._clr.clicked.connect(self.clear_test)
        self.ui._inst.clicked.connect(self.get_insert)

        # Отсюда идёт часть с инициализацией окна паттернов

        self.Form_pattern, self.Windows_pattern = uic.loadUiType("graphic/patterns_from.ui")

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

        self.ui._prac_id.addItems(self.prac_items)
        self.ui._themes.addItems(self.items)

        self.group_functions = groups_functions()
        self.group_functions.add_isp(1)

        self.set_users_list(str('_isp9_420ap_table'), self.group_functions.add_isp(1))
        self.set_users_list(str('_isp11_320ap_table'), self.group_functions.add_isp(2))
        self.set_users_list(str('_isp9_220ap_table'), self.group_functions.add_isp(3))
        self.set_users_list(str('_9isp_ap420_table'), self.group_functions.add_isp(4))
        self.set_users_list(str('_isp_table'), self.group_functions.add_isp(5))

        self.ui.delete_user.clicked.connect(self.delete_current_row)

        self.ui._fabric_button.clicked.connect(lambda: self.open_patterns_form(0))

        self.windows.show()
        self.win.exec()

    def _open_first_window(self):
        self.windows.close()
        self.first_window.show()

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

    def delete_current_row(self):

        for table in self.tables:
            selected_row = table.currentRow()

            if selected_row != -1:

                user = table.item(selected_row, 0)

                self.group_functions._delete_student(user.text())
                table.removeRow(selected_row)
    def set_users_list(self, widget, res):

        widget = getattr(self.ui, widget)

        for array in res:

            row = widget.rowCount()
            widget.insertRow(row)

            for column, data in enumerate(array):

                if data is None:
                    item = QTableWidgetItem(str('None'))

                else:
                    item = QTableWidgetItem(str(data))
                    widget.setItem(row, column, item)

    def _create_new_row(self, table_widget, pos):
        table_widget.insertRow(table_widget.rowCount())

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
        self.ui._conc.setText(conc)

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
        #_test = got_tree_tests()
        for i in got_tree_tests():
            item = QTreeWidgetItem(self.ui.treeWidget)
            item.setText(0, i)

        _count = _count_id = 0


        '''tasks = {}
        for i in range(len(id_s)):
            for j in got_tree_tasks():
                tasks[int(id_s)] = j[i]'''


        for subitmes in got_tree_tasks():

            parent_item = self.ui.treeWidget.topLevelItem(int(get_task_index(subitmes)))
            subitem = QTreeWidgetItem(parent_item)
            subitem.setText(0, subitmes)

            # Проблема!!!
            # Число count_id, когда становиться равным двум,
