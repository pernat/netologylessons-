class Animals:
    in_type = 'Хордовые'
    in_class = None
    in_order = None
    in_suborder = None
    in_family = None
    food = None
    name = None

    def eating(self):
        if self.in_order in 'Парнокопытные' and self.food == 'Комбикорм':
            print('Вы покормили парнокопытное животное - ', self.name)
        elif self.in_order in 'Гусеобразные и Курообразные' and self.food == 'Зерно':
            print('Вы покормили птицу - ', self.name)
        else:
            print('Этот корм не подходит')


class Artiodactyls(Animals):
    in_class = 'Млекопитающие'
    in_order = 'Парнокопытные'
    in_suborder = ['Жвачные', 'Мозоленогие', 'Нежвачные']


class DomesticBird(Animals):
    in_class = 'Птицы'
    in_order = 'Гусеобразные и Курообразные'



Cow1 = Artiodactyls()
Cow1.name = 'Корова'
Cow1.food = 'Комбикорм'
Cow1.eating()

Goat1 = Artiodactyls()
Goat1.name = 'Коза'
Goat1.food = 'Комбикорм'
Goat1.eating()

Sheep1 = Artiodactyls()
Sheep1.name = 'Овца'
Sheep1.food = 'Комбикорм'
Sheep1.eating()

Pig1 = Artiodactyls()
Pig1.name = 'Свинья'
Pig1.food = 'Комбикорм'
Pig1.eating()

Duck1 = DomesticBird()
Duck1.name = 'Утка'
Duck1.food = 'Зерно'
Duck1.eating()

Goose1 = DomesticBird()
Goose1.name = 'Гусь'
Goose1.food = 'Зерно'
Goose1.eating()

Cooco1 = DomesticBird()
Cooco1.name = 'Курица'
Cooco1.food = 'Мясо'
Cooco1.eating()
