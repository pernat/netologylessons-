#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests


# Получаем путь к исходным файлам которые надо перевести
def get_source_path():
    f_list_adr = os.path.join(os.path.sep, os.path.dirname(__file__), 'source')
    return f_list_adr


# Получаем путь к папке куда надо сохранить
def get_destination_path():
    f_list_adr = os.path.join(os.path.sep, os.path.dirname(__file__), 'destination')
    return f_list_adr


# Получаем список исходных файлов которые надо перевести
def get_file_list():
    sql_file_list = list()
    f_list = os.listdir(path=get_source_path())
    for name in f_list:
        sql_file_list.append(name)
    return sql_file_list


# Определяем оригинальный язык по образцу текста
def lang_detector(sample_text):
    response = requests.post(
        'https://translate.yandex.net/api/v1/tr.json/detect',
        params=dict(
            sid='e3a255c5.5af6fdcd.b74adee2',
            srv='tr-text',
            text=sample_text,
            hint='en,ru',
            options='1'
        )
    )
    return response.json()


# Возвращаем json от переводчика
def get_translate(lang, text):
    response = requests.post(
        'https://translate.yandex.net/api/v1/tr.json/translate',
        params=dict(
            id='14810217.5af6f59b.39a7c3a1-1-0',
            srv='tr-text',
            lang=lang + '-ru',
            reason='paste'
        ),
        data=dict(
            text=text
        )
    )
    return response.json()


# Читаем файлы, отправляем в определитель языка, переводчик и сохраняем
def translate_and_save():
    files = get_file_list()
    for x in files:

        with open(os.path.join(os.path.sep, get_source_path(), x), 'r', encoding='utf-8') as file:
            example = file.read()
        detect_send = lang_detector(example)
        true_lang = detect_send['lang']
        translate_doc = get_translate(true_lang, example)

        with open(os.path.join(os.path.sep, get_destination_path(), x), 'w', encoding='utf-8') as file:
            temp = translate_doc['text']
            file.write(''.join(temp))


if __name__ == '__main__':
    translate_and_save()
