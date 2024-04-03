count_even = 0
for _ in range(5):
    number = int(input())
    if number % 2 == 0:
        count_even += 1

print(count_even)