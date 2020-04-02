
def add(a,b):
    return int(a)+int(b)
    
def sub(a,b):
    return int(a)-int(b)
    
def mult(a,b):
    return int(a) * int(b)

def div(a,b):
    try:
        return float(int(a) / int(b))
    except Exception as e:
        print e
    
    
function_map = {'+' : add,
                '-' : sub, '*' : mult, '/' :div }

def precedence(op):
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    elif op in ['(', ')']:
        return -1

def isoperarand(op):
    if op in ['+', '-', '*', '/', '(']:
        return True
    return False

def calculator_input(data):
    data_s = []
    op_s = []
    result = 0
    data_str = ''
    prevoperand = False
    for index in range(0,len(data)):
        if data[index].isdigit():
            prevoperand = False
            data_str += data[index]
            try:
                if not data[index+1].isalnum():
                    data_s.append(data_str) 
                    data_str = ''
            except Exception as e:
                if len(data_str):
                   data_s.append(data_str)
        else:
            if data[index] == ')':
                while op_s[-1] != '(':
                    num2 = data_s.pop()
                    num1 = data_s.pop()
                    value = function_map[op_s.pop()](num1,num2)
                    data_s.append(value)
                op_s.pop()
                continue
            if len(op_s) and data[index] != '(':
                while precedence(op_s[-1]) > precedence(data[index]):
                    num2 = data_s.pop()
                    num1 = data_s.pop()
                    value = function_map[op_s.pop()](num1,num2)
                    data_s.append(value)
            prev_operand = True        
            op_s.append(data[index])

    while len(op_s):
        num2 = data_s.pop()
        num1 = data_s.pop()
        value = function_map[op_s.pop()](num1,num2)
        data_s.append(value)
    print data_s[-1]
                    

input_s = "((43+4)/2)"         
s = "(5-(1+5*3)))"
s = '(2+5*3)'
calculator_input(s)
