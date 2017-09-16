FIBBONACI SERIES
t1 = -1
t2 = 1
n=int(input("enter a value of n:"))
for i in range(n):
     t3= t1 + t2
     t1 = t2
     t2 = t3
     print(t3)
