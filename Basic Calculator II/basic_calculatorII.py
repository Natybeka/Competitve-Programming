def calculate(s: str) -> int:
    n = len(s)
    currentNumber = 0
    operator = "+"
    stack = []
    for i in range(n):
        if s[i].isdigit():
            currentNumber = currentNumber * 10 + int(s[i])
        if not s[i].isdigit() and not s[i].isspace() or i == n - 1:
            if operator == "+":
                stack.append(currentNumber)
            elif operator == "-":
                stack.append(-currentNumber)
            elif operator == "*":
                stack.append(stack.pop() * currentNumber)
            elif operator == "/":
                temp = stack.pop()
                if temp < 0 and temp % currentNumber != 0:
                    stack.append(temp // currentNumber + 1)
                else:
                    stack.append(temp // currentNumber)

            currentNumber = 0
            operator = s[i]

    result = 0
    print(stack)
    while stack:
        result += stack.pop()
    return result


print(calculate("3/2"))
