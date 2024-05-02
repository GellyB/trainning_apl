from PyQt5 import QtWidgets, uic
from classes.post_connect import *
from classes.maneg import _manag_stack
from classes.stud import _kurs_stack

class _curs_tab():
    def __init__(self, app):

        self.Form, self.Windows = uic.loadUiType("graphic/curs_tab_py.ui")

        self.Form_user, self.Windows_user = uic.loadUiType("graphic/_kurs_stack_py.ui")

        self.Form_manager, self.Windows_manager = uic.loadUiType("graphic/_kurs_maneg_py.ui")


        self.win = app
        self.windows = self.Windows()

        self.windows_user = self.Windows_user()

        self.windows_manager = self.Windows_manager()

        self.ui_user = self.Form_user()
        self.ui_user.setupUi(self.windows_user)

        self.ui_manager = self.Form_manager()
        self.ui_manager.setupUi(self.windows_manager)


        self.ui = self.Form()
        self.ui.setupUi(self.windows)

        self.ui.auth.clicked.connect(self.open_from_auth)
        self.ui.auth_2.clicked.connect(self.reg_user)
        self.ui.auth_3.clicked.connect(self.reg_manag)
        self.ui.auth_4.clicked.connect(self.auth_manag)

        self.windows.show()
        self.win.exec()

    def open_from_auth(self):

        nick = self.ui.nick_auth.text()
        pas = self.ui.pass_auth.text()
        res = auth_stud(nick, pas)

        if res:

            email = res[1]

            user_window = _kurs_stack(self.ui_user, self.windows_user, self.win, nick, email, self.windows)

            self.ui.nick_auth.clear()
            self.ui.pass_auth.clear()

            self.windows.hide()

    def reg_user(self):

        nick = self.ui.nick_auth_2.text()
        pas = self.ui.pass_auth_2.text()
        email = self.ui.pass_auth_3.text()

        res = reg_stud(nick, pas, email)
        print(res)

        if res:


            twently = _kurs_stack(self.ui_user, self.windows_user, self.win, nick, email, self.windows)

            self.ui.nick_auth.clear()
            self.ui.pass_auth.clear()
            self.ui.pass_auth_3.clear()

            self.windows.hide()

    def reg_manag(self):

        name = self.ui.nick_auth_3.text()
        l_name = self.ui.pass_auth_4.text()
        pathron = self.ui.pass_auth_8.text()
        date_f_birth = self.ui.pass_auth_9.text()
        key = self.ui.pass_auth_10.text()
        pas = self.ui.pass_auth_7.text()

        _res = maneg_regis(name, l_name, pathron, date_f_birth, key, pas)



        if _res:
            n_ui = name
            l_n_ui = l_name
            date = date_f_birth

            thrid = _manag_stack(self.ui_manager, self.windows_manager, self.win, n_ui, l_n_ui,
                                 date, self.windows)

            self.ui.nick_auth_3.clear()
            self.ui.pass_auth_4.clear()
            self.ui.pass_auth_8.clear()
            self.ui.pass_auth_9.clear()
            self.ui.pass_auth_10.clear()
            self.ui.pass_auth_7.clear()

            self.windows.hide()


    def auth_manag(self):

        name = self.ui._auth_maneg.text()
        last_name = self.ui.pass_auth_6.text()
        password_2 = self.ui.pass_auth_5.text()

        _res = maneg_auth(name, last_name, password_2)


        if _res:
            n_ui = name
            l_n_ui = last_name
            date = str(get_date(password_2))

            thrid = _manag_stack(self.ui_manager, self.windows_manager, self.win, n_ui, l_n_ui, date, self.windows)

            self.ui._auth_maneg.clear()
            self.ui.pass_auth_6.clear()
            self.ui.pass_auth_5.clear()

            self.windows.hide()