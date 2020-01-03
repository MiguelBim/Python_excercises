# Input: A list / array with integers.  For example:
# [3, 4, 1, 2, 9]
# Returns:
#  Nothing. However, this function will print out
#  a pair of numbers that adds up to 10. For example,
#  1, 9.  If no such pair is found, it should print
#  "There is no pair that adds up to 10.".


#SUMA DOS NUMEROS A 10
def pair10_list(given_list):

    dict = {}

    for num in given_list:
        val = 10 - num
        if val in dict:
            print(num, val)
            return
        else:
            dict[num] = 1

    print("There is no pair that adds up to 10.")

    return

def pair10(given_list):

    numbers_seen = {}

    for item in given_list:
        val = 10 - item
        if val in numbers_seen:
           print(val, item)
           return
        else:
            numbers_seen[item] = 1
    print("There is no pair that adds up to 10.")

print("""
Which pair adds up to 10?
[1, 1, 1, 2, 3, 4, 5]
""")
pair10_list([1, 1, 1, 2, 3, 4, 5])
