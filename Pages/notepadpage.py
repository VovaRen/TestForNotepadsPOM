from Pages.Notepads import NotePage


class Notepad(NotePage):

    def write_text(self):
        self.app.Notepad.edit.type_keys('ThisIsTest')

    def check_text_note(self):
        return self.app.Notepad.edit.window_text()

    def open_app(self):
        self.app.start('notepad')
