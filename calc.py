#!/usr/bin/env python

class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y
	
    def sub(self,x,y):
	return x - y


if __name__ == '__main__':
    cal = Calculator()
    print(cal.add(2, 3))
    print(cal.sub(3,2))
