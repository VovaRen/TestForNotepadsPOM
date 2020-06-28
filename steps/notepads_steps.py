from behave import given, when, then
from Pages.notepadpage import Notepad
from Pages.notepadpluspage import NotepadPlus


@given('Открыли notepad')
def step(context):
    context.note = Notepad()
    context.note.open_app()


@given('Открыли notepad++')
def step(context):
    context.note = NotepadPlus()
    context.note.open_app()


@when('Написали текст в {app}')
def step(context, app):
    context.note.check_before = context.note.check_text_note()
    context.note.write_text()


@then('Экстренно завершили работу {app}')
def step(context, app):
    context.note.kill_app()


@when('Открыли заново {app}')
def step(context, app):
    context.note.open_app()
    context.note.check_after = context.note.check_text_note()


@then('Проверили, сохранился ли текст в {app}')
def step(context, app):
    context.note.kill_app()
    context.note.check_text()
