string = input()

while string != 'End':
    double_string = ''
    for i in string:
        double_string += i*2
    if string != 'SoftUni':
        print(double_string)
    string = input()

