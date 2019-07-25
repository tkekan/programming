
def add(a,b):
    return int(a)+int(b)
    
def sub(a,b):
    return int(a)-int(b)
    
def mult(a,b):
    return int(a) * init(b)

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

def calculator_input(data):
    data = list(data)
    data_s = []
    op_s = []
    result = 0
    operator = None
    data_str = ''
    for index in range(0,len(data)):
        if data[index].isalnum():
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
                    data_s.push(value)
                    
            op_s.append(data[index])

    while len(op_s):
        num2 = data_s.pop()
        num1 = data_s.pop()
        value = function_map[op_s.pop()](num1,num2)
        data_s.append(value)
    print data_s[-1]
                    

input_s = "(43+4)/2"         
calculator_input(input_s)
