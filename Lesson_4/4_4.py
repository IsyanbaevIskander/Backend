
def Euclid_algo(a, b):  # для сокращения дроби
    if b == 0:
        return a
    return Euclid_algo(b, a % b)


# Класс Rational для дробных чисел
class Rational:
    def __init__(self, numerator, denominator):
        gcd = Euclid_algo(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'