from Pages.Notepads import NotePage


class NotepadPlus(NotePage):

    def write_text(self):
        self.app.Notepad.Scintilla.type_keys('ThisIsTest')

    def check_text_note(self):
        return self.app.Notepad.Scintilla.window_text()

    def open_app(self):
        self.app.start('notepad++')
