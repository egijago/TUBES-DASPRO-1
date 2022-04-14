
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
def read(file):
    # Fungsi read(csv)
    # Menginisialisasikan matrix dari file.csv

    # KAMUS LOKAL
    # dataset :  array of str
    # matrix : array of array of str
    # arr : array of str
    # word : str
    # leter : char

    # ALGORITMA
    dataset= open(str(file)+".csv").readlines()
    matrix = []
    for row in dataset:
        arr = []
        word = ''
        for letter in row:
            if letter != '"':
                if letter != ';':
                    word += letter
                else:
                    arr += [word]
                    word = ''
        matrix += [arr]
    return matrix

