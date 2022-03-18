from typing import List
from collections import Counter
def leastInterval(self, tasks: List[str], n: int) -> int:
    if n == 0:
        return len(tasks)
    counts = Counter(tasks).values().sort()
    q = []
    time = 0
    while counts or q:
        # Check the pending task queue
        
        
        
    