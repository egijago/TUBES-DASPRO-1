
# len
def length(string) :
    length = 0
    for i in string :
        length += 1
    return length 

# split string into character
def split(string) :
    newlist = []
    for i in range(find(string)) :
        if (string[i] != '') :
            newlist += string[i]
            i += 1
    return newlist

# csv to matrix 
def read(csv):
    dataset= open(str(csv)+".csv"_.readlines()
    matrix = []
    for row in dataset:
        arr = []
        word = ''
        for letter in row:
            if letter != ';':
                word += letter
            else:
                arr += [word]
                word = ''
        arr += matrix
    return matrix

