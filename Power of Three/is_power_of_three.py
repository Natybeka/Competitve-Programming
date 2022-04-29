def isPowerOfThree(n: int) -> bool:
    if n < 1:
        return False
    if n == 1:
        return True
    return isPowerOfThree(n / 3)
