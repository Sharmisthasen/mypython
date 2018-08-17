a = [1,3,5]
b = [2,4,6]
c = a[:]+b[:]
print(c)
d= c[:]
d.sort(reverse=True)
print('C after coping to D : ',c)
print('print D : ', d)
c[3]=42
d.append(10)
#print(d)
c.extend([7,8,9])
print(c[::2])