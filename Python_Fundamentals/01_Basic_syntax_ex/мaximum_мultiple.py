divisor = int(input())
boundary = int(input())

biggest = 0

for num in range(boundary, 0, -1):
    if num % divisor == 0:
        biggest = num
        break

print(biggest)
