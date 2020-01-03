
#-------------------------------------------------------
#Ejemplo 1
given_list = [4,7,2]
def total(given_list):
    x = 0
    for item in given_list:
        x += item
    return x

# En este caso se tiene una complejidad lineal, dado que el programa tardará el mismo tiempo para cada valor de entrada
# El tiempo que tarda crece linear (ecuación de la recta)
# Función t = an + b = O(n)
# t -> time
# Big O notation
# O(n) -> Lo que significa que la función crece en orden de n


#-------------------------------------------------------
#Ejemplo 2
given_list = [4,7,2]
def total(given_list):
    x = 0
    return x

#Esta función tardará siempre lo mismo sin importar lo que se le mande, por eso se considera de complejidad constante
# t = c
# O(1) -> La función no crece, es constante


#-------------------------------------------------------
#Ejemplo 3
array_2d = [[4,7],[1,1]]
def total(array_2d):
    x = 0
    for row in array_2d:
        for item in row:
            x += item
    return x

#Esta función al tener 2 for loops, crecerá mas rápido conforme mas elemento tenga la entrada, por lo que:
# t = anˆ2 + c
# O(n^2)


#-------------------------------------------------------
# nO(n)   = n(an + b)
#         = anˆ2 + bn
#         = O(nˆ2)
# Dado que nˆ2 es el término que crece mas rápido, se considera que la función es complejidad cuadrática

#-------------------------------------------------------
# Assigning time complexity to each step

array_2d = [[4,7],[1,1]]
def total(array_2d):
    x = 0                   # O(1)
    for row in array_2d:    # O(n)----|
        for item in row:    # O(n)-----> nO(n)
            x += item       # O(1)----|
    return x                # O(1)



#-------------------------------------------------------
# Using the rooks example

def rooks_are_safe_2(chessboard):

    n = len(chessboard)
    print(n) #3

    for row_i in range(n):                          # O(n)----|
        row_count = 0                                        #--> nO(n) = O(n^2)
        for col_i in range(n):                      # O(n)----|
            row_count += chessboard[row_i][col_i]
        if row_count > 1:                           # O(n) solo si hay mas de una torre en la columna
            return False

    for col_i in range(n):                          # O(n)
        col_count = 0
        for row_i in range(n):                      # O(n)
            col_count += chessboard[row_i][col_i]
        if col_count > 1:                           # O(n)
            return False

    return True

# The time complexity is calculated assumed an average test case (not the best, which in this case would be if no towers are in the same row/column

#-------------------------------------------------------
# Exercise

def count_negatives(given_array):

    num = 0

    for row in given_array:
        for item in row:
            if item < 0:
                num +=1
    return num

array = [[-4, -3, -1, 1],[-2, -2,  1, 2],[-1,  1,  2, 3],[ 1,  2,  4, 5]]
neg_num = count_negatives(array)
print(neg_num)
# Solution O(n^2)


# Solution O(n)

def count_negatives_2(given_array):

    count = 0
    row_i = 0
    col_i = len(given_array[0])-1
    print(col_i)

    while col_i >= 0 and row_i < len(given_array):
        if given_array[row_i][col_i] < 0:
            count += (col_i + 1)
            row_i += 1
        else:
            col_i -= 1
    return  count

array_2 = [[-4, -3, -1, 1],[-2, -2,  1, 2],[-1,  1,  2, 3],[ 1,  2,  4, 5]]
neg_num_2 = count_negatives_2(array_2)
print(neg_num_2)

