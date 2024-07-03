def print_r(n):
    if n == 0:
        return
    print(n)
    n -= 1
    print_r(n)

print_r(10)

# Code above doesn't solve the challenge "Print the numbers from 1 to 10 recursively." IMHO.
# It prints numbers from 10 to 1
# Following code will print numbers from 1 to 10 recursively.

def printing_numbers(n):
    if n > 0:
        printing_numbers(n - 1)
        print(n)
        
printing_numbers(10)
