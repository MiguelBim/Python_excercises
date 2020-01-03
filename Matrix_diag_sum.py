

def diagonal_sum(given_2d):

    sum = 0

    for i in range(len(given_2d)):
        for j in range(len(given_2d[i])):
            if i == j:
                sum += given_2d[i][j]

    return sum


array = [[1,2,3],[4,5,6],[7,8,9]]
diag_sum = diagonal_sum(array)
print(diag_sum)