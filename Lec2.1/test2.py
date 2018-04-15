with open('dict.txt') as file:
    menu_file = file.read()
    menu_file = menu_file.splitlines()
    file.close()

var1 = list()
var2 = dict()

# Цикл для получения одного блюда и общего списка
x = 0

while x < len(menu_file):
    for q, y in enumerate(menu_file):
        var0 = list()
        if y not in '':
            var0.append([y])
            var1.append(var0)
        else:
            print('Длинна списка menu_file', len(menu_file))
            print('Длинна списка menu_var1', len(var1))
            # z = len(var1)
            # b = len
            # for z in range(len(menu_file)):
            #     menu_file.pop(z)

            # z = len(var1)
            del menu_file[0:z + 1]
            print(var1)
            break
    x += 1


# print('sdgsdgijasdlfghj', menu_file)
print('\n', var1)
# print('\n', var2)
# print(type(var1))
