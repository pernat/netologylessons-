#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from pprint import pprint
import requests
from config import TOKEN, TARGET_USER_ID


def get_user_friends():
    friend_list = 'https://api.vk.com/method/friends.get'
    request = requests.get(friend_list,
                           params=dict(
                               access_token=TOKEN,
                               user_id=TARGET_USER_ID,
                               v='5.74'
                           )
                           )
    friends = request.json()
    return friends['response']['items']


def group(iterable, count):
    return zip(*[iter(iterable)] * count)


def get_user_groups():
    groups_list = 'https://api.vk.com/method/groups.get'
    request = requests.get(groups_list,
                           params=dict(
                               access_token=TOKEN,
                               user_id=TARGET_USER_ID,
                               v='5.74'
                           )
                           )
    groups_js = request.json()
    groups = list(groups_js['response']['items'])
    return groups


def get_is_member(a):
    answer_list = list()
    users = a[0]
    str_users = ", ".join(str(x) for x in users)
    for group in get_user_groups():
        print(group)
        groups_list = 'https://api.vk.com/method/groups.isMember'
        request = requests.get(groups_list,
                               params=dict(
                                   group_id=group,
                                   access_token=TOKEN,
                                   user_ids=str_users,
                                   v='5.74'
                               )
                               )
        groups = request.json()
        answer_list.append([group, groups['response']])
        time.sleep(0.5)
    return answer_list


split = lambda x, n: x if not x else [x[:n]]+[split([] if not -(len(x)-n) else x[-(len(x)-n):], n)][0]

a = split(get_user_friends(), 300)

pprint(get_is_member(a))