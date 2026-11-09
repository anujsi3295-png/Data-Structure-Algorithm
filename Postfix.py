def postfix_evaluation(expression):
    stack = []

    for exp in expression:
        if ord(exp) >= 48 and ord(exp) <= 57:
            stack.append(int(exp))
        else:
            val2 = stack.pop()
            val1 = stack.pop()

            if exp == "+":
                stack.append(val1 + val2)
            elif exp == '-':
                stack.append(val1 - val2)
            elif exp == '*':
                stack.append(val1 * val2)
            elif exp == '/':
                stack.append(val1 / val2)
            elif exp == '^':
                stack.append(val1**val2)

    return stack.pop()

# expression = "23+"
# expression = "234+*"
# expression = '231*+9-'
expression = "23+45-6*+3"

print("Expression :",expression)
print(postfix_evaluation(expression))