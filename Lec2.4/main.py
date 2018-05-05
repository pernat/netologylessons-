#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


def get_path():
    f_list_adr = os.path.join(os.path.sep, os.path.dirname(__file__), 'Migrations')
    return f_list_adr


def get_file_list():
    sql_file_list = list()
    f_list = os.listdir(path=get_path())
    for name in f_list:
        filename, file_extension = os.path.splitext(name)
        if file_extension == '.sql':
            sql_file_list.append(name)
    return sql_file_list


def get_job():
    file_list = get_file_list()
    while True:
        question = input('\nВведите слово для поиска или exit для выхода из программы: ')
        if question == 'exit':
            exit()
        tailings_files = list()
        for file_name in file_list:
            with open(os.path.join(os.path.sep, get_path(), file_name), 'r') as f:
                read = f.read()
                if question in read:
                    print('Найдено в файле: {}'.format(file_name))
                    tailings_files.append(file_name)
        file_list = tailings_files
        print('\nВсего найдено {} файлов по запросу: {}'.format(len(file_list), question))


if __name__ == '__main__':
    get_job()
