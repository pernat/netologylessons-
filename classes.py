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

    def eating(self):
        if self.in_order in 'Парнокопытные' and self.food == 'Комбикорм':
            print('Вы покормили парнокопытное животное - ', self.name)
        elif self.in_order in 'Гусеобразные и Курообразные' and self.food == 'Зерно':
            print('Вы покормили птицу - ', self.name)
        else:
            print('{} не подходит для животного: {}'.format(self.food, self.name))


# class Artiodactyls(Animals):
#     in_class = 'Млекопитающие'
#     in_order = 'Парнокопытные'
#     in_suborder = ['Жвачные', 'Мозоленогие', 'Нежвачные']


# class DomesticBird(Animals):
#     in_class = 'Птицы'
#     in_order = 'Гусеобразные и Курообразные'


Cow1 = Animals('Млекопитающие', 'Парнокопытные', 'Жвачные', None, 'Комбикорм', 'Корова')
Cow1.eating()

Goat1 = Animals('Млекопитающие', 'Парнокопытные', 'Жвачные', None, 'Комбикорм', 'Коза')
Goat1.eating()

Sheep1 = Animals('Млекопитающие', 'Парнокопытные', 'Жвачные', None, 'Комбикорм', 'Овца')
Sheep1.eating()

Pig1 = Animals('Млекопитающие', 'Парнокопытные', 'Жвачные', None, 'Комбикорм', 'Свинья')
Pig1.eating()

Duck1 = Animals('Птицы', 'Гусеобразные и Курообразные', None, None, 'Зерно', 'Утка')
Duck1.eating()

Goose1 = Animals('Птицы', 'Гусеобразные и Курообразные', None, None, 'Зерно', 'Гусь')
Goose1.eating()

Cooco1 = Animals('Птицы', 'Гусеобразные и Курообразные', None, None, 'Мясо', 'Курица')
Cooco1.eating()
