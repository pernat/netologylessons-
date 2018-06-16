#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import zip_longest
import json
import requests
import time
from Diplom import config
from tqdm import tqdm


def get_user_friends():
    """
    Get user's friends list
    """
    friend_list = 'https://api.vk.com/method/friends.get'
    request = requests.get(friend_list,
                           params=dict(
                               access_token=config.TOKEN,
                               user_id=config.TARGET_USER_ID,
                               v='5.74'
                           )
                           )
    friends = request.json()
    if friends['response']['count'] == 0:
        print('У пользователя нет друзей или они скрыты. Выход из программы')
        exit()
    return friends['response']['items']


def create_users_pack():
    """
    The formed bundle id of a user's friends to pay less to the API (on the basis that friends are not more than 10,000)
    Check for presence in the community is done by one request for the whole pack (max 500 id)
    """
    friends = list()
    if len(config.FRIEND_LIST_LEN) <= 500:
        friends.append(tuple(config.FRIEND_LIST_LEN))
    else:
        n = len(config.FRIEND_LIST_LEN) // config.USER_ID_PACK_SIZE[min(config.USER_ID_PACK_SIZE, key=lambda x: abs(x - len(config.FRIEND_LIST_LEN)))]
        friends = list(x for x in zip_longest(*[iter(config.FRIEND_LIST_LEN)] * n))
    return friends


def get_user_groups():
    """
    Get list of user groups
    """
    groups_list = 'https://api.vk.com/method/groups.get'
    request = requests.get(groups_list,
                           params=dict(
                               access_token=config.TOKEN,
                               user_id=config.TARGET_USER_ID,
                               v='5.74'
                           )
                           )
    groups_js = request.json()
    if groups_js['response']['count'] == 0:
        print('Пользователь не сотоит в группах или они скрыты. Выход из программы')
        exit()
    return groups_js['response']['items']


def get_is_member():
    """
    Sent to each group user request with service user's friends and get the answer who is and who is not
    """
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
                                       access_token=config.TOKEN,
                                       user_ids=str_users,
                                       v='5.74'
                                   )
                                   )
            groups_js = request.json()
            time.sleep(.3)
            try:
                answer_list.append((group, list(groups_js['response'])))
            except KeyError:
                continue
            finally:
                pbar.set_description("Группа: %s, %d-я пачка" % (group, x + 1))
    return answer_list


def find_unic_group():
    """
    Get groups in which only the specified user is
    """
    groups_info = get_is_member()
    not_unic_groups = list()
    for x in groups_info:
        for z in range(len(x[1])):
            if x[1][z]['member'] == 1:
                not_unic_groups.append(x[0])
    unic_groups = set(get_user_groups()).difference(set(not_unic_groups))
    return unic_groups


def get_group_info():
    """
    Get info about each group
    """
    groups = find_unic_group()
    str_groups = ", ".join(str(z) for z in groups)
    groups_list = 'https://api.vk.com/method/groups.getById'
    request = requests.get(groups_list,
                           params=dict(
                               group_ids=str_groups,
                               fields='members_count',
                               access_token=config.TOKEN,
                               v='5.74'
                           )
                           )
    time.sleep(.3)
    groups_js = request.json()
    return groups_js


def create_json():
    """
    The most important function!!!
    """
    response = get_group_info()
    itog = list()
    for x in response['response']:
        try:
            json_dic = {'name': x['name'], 'gid': x['id'], 'members_count': x['members_count']}
        except Exception:
            continue
        itog.append(json_dic)
    return json.dumps(itog, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print(create_json())
