#!/usr/bin/python
# -*- coding: utf-8 -*-


class Animals:
    in_type = 'Хордовые'
    in_class = None
    in_order = None
    in_suborder = None
    in_family = None
    food = None

    def __init__(self, in_class, in_order, in_suborder, in_family, food):
        self.in_class = in_class
        self.in_order = in_order
        self.in_suborder = in_suborder
        self.in_family = in_family
        self.food = food

    def eating(self, name, voice):
        if self.in_order in 'Парнокопытные' and self.food == 'Комбикорм':
            print('Вы покормили парнокопытное животное -', name, voice)
        elif self.in_order in 'Гусеобразные и Курообразные' and self.food == 'Зерно':
            print('Вы покормили птицу -', name, voice)
        else:
            print('{} не подходит для животного: {} {}'.format(self.food, name, voice))


class Cow(Animals):
    voice = 'му-му-му'
    name = 'Корова'


class Goat(Animals):
    voice = 'бе-бе-бе'
    name = 'Коза'


class Duck(Animals):
    voice = 'кря-кря'
    name = 'Утка'


class Cooco(Animals):
    voice = 'ко-ко-ко'
    name = 'Курица'


cow1 = Cow('Млекопитающие', 'Парнокопытные', 'Жвачные', None, 'Комбикорм')
cow1.weight = 500
cow1.eating(Cow.name, Cow.voice)

goat1 = Goat('Млекопитающие', 'Парнокопытные', 'Жвачные', None, 'Комбикорм')
goat1.weight = 60
goat1.eating(Goat.name, Goat.voice)

duck1 = Duck('Птицы', 'Гусеобразные и Курообразные', None, None, 'Зерно')
duck1.weight = 4
duck1.eating(Duck.name, Duck.voice)

cooco1 = Cooco('Птицы', 'Гусеобразные и Курообразные', None, None, 'Мясо')
cooco1.weight = 2
cooco1.eating(Cooco.name, Cooco.voice)
