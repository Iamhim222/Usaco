def code():
  f,d = list(map(int,input().split()))
  nums = []
  bd = 0
  franchises = [[] for _ in range(f)]
  for _ in range(d):
    i = list(map(int,input().split()))
    nums = sum(i)
    for n in range(0,f):
      franchises[n].append(i[n])
    if nums%13 == 0:
      bd += nums/13
  for n in range(f):
      nums = sum(franchises[n])
      if nums%13 == 0:
        bd += nums/13
  return bd
nums = []
for _ in range(10):
  nums.append(str(int(code())))

print("\n".join(nums))