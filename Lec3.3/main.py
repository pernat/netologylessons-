#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import requests
from connect_data import TOKEN, MY_PAGE_ID


def get_friends():
    friend_list = 'https://api.vk.com/method/friends.get'
    request = requests.get(friend_list,
                           params=dict(
                                access_token=TOKEN,
                                v='5.74'
                                    )
                           )
    friends = request.json()
    return friends['response']['items']


def get_mutual_friends():
    link = 'https://vk.com/id'
    friend_list = 'https://api.vk.com/method/friends.getMutual'
    for x in get_friends():
        request = requests.get(friend_list,
                               params=dict(
                                   access_token=TOKEN,
                                   source_uid=MY_PAGE_ID,
                                   target_uid=x,
                                   v='5.74'
                                    )
                               )
        friends = request.json()

        if 'response' in friends and friends['response']:

            print('\n==============\nОбщие друзья с ', ''.join((link, str(x), ' ', ':')))
            print('Всего: {}'.format(len(friends['response'])))
            for friend in friends['response']:
                print('Ссылка на профиль: {}'.format(''.join((link, str(friend)))))
        time.sleep(1)


if __name__ == '__main__':
    get_mutual_friends()
