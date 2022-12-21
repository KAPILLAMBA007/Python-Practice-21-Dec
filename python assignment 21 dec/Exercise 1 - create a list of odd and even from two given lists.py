l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
a=l1[1::2]
b=l2[::2]
print("Element at odd-index positions from list one",a)
print("Element at even-index positions from list two",b)
c=a+b
print(c)