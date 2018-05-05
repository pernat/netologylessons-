#!/usr/bin/python
# -*- coding: utf-8 -*-


class Animals:
    in_type = 'Хордовые'
    in_class = None
    in_order = None
    in_suborder = None
    in_family = None
    food = None
    name = None

    def __init__(self, in_class, in_order, in_suborder, in_family, food, name):
        self.in_class = in_class
        self.in_order = in_order
        self.in_suborder = in_suborder
        self.in_family = in_family
        self.food = food
        self.name = name

    def eating(self, voice):
        if self.in_order in 'Парнокопытные' and self.food == 'Комбикорм':
            print('Вы покормили парнокопытное животное -', self.name, voice)
        elif self.in_order in 'Гусеобразные и Курообразные' and self.food == 'Зерно':
            print('Вы покормили птицу -', self.name, voice)
        else:
            print('{} не подходит для животного: {} {}'.format(self.food, self.name, voice))


cow1 = Animals('Млекопитающие', 'Парнокопытные', 'Жвачные', None, 'Комбикорм', 'Корова')
cow1.weight = 500
cow1.voice = 'му-му-му'
cow1.eating(cow1.voice)

goat1 = Animals('Млекопитающие', 'Парнокопытные', 'Жвачные', None, 'Комбикорм', 'Коза')
goat1.weight = 60
goat1.voice = 'бе-бе-бе'
goat1.eating(goat1.voice)

sheep1 = Animals('Млекопитающие', 'Парнокопытные', 'Жвачные', None, 'Комбикорм', 'Овца')
sheep1.weight = 80
sheep1.voice = 'ме-ме-ме'
sheep1.eating(sheep1.voice)

pig1 = Animals('Млекопитающие', 'Парнокопытные', 'Жвачные', None, 'Комбикорм', 'Свинья')
pig1.weight = 200
pig1.voice = 'хрю-хрю'
pig1.eating(pig1.voice)

duck1 = Animals('Птицы', 'Гусеобразные и Курообразные', None, None, 'Зерно', 'Утка')
duck1.weight = 100
duck1.voice = 'кря-кря'
duck1.eating(duck1.voice)

goose1 = Animals('Птицы', 'Гусеобразные и Курообразные', None, None, 'Зерно', 'Гусь')
goose1.weight = 100
goose1.voice = 'га-га-га'
goose1.eating(goose1.voice)

cooco1 = Animals('Птицы', 'Гусеобразные и Курообразные', None, None, 'Мясо', 'Курица')
cooco1.weight = 100
cooco1.voice = 'ко-ко-ко'
cooco1.eating(cooco1.voice)
