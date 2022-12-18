# calculator
def add(x,y):
    return (x+y)
def subtract(x,y):
    return (x-y)
def multiply(x,y):
    return (x*y)
def divide(x,y):
    return (x/y)
def square(x,y):
    return (x**y)
while True:
    x= int(input("enter first number : "))
    y=int(input("enter second number : "))
    print('option 1 = add')
    print('option 2 = subtract')
    print('option 3 = multiply')
    print('option 4 = divide')
    print('option 5 = square')
    choose= int(input('choose 1/2/3/4/5 = '))
    if choose== 1 :
        print(add(x,y))
    if choose== 2 :
        print(subtract(x,y))
    if choose== 3 :
        print(multiply(x,y))
    if choose== 4 :
        print(divide(x,y))
    if choose== 5 :
        print(square(x,y))
    break_condition= input("Do you want to continue? yes/no : ")
    if break_condition == 'no':
            Break 
