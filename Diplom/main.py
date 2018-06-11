#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import zip_longest
import json
import requests
import time
from config import TOKEN, TARGET_USER_ID
from tqdm import tqdm


# Получаем список друзей пользователя
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


# Формируем пачки id друзей пользователя чтобы меньше обращаться к API (из расчета, что друзей не более 10000)
# (проверка на присутствие в сообществе делается одним запросом для всей пачки (max 500 id))
def create_users_pack():
    friend_lst = get_user_friends()
    friends = list()
    if len(friend_lst) <= 500:
        friends.append(tuple(friend_lst))
    elif len(friend_lst) <= 1000:
        n = len(friend_lst) // 3
        friends = list(x for x in zip_longest(*[iter(friend_lst)] * n))
    elif len(friend_lst) <= 2000:
        n = len(friend_lst) // 5
        friends = list(x for x in zip_longest(*[iter(friend_lst)] * n))
    elif len(friend_lst) <= 3000:
        n = len(friend_lst) // 7
        friends = list(x for x in zip_longest(*[iter(friend_lst)] * n))
    elif len(friend_lst) <= 4000:
        n = len(friend_lst) // 9
        friends = list(x for x in zip_longest(*[iter(friend_lst)] * n))
    elif len(friend_lst) <= 5000:
        n = len(friend_lst) // 11
        friends = list(x for x in zip_longest(*[iter(friend_lst)] * n))
    elif len(friend_lst) <= 6000:
        n = len(friend_lst) // 13
        friends = list(x for x in zip_longest(*[iter(friend_lst)] * n))
    elif len(friend_lst) <= 7000:
        n = len(friend_lst) // 15
        friends = list(x for x in zip_longest(*[iter(friend_lst)] * n))
    elif len(friend_lst) <= 8000:
        n = len(friend_lst) // 17
        friends = list(x for x in zip_longest(*[iter(friend_lst)] * n))
    elif len(friend_lst) <= 9000:
        n = len(friend_lst) // 19
        friends = list(x for x in zip_longest(*[iter(friend_lst)] * n))
    else:
        n = len(friend_lst) // 20
        friends = list(x for x in zip_longest(*[iter(friend_lst)] * n))
    return friends


# Получаем список групп в которых состоит пользователь
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


# Отправляем в каждую группу пользователя запрос с пакетом друзей пользователя и получаем ответ кто состоит, а кто нет
def get_is_member():
    answer_list = list()
    users_pack_lst = create_users_pack()
    user_pack_len = len(users_pack_lst)
    user_groups = get_user_groups()
    for x in range(user_pack_len):
        users = list(filter(None, users_pack_lst[x]))
        str_users = ", ".join(str(z) for z in users)
        pbar = tqdm(user_groups)
        for group in pbar:
            groups_list = 'https://api.vk.com/method/groups.isMember'
            request = requests.get(groups_list,
                                   params=dict(
                                       group_id=group,
                                       access_token=TOKEN,
                                       user_ids=str_users,
                                       v='5.74'
                                   )
                                   )
            groups_js = request.json()
            answer_list.append((group, list(groups_js['response'])))
            pbar.set_description("Группа: %s, %d-я пачка" % (group, x + 1))
            time.sleep(.6)
    return answer_list


# Получаем группы в которых состоит только указанный пользователь
def find_unic_group():
    groups_info = get_is_member()
    not_unic_groups = list()
    for x in groups_info:
        for z in range(len(x[1])):
            if x[1][z]['member'] == 1:
                not_unic_groups.append(x[0])
    unic_groups = set(get_user_groups()).difference(set(not_unic_groups))
    return unic_groups


# Получаем инфо о каждой группе
def get_group_info():
    groups = find_unic_group()
    str_groups = ", ".join(str(z) for z in groups)
    groups_list = 'https://api.vk.com/method/groups.getById'
    request = requests.get(groups_list,
                           params=dict(
                               group_ids=str_groups,
                               fields='members_count',
                               access_token=TOKEN,
                               v='5.74'
                           )
                           )
    groups_js = request.json()
    return groups_js


# Формируем json
def create_json():
    response = get_group_info()
    itog = list()
    for x in response['response']:
        json_dic = {'name': x['name'], 'gid': x['id'], 'members_count': x['members_count']}
        itog.append(json_dic)
    return json.dumps(itog, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print('Надо немного подождать')
    print(create_json())
