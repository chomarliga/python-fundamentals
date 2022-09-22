budget = int(input())
left_money = budget
command = input()

while command != 'End':
    left_money -= int(command)
    if left_money < 0:
        print("You went in overdraft!")
        break
    command = input()

else:
    print("You bought everything needed.")
