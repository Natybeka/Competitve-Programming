# Description
# You are given a positive integer p. Consider an array nums (1-indexed) that consists of the integers in the inclusive range [1, 2p - 1] in their binary representations. You are allowed to do the following operation any number of times:

# Choose two elements x and y from nums.
# Choose a bit in x and swap it with its corresponding bit in y. Corresponding bit refers to the bit that is in the same position in the other integer.
# For example, if x = 1101 and y = 0011, after swapping the 2nd bit from the right, we have x = 1111 and y = 0001.

# Find the minimum non-zero product of nums after performing the above operation any number of times. Return this product modulo 109 + 7.

# Input: p = 3
# Output: 1512
# Explanation: nums = [001, 010, 011, 100, 101, 110, 111]
# - In the first operation we can swap the leftmost bit of the second and fifth elements.
#     - The resulting array is [001, 110, 011, 100, 001, 110, 111].
# - In the second operation we can swap the middle bit of the third and fourth elements.
#     - The resulting array is [001, 110, 001, 110, 001, 110, 111].
# The array product is 1 * 6 * 1 * 6 * 1 * 6 * 7 = 1512, which is the minimum possible product.

# Solution
# how many 1 * max_num pairs can you produce
# turns out it is max_num // 2 - 1 number of pairs
# custom power functions improves the power function to log n and
# uses the mod the prevent integer overflow
# Runtime is O(log n)

def my_pow(n: int, e: int) -> int:
    if e == 0:
        return 1
    MOD = 10 ** 9 + 7
    temp = my_pow(n, e // 2)
    temp = temp % MOD
    if e % 2 == 0:
        return (temp * temp) % MOD
    return (((temp * temp) % MOD) * (n % MOD)) % MOD


def minNonZeroProduct(p: int) -> int:
    max_num = 2 ** p - 1
    MOD = 10 ** 9 + 7
    power = my_pow(max_num - 1, (max_num - 1) // 2)
    power = ((power % MOD) * (max_num % MOD)) % MOD
    return power


print(minNonZeroProduct(5))
