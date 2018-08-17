# create class

class MyfirstClass :
    def __init__(self,a,b):
        print('Inside the inti functions')
        self.x= a
        self.y= b
        print('The first number is  : ',a)
        print('The second number is  : ',b)
        self.add = int(self.x)+int(self.y)
        print('Addition of the 2 numbers is : ',self.add)

in1 = input('Enter the first number :')
in2 = input('Enter the second num to add :')
ob1 = MyfirstClass(in1,in2)
#print('Add : ',ob1.add)

''' to delete object property 
        del ob1.in1
    to delete the object itself 
        del ob1
'''