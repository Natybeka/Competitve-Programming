from pyparsing import rest_of_line


def power_recursive(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return 1 / power_recursive(x, abs(n))
    temp = n // 2
    res = power_recursive(x, temp)
    if temp % 2 == 0:
        return res * res
    return x * res * res


def power_iter(x: float, n: int) -> float:
    if n == 0:
        return 1

    if n < 0:
        x, n = 1 / x, -n
    result = 1
    while n:
        if n & 1:
            result *= x
            n -= 1
        x *= x
        n //= 2
    return result


print(power_iter(2.000, -3))

print(power_recursive(2.000, -3))
