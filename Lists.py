

#SECOND LARGEST
def second_largest(values_list):

    if len(values_list) > 1:
        largest_value = values_list[0]
        second_largest = values_list[0]

        for i in range(len(values_list)):

            if values_list[i] > largest_value:
                if largest_value >= second_largest:
                    second_largest = largest_value
                largest_value = values_list[i]

    else:
        second_largest = None

    return second_largest

list = [1,3,4,5,0,2]
# list = [-2,-2]
l_val = second_largest(list)
print(l_val)


