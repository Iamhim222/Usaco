def task(n):
    if n == 1:
        print(1)
        return 
    print(n)
    task(n-1)

task(5)