
#PALINDROME
if __name__ == '__main__':

    #También se puede con strings
    word = ''
    print("The original word is: ", word)
    rev_word = word[::-1]
    print("The word reversed is: ", rev_word)
    # print(len(word)) = 9

    def palindrome(word):

        rev_word = word[::-1]
        flag = True

        for index in range(len(word)):
            if word[index] != rev_word [index]:
                flag = False
                break
        if flag != True:
            print("The word is not a palindrome")
        else:
            print("The word is a palindrome")

    palindrome(word)

    #------------------------------------------------------------------------------------
    #Extra exercise testing
