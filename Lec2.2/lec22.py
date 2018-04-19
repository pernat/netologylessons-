import os
import chardet
from collections import Counter

# Указываем переменные содержащие путь
f_list_adr = os.path.dirname(__file__)
f_list = os.listdir(path=f_list_adr + '/PY1_Lesson_2.3/')

file_encoding = dict()
test = list()


# Создаем словарь с кодировками для кажддого файла
for file_name in f_list:
    with open(f_list_adr + '/PY1_Lesson_2.3/' + file_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        print(result)
        file_encoding[file_name] = result['encoding']


# Открываем файлы
for name in f_list:
    print(name)
    with open(f_list_adr + '/PY1_Lesson_2.3/' + name, 'r', encoding=file_encoding[name]) as f:
        data = f.read()
        data = data.split(' ')
        data.sort()
        for i in data:
            # print(i.split())
            if len(i) > 6:
                test.append(i)
        count = Counter(test)
        key_word = max(count, key=count.get)
        print(key_word)
        print(test)
        for item in test:
            if item in key_word:
                test.remove(key_word)
        print('SDFSFSDF', test)

        # print(data)
        # print(count)

