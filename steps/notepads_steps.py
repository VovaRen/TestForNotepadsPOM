from behave import given, when, then
from Pages.notepad_page import NotePage
from Pages.notepadplus_page import NoteplusPage


@given('Open "{app}" and write text')
def step(context, app):
    context.note = NotePage()
    context.note.start_app(app)
    context.note.v_z()
    context.note.write_text()


@when('Kill "{app}" and open')
def step(context, app):
    context.note.kill_app()
    context.note.start_app(app)
    context.note.v_x()


@then('Text in "{app}"')
def step(context, app):
    context.note.eq()


@given('Open notepad++ and write text')
def step(context):
    context.note1 = NoteplusPage()
    context.note1.start_app1()
    context.note1.v_v()
    context.note1.write_text1()


@when('Kill notepad++ and open')
def step(context):
    context.note1.kill_app1()
    context.note1.start_app1()
    context.note1.v_c()


@then('Text in notepad++')
def step(context):
    context.note1.eq1()
