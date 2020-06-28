from pywinauto.application import Application


class TextNotFound(Exception):
    print('Текст не найден')


class NotePage:

    def __init__(self):
        self.app = Application()
        self.check_before = None
        self.check_after = None

    def kill_app(self):
        self.app.kill(soft=True)

    def check_text(self):
        if self.check_before == self.check_after:
            raise TextNotFound
