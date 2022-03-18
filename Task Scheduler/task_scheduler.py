# Problem description
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.

# Solution process the maximum occuring task first
# maxHeap for accessing the most occuring task first
# and process other tasks in the maxHeap until the
# first processed task is ready to be executed again
import heapq
from typing import List
from collections import Counter


def leastInterval(tasks: List[str], n: int) -> int:
    if n == 0:
        return len(tasks)
    counts = Counter(tasks)
    maxHeap = [-count for count in counts.values()]
    heapq.heapify(maxHeap)

    q = []
    time = 0
    while maxHeap or q:
        time += 1
        if maxHeap:
            count = 1 + heapq.heappop(maxHeap)
            if count:
                q.append([count, time + n])

        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.pop(0)[0])
    return time


print(leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2))
