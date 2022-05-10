import operator

def calculator(n1,n2,opt):
    op = {"+": operator.add,"-": operator.sub,"*": operator.mul,"/": operator.truediv,'//': operator.floordiv,"%": operator.mod,}
    operation = op.get(opt)
    if operation:
        try:
            return operation(n1,n2)
        except ZeroDivisionError:
            print("Cannot divide by zero")
    return None

calc = calculator(5,0,"/")
print(calc)