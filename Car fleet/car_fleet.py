from typing import List
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    sortedPos = sorted(zip(position, speed))
    monoStack = []
    for position, speed in sortedPos[::-1]:
        distance = target - position
        if not monoStack:
            monoStack.append(distance / speed)
            continue
        if distance / speed > monoStack[-1]:
            monoStack.append(distance / speed)
    return len(monoStack)

print(carFleet(10, [6, 8], [3, 2]))

        
