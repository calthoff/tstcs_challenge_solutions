def print_r(n):
    if n == 0:
        return
    print(n)
    n -= 1
    print_r(n)

print_r(10)
