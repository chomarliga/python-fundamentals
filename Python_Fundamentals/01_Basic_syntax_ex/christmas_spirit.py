quantity = int(input())
days_left = int(input())
spirit = 0
money = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        money += quantity * 2
        spirit += 5
    if day %3 == 0:
        money += quantity * 8
        spirit += 13
    if day % 5 == 0:
        money += quantity * 15
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        money += 23

if days_left % 10 == 0:
    spirit -= 30

print(f"Total cost: {money}")
print(f"Total spirit: {spirit}")





