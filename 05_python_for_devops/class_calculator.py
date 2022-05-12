import operator
import math

class calculator:
    def __init__(self, total):
        self.total = 0

    def add(self, num1, num2):
        if num2:
            self.total = operator.add(num1, num2)
            return self.total
        else:
            self.total += num1
            return self.total

    def sub(self, num1, num2):
        if num2:
            self.total = operator.sub(num1, num2)
            return self.total
        else:
            self.total -= num1
            return self.total

    def mult(self, num1, num2):
        if num2:
            self.total = operator.mul(num1, num2)
            return self.total
        else:
            self.total = operator.mul(self.total, num1)
            return self.total
    
    def div(self, num1, num2):
        if num2:
            self.total = operator.truediv(num1, num2)
            return self.total
        else:
            self.total = operator.truediv(self.total, num1)
            return self.total

    # def pow(self):

    # def log(self):

    # def showcalc(self):

    # def ac(self):
