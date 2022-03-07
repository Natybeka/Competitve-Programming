# Problem description
# There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

# In each step, you will choose any 3 piles of coins (not necessarily consecutive).
# Of your choice, Alice will pick the pile with the maximum number of coins.
# You will pick the next pile with the maximum number of coins.
# Your friend Bob will pick the last pile.
# Repeat until there are no more piles of coins.
# Given an array of integers piles where piles[i] is the number of coins in the ith pile.

# Return the maximum number of coins that you can have.
def maxCoins(piles):
    piles.sort()
    sumPile = 0
    index = len(piles) - 2
    while index >= len(piles) // 3:
        sumPile += piles[index]
        index -= 2
    return sumPile

# Shorthand for the code above
# return sum(sorted(piles)[len(piles) // 3 :: 2])

print(maxCoins([2,4,1,2,7,8]))