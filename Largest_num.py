
number_list = [5,88,9,74]
for i in number_list:
    print('Before sorting : ',i)

number_list.sort(reverse=True)
for i in number_list:
    print('After sorting',i)

print('The largest number among the list is :',number_list[0])  
  