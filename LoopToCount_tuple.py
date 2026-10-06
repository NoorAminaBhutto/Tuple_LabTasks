numbers = (10, 15, 20, 25, 30, 35, 40)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

result = (even_count, odd_count)

print(result)