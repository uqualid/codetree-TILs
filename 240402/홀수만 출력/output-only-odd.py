def print_numbers(a, b):
    for i in range(a,b+1,2):
        print(i, end=' ')

# Example usage
n,m = input().split()
n= int(n)
m = int(m)
print_numbers(n,m)