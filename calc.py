#!/usr/bin/env python

class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def mod(self, x, y):
        return x % y

if __name__ == '__main__':
    cal = Calculator()
    print(cal.add(22, 3))
    print(cal.sub(5, 3))
    print(cal.mul(2, 3))
    print(cal.mod(5, 3))
