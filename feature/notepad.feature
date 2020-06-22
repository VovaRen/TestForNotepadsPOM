Feature: Test for Notepad
    Scenario: Text in Notepad?
        Given   Open "Notepad.exe" and write text
        When    Kill "Notepad.exe" and open
        Then    Text in "Notepad.exe"

    Scenario: Text in notepad++?
         Given  Open notepad++ and write text
         When   Kill notepad++ and open
         Then   Text in notepad++