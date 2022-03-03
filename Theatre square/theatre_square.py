# Problem description
# m x n city square paved with n a x a flagstones, then find the least amount
# of n to cover the square. Constraints sides of the flagstone squares must be parallel
# with sides of the square.
import math
inputs = input().split()
n = int(inputs[0])
m = int(inputs[1])
a = int(inputs[2])
print(math.ceil(n / a) * math.ceil(m / a))