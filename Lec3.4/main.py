#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests


class YaMetInterface:
    def __init__(self, token):
        self.token = token

    def get_params(self):
        payload = {'oauth_token': self.token}
        return payload

    @property
    def get_counters(self):
        request = requests.get('https://api-metrika.yandex.ru/management/v1/counters',
                               params=self.get_params()
                               )
        return [c['id'] for c in request.json()['counters']]

    def get_counter_stat(self, id):
        request_visits = requests.get('https://api-metrika.yandex.ru/stat/v1/data?{}&{}'
                                      .format('metrics=ym:s:visits', 'ids=' + str(id)),
                                      params=self.get_params()
                                      )
        print('Количество визитов: {}'.format(request_visits.json()['totals']))

        request_users = requests.get('https://api-metrika.yandex.ru/stat/v1/data?{}&{}'
                                     .format('metrics=ym:s:users', 'ids=' + str(id)),
                                     params=self.get_params()
                                     )
        print('Количество посетителей: {}'.format(request_users.json()['totals']))

        request_views = requests.get('https://api-metrika.yandex.ru/stat/v1/data?{}&{}'
                                     .format('metrics=ym:s:pageviews', 'ids=' + str(id)),
                                     params=self.get_params()
                                     )
        print('Количество просмотров: {}'.format(request_views.json()['totals']))


def get_info():
    token = input('Введите свой токен от метрики: ')
    my_counter = YaMetInterface(token)
    for x in my_counter.get_counters:
        print('\nМетрика для счетчика с id {}'.format(x))
        my_counter.get_counter_stat(x)


if __name__ == '__main__':
    get_info()
