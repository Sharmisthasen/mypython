'''
def return_me(a,b):
    c = int(a)+int(b)
    d = int(a)*int(b)
   # c=str(c)
   # d=str(d)
    return  'Addition :',c,'multiplication :',d
a=input('enter the first number')
b=input('enter the seceond number')

print(return_me(a,b))'''
def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1
    print(n)
    return fibonacci(n - 1)+ fibonacci(n - 2)
#fibonacci(5)
print(fibonacci(5))
