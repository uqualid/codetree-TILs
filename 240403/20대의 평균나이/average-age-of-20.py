ages = []
while True:
    age = int(input())
    if 20 <= age <= 29:
        ages.append(age)
    else:
        break

average_age = sum(ages) / len(ages)
print(f"{average_age:.2f}")