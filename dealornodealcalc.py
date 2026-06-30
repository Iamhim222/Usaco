n = int(input())
e = []
for i in range(n):
  e.append(int(input())-1)

deal = int(input())
val = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
a = 0
for i in range(0,10):
  if i not in e:
    a += val[i]
b = a/(10-n)
if b < deal:
  print("deal")
else:
  print("no deal")