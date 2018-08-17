def prime_Test(num):
    a=int(num)
    i = 1
    count = 0
    #print('A ',a)
    for i in range (1,a+1):
        j = a % i
       # print('J :  - ',j)
        if j == 0:
            count = count +1
            #print('count : - ',count)
        
    if count == 2:
        print (num ,'is prime .')
    else:
        print(num , 'is not prime')


number = input()
prime_Test(number)

          
