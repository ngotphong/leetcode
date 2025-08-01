def generate(numRows):
    result = []
    for row in range(numRows):
        result.append([1] * (row + 1))
        for i in range(1, row):
            result[row][i] = result[row - 1][i - 1] + result[row - 1][i]
    return result

print(generate(5))