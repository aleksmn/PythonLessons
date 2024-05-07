class Fraction:
    def __init__(self, numerator, denominator):
        # числитель
        self.numerator = numerator
        # знаменатель
        self.denominator = denominator


    def display(self):
        print(f"{self.numerator}/{self.denominator}")

    # сложение
    def add(self, other_fraction):
        new_numerator = ...
        new_denominator = ...
        # возвращаем дродь
        return ...
    
    # сложение
    def subtract(self, other_fraction):
        ...


f1 = Fraction(2, 5)
f2 = Fraction(3, 7)

f1.display()
f2.display()
print(f1.add(f2))