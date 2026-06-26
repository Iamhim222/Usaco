def sum_numbers(n):
    if n == 0:
        return 0
    result = n + sum_numbers(n-1)
    return result

print(sum_numbers(4))