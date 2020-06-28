Feature: Test for Notepad
    Scenario Outline: Text in Notepad?
        Given   Открыли <app>
        When    Написали текст в <app>
        Then    Экстренно завершили работу  <app>
        When    Открыли заново <app>
        Then    Проверили, сохранился ли текст в <app>

        Examples:
        |app|
        |notepad|
        |notepad++|