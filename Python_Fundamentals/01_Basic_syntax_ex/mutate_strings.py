first = input()
second = input()
pre_string = first
new_string = first
for i in range(len(first)):
    new_string = pre_string.replace(first[i], second[i],1)
    if new_string == pre_string:
        continue
    print(new_string)
    pre_string = new_string
