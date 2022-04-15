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
    return 

def ascend_sort(my_mtrx,data_idx):
    # Fungsi untuk sort matrix ascending berdasarkan value di indeks data_idx elemen matriks tersebut
    # Input: my_mtrx    : array of array of string
    #        data_idx   : integer                       (indeks dari array elemen my_mtrx yang menjadi basis sorting)
    # Output: temp_mtrx : array of array of string      (my_mtrx yang sudah di sort)

    # KAMUS LOKAL
    # mtrx_length, check  : int
    # any_swap            : bool
    
    # ALGORITMA
    mtrx_length = length(my_mtrx)
    temp_mtrx = my_mtrx
    if mtrx_length > 1:
        check = 1
        any_swap = True

        while check <= mtrx_length - 1 and any_swap:
            any_swap = False
            for idx in range(mtrx_length, check, -1):
                if temp_mtrx[idx][data_idx] < temp_mtrx[idx - 1][data_idx]:
                    temp_value = temp_mtrx[idx][data_idx]
                    temp_mtrx[idx][data_idx] = temp_mtrx[idx - 1][data_idx]
                    temp_mtrx[idx - 1][data_idx] = temp_value
                    any_swap = True

                elif temp_mtrx[idx][data_idx] < temp_mtrx[idx - 1][data_idx]:
                    idx += 1
            check += 1
    return temp_mtrx

def descend_sort(my_mtrx,data_idx):
    # Fungsi untuk sort matrix descending berdasarkan value di indeks data_idx elemen matriks tersebut
    # Input: my_mtrx    : array of array of string
    #        data_idx   : integer                       (indeks dari array elemen my_mtrx yang menjadi basis sorting)
    # Output: temp_mtrx : array of array of string      (my_mtrx yang sudah di sort)

    # KAMUS LOKAL
    # mtrx_length, check  : int
    # any_swap            : bool

    # ALGORITMA
    mtrx_length = length(my_mtrx)
    temp_mtrx = my_mtrx
    if mtrx_length > 1:
        check = 1
        any_swap = True

        while check <= mtrx_length - 1 and any_swap:
            any_swap = False
            for idx in range(mtrx_length, check, -1):
                if temp_mtrx[idx][data_idx] > temp_mtrx[idx - 1][data_idx]:
                    temp_value = temp_mtrx[idx][data_idx]
                    temp_mtrx[idx][data_idx] = temp_mtrx[idx - 1][data_idx]
                    temp_mtrx[idx - 1][data_idx] = temp_value
                    any_swap = True

                elif temp_mtrx[idx][data_idx] < temp_mtrx[idx - 1][data_idx]:
                    idx += 1
            check += 1
    return temp_mtrx

# def matrix_print(my_mtrx):
#     # Fungsi untuk print matrix menjadi suatu tabel
#     # Input: my_mtrx    : array of array of string
#     # Output: String    (Bentuk tabel)

#     # KAMUS LOKAL
#     #

#     # ALGORITMA
