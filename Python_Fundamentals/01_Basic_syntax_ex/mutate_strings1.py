first = input()
second = input()
last_string = first
for i in range(len(first)):
    left = second[:i+1]
    right = first[i+1:]
    current_string = left + right
    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string




