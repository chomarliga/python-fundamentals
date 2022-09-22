command = input()
coffees = 0
actions = ['coding', 'dog', 'cat', 'movie']
while command != 'END':
    command_low = command.lower()
    if command_low in actions:
        if command.isupper():
            coffees += 2
        else:
            coffees +=1
    command = input()

if coffees <= 5:
    print(coffees)
else:
    print('You need extra sleep')
