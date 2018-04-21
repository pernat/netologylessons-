with open('dict.txt') as file:
    menu_file = file.read()
    menu_file = menu_file.splitlines()
    file.close()


def get_cook_book():
    diction = dict()
    dic2 = dict()
    temp = list()
    z1 = 0
    z2 = 1
    for z, y in enumerate(menu_file):
        if y in '':
            temp = []
            z1 = z+1
            z2 = z+2
            continue
        if z == z1:
            diction[y.lower()] = temp
            continue
        elif z == z2:
            dic2 = dict()
            continue
        spl = y.split(' | ')
        dic2['ingridient_name'] = spl[0]
        dic2['quantity'] = int(spl[1])
        dic2['measure'] = spl[2]

        temp.append(dic2)
        dic2 = dict()
    return diction


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


create_shop_list()
