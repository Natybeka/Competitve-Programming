# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# Problem given path with steps U and D and count the number of valleys
# The hiker went through

# Solution count the valley as the hiker reaches sea level
def countingValleys(steps, path):
    # Write your code here
    height = 0
    valley_count = 0
    for step in path:
        if step == 'U':
            height += 1
            if height == 0:
                valley_count += 1
            
        else:
            height -= 1
    return valley_count