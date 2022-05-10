import operator
op = {"+": "operator.add","-": "operator.sub","*": "operator.mul","/": "operator.truediv",'//': "operator.floordiv","%": "operator.mod"}

def calculator(n1,n2,opt):
    try:
        total = eval(op.get(opt))(n1,n2)
        return total
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return 0
calc = calculator(5,2,"%")
print(calc)