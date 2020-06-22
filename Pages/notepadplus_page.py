from pywinauto.application import Application


class TextNotFound(Exception):
    pass


class NoteplusPage:

    def __init__(self):
        self.app = Application()
        self.c = []
        self.v = []

    def start_app1(self):
        self.app.start(r'C:\Program Files (x86)\Notepad++\notepad1.exe')

    def write_text1(self):
        self.app.Notepad.Scintilla.type_keys('ThisIsTest')

    def v_c(self):
        c = self.app.Notepad.Scintilla.window_text()
        return c

    def v_v(self):
        v = self.app.Notepad.Scintilla.window_text()
        return v

    def eq1(self):
        self.app.kill(soft=True)
        if len(self.c) <= len(self.v):
            raise TextNotFound('Текст не найден')

    def kill_app1(self):
        self.app.kill(soft=True)
