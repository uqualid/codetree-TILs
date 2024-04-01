def print_numbers(n,m):
    for i in range(n, m-1, -2):
        print(i, end=' ')

# Example usage
a,b = input().split()
a = int(a)
b = int(b)
print_numbers(a,b)