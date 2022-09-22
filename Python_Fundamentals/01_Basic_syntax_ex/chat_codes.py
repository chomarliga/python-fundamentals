number = int(input())

for _ in range(number):
    mess = int(input())
    if mess == 88:
        print('Hello')
    elif mess == 86:
        print('How are you?')
    elif mess > 88:
        print('Bye.')
    else:
        print('GREAT!')