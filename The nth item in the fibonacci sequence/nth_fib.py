from typing import List
# Description
# Find the nth number in the fibonacci sequence
# Solution memoization
# save values of the computations to avoid repeating them
# if value has been computed just return the value
# otherwise call the function fib(n - 1) + fib(n - 2)


def fib(n: int) -> int:
    mem = [None] * (n + 1)
    result = fib_helper(n, mem)
    return result


def fib_helper(n: int, mem: List[int]) -> int:
    if mem[n]:
        return mem[n]

    if n == 1 or n == 2:
        result = 1
    elif n == 0:
        result = 0
    else:
        result = fib_helper(n - 1, mem) + fib_helper(n - 2, mem)
    mem[n] = result
    return result


print(fib(5))
