import os.path
# import chardet
from chardet.universaldetector import UniversalDetector


# migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
file_encoding = dict()
detector = UniversalDetector()

q = input('Введите ключевые слова: ')


def get_path():
    f_list_adr = os.path.dirname(__file__)
    return f_list_adr


def get_file_list():
    f_list = os.listdir(path=get_path() + '/Migrations/')
    return f_list


def get_job():
    # Это была неудачная попытка определять кодировку sql файлов
    for file_name in get_file_list():
        with open(get_path() + '/Migrations/' + file_name, 'rb') as f:
            for line in f:
                detector.feed(line)
                if detector.done:
                    result = detector.result
                    file_encoding[file_name] = result['encoding']
                    break
                detector.close()
    for name in get_file_list():
        filename, file_extension = os.path.splitext(name)
        if '.sql' in file_extension:
            with open(get_path() + '/Migrations/' + name, 'r') as fdd:
                data = fdd.read()
                data = data.split()
                # Получаем список файлов и количества слов в них
                print('В файле', name, 'совпаденией - \n', data.count(q))


get_path()
get_file_list()
get_job()
