class Calculator:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        try:
            ans = a / b
            return ans
        except ZeroDivisionError:
            return 'Zero division'

    @staticmethod
    def exponentiation(a, b):
        return a ** b
