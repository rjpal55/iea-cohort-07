import operator
import math

def calculator(n1,n2,opt):
    op = {"+": operator.add,"-": operator.sub,"*": operator.mul,"/": operator.truediv,"//": operator.floordiv,"%": operator.mod,"log": math.log,}
    operation = op.get(opt)
    if operation:
        if opt == "log":
            try:
                return operation(n1) / operation(n2)
            except ValueError:
                print("Log of 0 is undefined")
                return None
            except ZeroDivisionError:
                print("Cannot take log base of 1")
                return None
        try:
            return operation(n1,n2)
        except ZeroDivisionError:
            print("Cannot divide by zero")
    return None

calc = calculator(49,1,"log")
print(calc)