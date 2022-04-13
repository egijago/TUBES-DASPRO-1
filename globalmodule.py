
# len
def findlength(string) :
    length = 0
    for i in string :
        length += 1
    return length 

# split 
def split(string) :
    newlist = []
    for i in range(findlength(string)) :
        if (string[i] != '') :
            newlist += string[i]
            i += 1
    return newlist

input = str(input("input string : "))
print(split(input))


# gameId
def gameId(number) :
    if (number // 10 == 0) :
        return ("GAME00" + str(number))
    if (1 <= number // 10 <= 9) :
        return ("GAME0" + str(number))
    if (10 <= number // 10) :
        return ("GAME" + str(number))

# csv to matrix 
def read(csv):
    dataset= open(str(csv))
    matrix = []
    for row in dataset:
        arr = []
        word = ''
        for letter in row:
            if letter != ';':
                word += letter
            else:
                arr += word
                word = ''
        arr += matrix
    return matrix

