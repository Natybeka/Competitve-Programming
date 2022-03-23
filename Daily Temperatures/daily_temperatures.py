# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Solution use monotonic stack to find the next day
# With the greater temperature and keep track of the day in the stack as well
# Space n2
# Time n (nested loop but each element is only popped once so at most n pops)
from typing import List


# def dailyTemperatures(temperatures: List[int]) -> List[int]:
#     monoStack = [0]
#     greaterTemp = [0] * len(temperatures)

#     for count, temperature in enumerate(temperatures[1:], start=1):
#         while monoStack and temperature > temperatures[monoStack[-1]]:
#             previousDay = monoStack.pop()
#             greaterTemp[previousDay] = count - previousDay
#         monoStack.append(count)
#     return greaterTemp


# Second solution
# Iterate from the end of the list back
# if the next day is doesn't have the highest temp check answer[day + current_day]th
# element
# space o(1)
# time n(linear)
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answer = [0] * n
    maximumTemp = 0
    for current in range(n - 1, -1, -1):
        if temperatures[current] >= maximumTemp:
            maximumTemp = temperatures[current]
            continue
        days = 1
        while temperatures[current + days] <= temperatures[current]:
            days += answer[current + days]

        answer[current] = days
    return answer


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
