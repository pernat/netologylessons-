import os
import chardet
from collections import Counter
import json

file_encoding = dict()


def get_path():
    f_list_adr = os.path.dirname(__file__)
    return f_list_adr


def get_file_list():
    f_list = os.listdir(path=get_path() + '/PY1_Lesson_2.3/')
    return f_list


def get_job():
    for file_name in get_file_list():
        with open(get_path() + '/PY1_Lesson_2.3/' + file_name, 'rb') as f:
            data1 = f.read()
            result = chardet.detect(data1)
            file_encoding[file_name] = result['encoding']
    for name in get_file_list():
        print('Наиболее часто встречающиеся слова в файле {}:'.format(name))
        with open(get_path() + '/PY1_Lesson_2.3/' + name, 'r', encoding=file_encoding[name]) as f:
            data0 = json.load(f)
            data1 = data0["rss"]["channel"]["items"][0]["description"]
            data_new = json.dumps(data1, ensure_ascii=False, indent=2)
            data_new = data_new.split(' ')
            data_new.sort()
            word_list = list()
            for i in data_new:
                if len(i) > 6:
                    word_list.append(i.lower())
            count = Counter(word_list)
            print(count.most_common(10), '\n')


get_path()
get_file_list()
get_job()