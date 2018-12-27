a = ('a','b','c','d','e','f')
mystr = str()
for i in range(len(a)):
    mystr = mystr + a[i]
print(mystr)
mylist = []
for i in range(len(a)):
    mylist.append(a[i])
print(mylist)