#!/usr/bin/python
# -*- coding: utf-8 -*-


APP_ID = input('Введите ID своего приложения: ')
AUTH_URL = 'https://oauth.vk.com/authorize'

auth_data = {
    'client_id': APP_ID,
    'redirect_uri': 'https://vk.com',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.74'
}

# print('?'.join((AUTH_URL, urlencode(auth_data))))


TOKEN = input('Введите свой токен: ')
MY_PAGE_ID = input('Введите id своей страницы: ')
