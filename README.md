# Тестовое задание от компании "ИП Фурсов Игорь Николаевич"

## Поставленное ТЗ

1. Создать Google сервис аккаунт 
2. Создать собственную таблицу Google Sheet (вручную)
3. Подключить к созданному аккаунту Google Sheets API из кода
4. Написать тесты к методам класса SpreadsheetAPI
5. Написать тесты к функциям в файле functions.py

Нет предпочтения в выборе библиотеки, способа и методов тестирования.

В ответе прикрепить ссылку на репозиторий с проектом и тестами, в readme указать главные уязвимости и список багов.

## Выполнение задания

### Багрепорт


> Используемое ПО: Python=3.10, Pytest=7.1.3, WSL: Ubuntu



    Заголовок   DeprecationWarning
    Модуль      data.ss
    Класс       SpreadsheetAPI
    Функция     get_sheet()
    Версия      0.1.0
    Критичность Trivial
    Приоритет   Low
    Статус      Новый
    Автор       Извеков А.Д.
    Назначен    Middle Python Developer
    Описание    При использовнии функции get_sheet, 
                выдает предупреждение об устаревшем модуле ssl.PROTOCOL_TLS
    Дополнение  https://photo-screen.ru/i/aiHZNnPex

---

    Заголовок   При вызове функции нет проверки на входные данные
    Модуль      data.ss
    Класс       SpreadsheetAPI
    Функция     get()
    Версия      0.1.0
    Критичность Major
    Приоритет   Medium
    Статус      Новый
    Автор       Извеков А.Д.
    Назначен    Middle Python Developer
    Описание    При вводе диапазона в неверном формате не вызывается ошибка ValueError
    Дополнение  https://photo-screen.ru/i/JEaKaXyiV

---

    Заголовок   Ошибка в результате работы функции
    Модуль      data.ss
    Класс       SpreadsheetAPI
    Функция     insert()
    Версия      0.1.0
    Критичность Critical
    Приоритет   High
    Статус      Новый
    Автор       Извеков А.Д.
    Назначен    Middle Python Developer
    Описание    При успешном добавлении возвращает None, а не True
    Дополнение  https://photo-screen.ru/i/JIch5IKSl

---

    Заголовок   Ошибка в результате работы функции
    Модуль      funcs
    Класс       -
    Функция     get_range
    Версия      0.1.0
    Критичность Medium
    Приоритет   Major
    Статус      Новый
    Автор       Извеков А.Д.
    Назначен    Middle Python Developer
    Описание    В случаях, когда не указан sheet_name подставляется None
                Например: 'None!A:B3'
    Дополнение  https://photo-screen.ru/i/pGtnOZF6h


---

    Заголовок   Нет проверки на входные данные
    Модуль      funcs
    Класс       -
    Функция     get_body_insert
    Версия      0.1.0
    Критичность Medium
    Приоритет   Low
    Статус      Новый
    Автор       Извеков А.Д.
    Назначен    Middle Python Developer
    Описание    Нет проверки на правильность входных данных
    Дополнение  


# Результаты работы

[![Maintainability](https://api.codeclimate.com/v1/badges/4a5ebc4b0aaf1d82c28d/maintainability)](https://codeclimate.com/github/IzvekovWeb/Test_Task_Fursov/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4a5ebc4b0aaf1d82c28d/test_coverage)](https://codeclimate.com/github/IzvekovWeb/Test_Task_Fursov/test_coverage)