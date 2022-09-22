n = int(input())

for i in range(n):
    string = input()
    # pureness = True
    # for j in range(len(string)):
    #     let = string[j]
    #     if let == ',' or let == '.' or let == "_":
    #         pureness = False
    #         break
    # if not pureness:
    if '.' in string or ',' in string or '_' in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")

