string = input()

low_string = string.lower()
counter = 0

counter += low_string.count('water')
counter += low_string.count('sand')
counter += low_string.count('fish')
counter += low_string.count('sun')

print(counter)



