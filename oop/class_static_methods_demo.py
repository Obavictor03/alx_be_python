class Calculator:
    calculation_type = "Arithmetic Operations"   # Class attribute

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(cls.calculation_type)
        return a * b
