
#Método 1. Gettin the coordenates of each rook
def rooks_are_safe(chessboard):

    rows = []
    columns = []

    for i in range(len(chessboard)):
        for j in range(len(chessboard[i])):
            if chessboard[i][j] == 1:
                rows.append(i)
                columns.append(j)
    print(rows)
    print(columns)

    for value in rows:
        if rows.count(value) > 1:
            return False
        else:
            flag = True

    for value in columns:
        if columns.count(value) > 1:
            return False
        else:
            flag = True


    return flag


#Método 2 (Counting the number of rooks by column and row
def rooks_are_safe_2(chessboard):

    n = len(chessboard)
    print(n) #3

    for row_i in range(n):
        row_count = 0
        for col_i in range(n):
            row_count += chessboard[row_i][col_i]
        if row_count > 1:
            return False

    for col_i in range(n):
        col_count = 0
        for row_i in range(n):
            col_count += chessboard[row_i][col_i]
        if col_count > 1:
            return False

    return True

chessboard = [[0,0,0],[1,0,1],[0,0,0]]
safe = rooks_are_safe_2(chessboard)
print(safe)