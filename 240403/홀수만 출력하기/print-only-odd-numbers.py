def print_odd_multiples_of_three(numbers):
    for number in numbers:
        if number % 2 != 0 and number % 3 == 0:
            print(number)

# Example usage
n = int(input())
numbers = [int(input()) for _ in range(n)]
print_odd_multiples_of_three(numbers)