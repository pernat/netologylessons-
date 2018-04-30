#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import errno
import subprocess


def get_path():
    f_list_adr = os.path.dirname(__file__)
    return f_list_adr


def get_file_list():
    f_list = os.listdir(path=get_path() + '/Source/')
    return f_list


def take_resize():
    try:
        os.makedirs(get_path() + '/Result/')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    for x in get_file_list():
        subprocess.run(['convert', '-resize', '200', get_path() + '/Source/' + x,
                        get_path() + '/Result/' + x])


if __name__ == '__main__':
    take_resize()
