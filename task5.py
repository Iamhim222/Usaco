def task(n,i,add):
    if n == -1:
        print(add)
        return
    try:
        add += sum(i[n])
    except:
        add += i[n]
    task(n-1,i,add)
i = [1,2,[3,4],[5,6]]
task(len(i)-1,i,0)