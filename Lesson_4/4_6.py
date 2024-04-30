class PresentationMixin:
    def prresentaion(self):
        print(f'Здравствуй, меня зовут {self.name}, я живу на этот свете уже целых {self.age} лет.'
              f'Как видишь, я {self.race}.\n{self.history}')


class Elf(PresentationMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.race = 'эльф'
        self.history = ('Эльфы - величественный народ. Несмотря на наше хрупкое телосложение '
               'мы очень сильны. С детства нас обучают стрельбе из лука. Также каждый эльф '
               'в какой-то степени владеет магией. Эй! Не трогай мои уши!')


class Dwarf(PresentationMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.race = 'дворф'
        self.history = ('Мы, дворфы, - один из самых древних народов на Земле. Не обращай внимания на наш '
                        'рост. Хоть мы и малы, но любой дворф с легкостью поднимет льва. Дворфы - великолепные '
                        'кузнецы, великолепно управляющиеся с любым оружием. И да, хватит меня называть Хасбиком!')

class Orc(PresentationMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.race = 'орк'
        self.history = ('Орки - очень воинственный и суровый народ. Мы всегда воюем, ведь мы созданы для войны.'
                        'С раннего детства нас подвергают суровым испытаниям, чтобы мы стали как можно сильнее.'
                        'Кто такой этот твой Шрек?')
