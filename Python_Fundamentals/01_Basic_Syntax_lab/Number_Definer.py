number = float(input())

if number == 0:
    print('zero')
else:
    if 0 < number < 1:
        print('small positive')
    elif 1 < number < 1000000:
        print('positive')
    elif number > 1000000:
        print('large positive')

    if -1 < number < 0:
        print('small negative')
    elif -1000000 < number < -1:
        print('negative')
    elif number < -1000000:
        print('large negative')

