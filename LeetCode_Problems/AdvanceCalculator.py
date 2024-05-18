import math 
import statistics

def  add(num1,num2):
    ans = num1 + num2
    print(ans)

def  sub(num1,num2):
    ans = num1 - num2
    print(ans)
    
def  multi(num1,num2):
    ans = num1 * num2
    print(ans)

def  division(num1,num2):
     ans = 0
     try:
         ans = num1 / num2
     except ZeroDivisionError:
         print( "Divisio by zeo not allowed")
     print(ans)

def  mod(num1,num2):
    ans = num1 % num2
    print(ans)

def power(num):
   
    #pow = int(input ("Enter power "))
    ans = math.exp(num)
    print("Exponential of given number = ",ans)

def sqrroot(num):
    ans = math.sqrt(num)
    print(ans)

def nthroot(num):
    root = int(input("Enter root number "))
    ans = num ** (1/root)
    print(ans)

def sinee(num):
    ans = math.sin(num)
    print(ans)  

def cos(num):
    ans = math.cos(num)
    print(ans) 

def tanget(num):
    ans = math.tan(num)
    print(ans)

def logof(num):
    ans = math.log(num)
    print("Log of ",num," is= ",ans)

def meanof(data):
    ans = statistics.mean(data)
    print("mean = ",ans)

def modof(data):
    ans = statistics.mode(data)
    print("mode = ",ans)


def medianof(data):
    ans = statistics.median(data)
    print("median = ",ans)  
    
while True:
    print("")
    print("1:Addition")
    print("2:Substraction")
    print("3:Multiplication")
    print("4:Divide")
    print("5:mod")
    print("6:Power/Exponentiation")
    print("7:Square root ")
    print("8:nth root")
    print("9:Sin")
    print("10:Cosin")
    print("11:tan")
    print("12:log")
    print("13:Mean")
    print("14:Mode")
    print("15:Median")
    print("16:EXIT")
    print("")
    choice = int(input("Enter your choice "))
    
    if choice <= 5:

        num1 = int(input("Enter integer number1 "))
        num2 = int(input("Enter integer second number "))
        

        if choice == 1:
            add(num1,num2)
        elif choice == 2:
            sub(num1,num2)
        elif choice == 3:
            multi(num1,num2)
        elif choice == 4:
            division(num1,num2)
        elif choice == 5:
            mod(num1,num2)

    elif choice <= 11:
         num = int(input("Enter integer number "))

         if choice == 6:
            power(num)
         elif choice == 7:
             sqrroot(num)
         elif choice == 8:
             nthroot(num)
         elif choice == 9:
             sinee(num)
         elif choice == 10:
             cos(num)
         elif choice == 11:
             tanget(num)
    elif choice <= 15:
         lst = []
         n = int(input("Enter number of elements to calculate mean ,mode median: "))
         for i in range(n):
                data = int(input("Enter integer element: "))
                lst.append(data)  
         print(lst)

         if choice == 13:
            meanof(lst)
         elif choice == 14:
             modof(lst)
         else:
             medianof(lst)

    elif choice ==16:
        break

    else:
        print("Enter valid input")
         

