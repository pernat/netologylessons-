#!/usr/bin/python
# -*- coding: utf-8 -*-

from zeep import Client
import os

client = Client('https://www.w3schools.com/xml/tempconvert.asmx?WSDL')
result = client.service.FahrenheitToCelsius(46)

print(result)


def get_source_path():
    f_list_adr = os.path.join(os.path.sep, os.path.dirname(__file__), 'source')
    return f_list_adr


def get_avg_temp(file_path):
    temp_list = list()
    with open(file_path, 'r', encoding='utf-8') as f:
        x = f.read()
        a = x.split()
        print(a)


get_avg_temp(os.path.join(os.path.sep, get_source_path(), 'temps.txt'))
