
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

