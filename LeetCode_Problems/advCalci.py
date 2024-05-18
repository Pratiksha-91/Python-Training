import re

def checkpattern(expression):
    exppart = re.findall(r'\d+\.?\d*|[()+\-*/^]', expression)
    return exppart

def calculate(expression):

    precedence = {"^":3,"*":2,"/":2,"+":1,"-":1,"(":0}
    operators = []
    operands = []

    partofexp = checkpattern(expression)

    
    def calci():
        operator = operators.pop()
        y = operands.pop()
        x = operands.pop()

        if operator == '+':
            operands.append(x + y)
        elif operator == '-':
            operands.append(x - y)
        elif operator == '*':
            operands.append(x * y)
        elif operator == '/':
            if y == 0:
                raise ZeroDivisionError("Division by zero")
            operands.append(x / y)
        elif operator == '^':
            operands.append(x ** y)
        else:
            print("Invalid operator")


    for i in partofexp:
        if i.isdigit() or '.' in i:
            operands.append(float(i))
        elif i == '(':
            operators.append(i)
        elif i == '^':
            operators.append(i)
        elif i == '*':
            operators.append(i)
        elif i == '/':
            operators.append(i)
        elif i == '+':
            operators.append(i)
        elif i == '-':
            operators.append(i)
       
        elif i == ')':
            while operators[-1] != '(':
                calci()
            operators.pop() 
        else:
              # Operator
            while operators and precedence[operators[-1]] >= precedence[i]:
                calci()
            operators.append(i)
            

    while operators:
         calci()
    
    return operands.pop()
    
       
expression = input("Enter a mathematical expression: ")
try:
    result = calculate(expression)
    print("Result:", result)
except Exception as e:
    print("Error:", e)


