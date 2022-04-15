from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    n = len(matrix)
    m = len(matrix[0])
    #         Boundaries of the spiral
    #  with each iteration move inward row + 1 and column - 1

    rowBegin = 0
    colBegin = 0
    rowEnd = len(matrix)
    colEnd = len(matrix[0])

    output = []
    while rowBegin < rowEnd and colBegin < colEnd:
        for i in range(colBegin, colEnd):
            output.append(matrix[rowBegin][i])
        rowBegin += 1
        for j in range(rowBegin, rowEnd):
            print(j)
            output.append(matrix[j][colEnd - 1])
        colEnd -= 1
        if rowEnd > rowBegin:
            for k in range(colEnd - 1, colBegin - 1, -1):
                output.append(matrix[rowEnd - 1][k])
            rowEnd -= 1
        if colEnd > colBegin:
            for l in range(rowEnd - 1, rowBegin - 1, -1):
                output.append(matrix[l][colBegin])
            colBegin += 1

    print(rowBegin, rowEnd, colBegin, colEnd)
    return output
