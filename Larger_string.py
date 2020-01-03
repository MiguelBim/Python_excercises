
def larger_than(a, b):

    flag = None

    if len(a) > len(b):
        flag = True
    elif len(a) < len(b):
        flag = False
    elif len(a) == len(b):
        for i in range(len(a)):
            if a[i] > b[i]:
                flag = True
                break
            elif a[i] < b[i]:
                flag = False
                break
            else:
                flag = False

    return flag

print(larger_than( "111", "111" ))
