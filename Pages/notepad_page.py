from pywinauto.application import Application


class TextNotFound(Exception):
    pass


class NotePage:

    def __init__(self):
        self.app = Application()
        self.x = []
        self.z = []

    def start_app(self, app):
        self.app.start(app)

    def write_text(self):
        self.app.Notepad.edit.type_keys('ThisIsTest')

    def v_x(self):
        x = self.app.Notepad.edit.window_text()
        return x

    def v_z(self):
        z = self.app.Notepad.edit.window_text()
        return z

    def eq(self):
        self.app.kill()
        if len(self.x) <= len(self.z):
            raise TextNotFound('Текст не найден')

    def kill_app(self):
        self.app.kill()
