#!/usr/bin/python
# -*- coding: utf-8 -*-


def get_cook_book():
    with open('dict.txt') as file:
        menu_file = list()
        for u in file:
            new_file = u.strip()
            menu_file.append(new_file)
    cook_book_diction = dict()
    list_for_dish = list()
    z1 = 0
    z2 = 1
    for z, y in enumerate(menu_file):
        if not y:
            list_for_dish = []
            z1 = z+1
            z2 = z+2
            continue
        if z == z1:
            cook_book_diction[y.lower()] = list_for_dish
            continue
        elif z == z2:
            dict_for_ingridients = dict()
            continue
        spl = y.split(' | ')
        dict_for_ingridients['ingridient_name'] = spl[0]
        dict_for_ingridients['quantity'] = int(spl[1])
        dict_for_ingridients['measure'] = spl[2]
        list_for_dish.append(dict_for_ingridients)
        dict_for_ingridients = dict()
    return cook_book_diction


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = get_cook_book()
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


if __name__ == '__main__':
    create_shop_list()
