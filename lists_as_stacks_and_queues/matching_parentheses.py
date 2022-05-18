expression = input()
parentheses = []

for i in range(len(expression)):
    if expression[i] == "(":
        parentheses.append(i)
    elif expression[i] == ")":
        start_index = parentheses.pop()
        print(expression[start_index:i + 1])


a = 1