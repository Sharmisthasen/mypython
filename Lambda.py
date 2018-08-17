def myFunc(n):
    return lambda a,b:(a*b)+n

cal = myFunc(3)
a = input('Enter A : ')
b = input ('Enter')
print(cal(4,2))