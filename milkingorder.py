n,m,k = list(map(int,input().split())) # n is number of cows 
# M is amount of cows aranged into a hierarchy
# K is amount of cows arenged in spesific positions
order = list(map(int,input().split()))
milking_order = [""]*n

for i in range(k):
    c,p = list(map(int,input().split()))
    milking_order[p-1] = c

for i in range(0,n):
    if milking_order[i] == "":
        
