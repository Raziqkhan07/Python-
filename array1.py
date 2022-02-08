import array as arr
a=arr.array('u',['a','b','c'])

for i in range(0,3):
    print(a[i],end=" ")
a.append('r')
#a.insert()
for i in range(0,4):
   # print()
    print(a[i],end=" ")
print()
print(type('u'))