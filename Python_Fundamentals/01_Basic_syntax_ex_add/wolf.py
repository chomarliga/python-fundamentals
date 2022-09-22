string = input()
list_animals = string.split(', ')

for i in range(len(list_animals), 0, -1):
    animal = list_animals[-1]
    if i == len(list_animals) and list_animals[i-1] == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    if list_animals[i-2] == 'wolf':
        print(f'Oi! Sheep number {len(list_animals) - (i-1)}! You are about to be eaten by a wolf!')
        break


