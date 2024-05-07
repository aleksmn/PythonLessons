class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def set_numerator(self, numerator):
        self.numerator = numerator

    def set_denominator(self, denominator):
        self.denominator = denominator

    def display(self):
        print(f"{self.numerator}/{self.denominator}")

    def add(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def subtract(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator - other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def divide(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator
        new_denominator = self.denominator * other_fraction.numerator
        return Fraction(new_numerator, new_denominator)

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

class MetricToEnglishConverter:
    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * 0.621371

    @staticmethod
    def miles_to_kilometers(miles):
        return miles * 1.60934

    @staticmethod
    def gallons_to_liters(gallons):
        return gallons * 3.78541

    @staticmethod
    def liters_to_gallons(liters):
        return liters * 0.264172