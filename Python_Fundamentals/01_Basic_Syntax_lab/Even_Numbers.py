n = int(input())
# even = True
for i in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f'{number} is odd!')
        # even = False
        break

# if even:
else:
    print("All numbers are even.")
