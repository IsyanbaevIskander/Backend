from datetime import date


class Person:
    def __init__(self, name: str, city: str, birth: date):
        self.__name = name
        self.__city = city
        self.__birth = birth

    def age(self):
        copy = self.__birth
        today = date.today()
        return (today.year - copy.year -
                ((copy.month, copy.day) > (today.month, today.day)))  # сначала сравниваем месяцы, потом дни
