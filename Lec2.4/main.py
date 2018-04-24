#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
from chardet.universaldetector import UniversalDetector


def get_path():
    f_list_adr = os.path.dirname(__file__)
    return f_list_adr


def get_file_list():
    f_list = os.listdir(path=get_path() + '/Migrations/')
    return f_list


def get_job():
    file_list = get_file_list()
    file_encoding = dict()
    detector = UniversalDetector()
    # Это была неудачная попытка определять кодировку sql файлов, но почему то без этого не работает
    for file_name in file_list:
        with open(get_path() + '/Migrations/' + file_name, 'rb') as f:
            for line in f:
                detector.feed(line)
                if detector.done:
                    result = detector.result
                    file_encoding[file_name] = result['encoding']
                    break
                detector.close()
    new_file_list = file_list
    new_file_list2 = list()
    x = 0
    while True:
        q = input('Введите ключевые слова для поиска или "exit" для выхода: ')
        if q == 'exit':
            break
        if x > 0:
            new_file_list = new_file_list2
            new_file_list2 = list()
        if len(new_file_list) == 0:
            print('К сожалению больше ни чего не найдено')
            exit()
        for name in new_file_list:
            filename, file_extension = os.path.splitext(name)
            if '.sql' in file_extension:
                with open(get_path() + '/Migrations/' + name, 'r') as fdd:
                    data = fdd.read()
                    data = data.split()
                if data.count(q) > 0:
                    print('В файле', name, 'совпаденией: \n', data.count(q))
                    new_file_list2.append(name)
                else:
                    continue
        x += 1


get_job()
