def isPowerOfFour(n: int) -> bool:
    if n < 1:
        return False
    if n == 1:
        return True
    return isPowerOfFour(n / 4)
