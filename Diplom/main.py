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


def get_is_member():
    answer_list = list()
    for group in get_user_groups():
        groups_list = 'https://api.vk.com/method/groups.isMember'
        request = requests.get(groups_list,
                               params=dict(
                                   group_id=group,
                                   access_token=TOKEN,
                                   user_id='624576',
                                   v='5.74'
                               )
                               )
        groups = request.json()
        answer_list.append([group, groups])
        time.sleep(1)
    return answer_list


pprint(get_is_member())
