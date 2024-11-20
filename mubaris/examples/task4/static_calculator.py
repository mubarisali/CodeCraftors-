import unittest
import math
class Calculator:
    def add(*args):
        return sum(args) if args else 0

    def multiply(*args):
        result = 1
        for num in args:
            result *=num
        return result if args else 1

if __name__ == "__main__":
    print(Calculator.add(1,2,3,4))
    print(Calculator.add())
    print(Calculator.multiply(1,2,3,4))
    print(Calculator.multiply())