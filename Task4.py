def task(n):
    global sum
    if n % 2 == 0:
        sum += n
    if n == 1:
        print(sum)
        return 
    task(n-1)

sum = 0

task(5)
