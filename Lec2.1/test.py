# def get_lst():
with open('dict.txt') as file:
    menu_file = file.read()
    menu_file = menu_file.splitlines()
    file.close()


print(menu_file)
dishes = list()
persons = list()
ingridient_name = list()
quantity = list()
measure = list()
cook_book = dict()
test = list()

dishes.append(menu_file[0])
persons.append(menu_file[1])

for x, y in enumerate(menu_file):
    print('Это x: ', x, 'Это у: ', y)
    if y == "":
        print('ЫФУРПЛЫОРПЛЫРВПЛО', x)
        dishes.append(menu_file[x + 1])
        persons.append(menu_file[x + 2])
print('Блюда: ', dishes)
print('Персон: ', persons)

b = len(persons)

print(b)
print(type(b))

    # teat_lst = list()
    # dishes = list()
    # for line in file:
    #     test = line.strip()
    #     teat_lst.append(test)
    # print(teat_lst)
    # count = 0
    # for x, y in enumerate(teat_lst):
    #     p = y.split(' | ')
    #     print(p)
    #     if y == "":
    #         dishes.append(teat_lst[x + 1])
    #     count += 1
    # print('\n', dishes)
    # file.close()

