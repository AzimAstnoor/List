ran = int(input("Ënter the range of number:"))
a = []
for i in range(ran):
    j = int(input())
    a.append(j)
    for i in range(0, len(a)):
      for j in range(i+1, len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
print(a)