#!/usr/bin/python
# -*- coding: utf-8 -*-

from zeep import Client
import os
import math


def get_source_path():
    f_list_adr = os.path.join(os.path.sep, os.path.dirname(__file__), 'source')
    return f_list_adr


# Функция средней температуры
def get_avg_temp(file_path):
    fahrenheit_temp_list = list()
    with open(file_path, 'r', encoding='utf-8') as f:
        x = f.read()
        temp_list = x.split()
    for i, z in enumerate(temp_list):
        if i == 0 or i % 2 == 0:
            fahrenheit_temp_list.append(int(z))
    avg_fahrenheit = sum(fahrenheit_temp_list) / len(fahrenheit_temp_list)
    client = Client('https://www.w3schools.com/xml/tempconvert.asmx?WSDL')
    result = client.service.FahrenheitToCelsius(avg_fahrenheit)
    print('Средняя температура за неделю по цельсию: {} C\n'.format(round(float(result), 1)))


# Функция для работы с получением валюты
def get_travel_cost(file_path):
    currency_rub = 0
    my_travel_dict = dict()
    my_travel = list()
    with open(file_path, 'r', encoding='utf-8') as f:
        x = f.read()
        temp_list = x.split()
        for z in temp_list:
            my_travel.append(z)
    x = 0
    for i in range(len(my_travel)):
        if x <= (len(my_travel) - 2):
            my_travel_dict[my_travel[x]] = [my_travel[x + 1], my_travel[x + 2]]
        x += 3
    for key in my_travel_dict:
        print('Стоимость перелета {}: {} {}'.format(key, my_travel_dict[key][0], my_travel_dict[key][1]))

        client = Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
        result = client.service.ConvertToStr(
            fromCurrency=my_travel_dict[key][1],
            toCurrency='RUB',
            amount=my_travel_dict[key][0],
            rounding='true',
            format='',
            date='',
            type=''
        )
        currency_rub += float(result.replace(',', ''))
        print('Стоимость перелета в рублях: {} RUB\n'.format(result))
    print('\nВы потратите на путешествие: {} RUB'.format(math.ceil(currency_rub)))


if __name__ == '__main__':
    get_avg_temp(os.path.join(os.path.sep, get_source_path(), 'temps.txt'))
    get_travel_cost(os.path.join(os.path.sep, get_source_path(), 'currencies.txt'))
