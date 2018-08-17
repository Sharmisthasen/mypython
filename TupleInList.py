#cls
# import gc 

#class TupleInList:

list1 = [(1,2,3), (2,3,5),(7,8,6),2,3,44]
#print(list1)

def printmgs():
    print('Print the list :',list1)

#obj = TupleInList()
printmgs()
list2=list1[0][1]
print(list2)
list1[0]= (45,7,6)
tuples = (2,3,4,1)
print(tuples.__hash__(),'Tuple hash')
#printmgs()
#list2=[[10,12,24]*3]
#print(list2)
#list2[0][2]=99
#print(list2)

