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

def max_length(my_mtrx, header_idx):
    # Fungsi untuk mencari jumlah karakter dari string  terpanjang di elemen matrix my_mtrx
    # Input : my_mtrx       : array of array of str
    #         header_idx    : int                       (indeks dari bagian elemen yang ingin dicari)
    # Output: length_bound  : int

    # KAMUS LOKAL
    # elements  : array of string

    # ALGORITMA
    length_bound = 0
    for elements in my_mtrx:
        if elements[header_idx] > length_bound:
            length_bound = length(elements[header_idx])
    return length_bound

def matrix_print(my_mtrx, header_list):
    # Fungsi untuk print matrix menjadi suatu tabel
    # Input: my_mtrx    : array of array of str
    #        header_list: array of int              (List yang menyimpan indeks elemen my_mtrx untuk di print)
    # Output: String    (Bentuk tabel)

    # KAMUS LOKAL
    # elements_idx                                : array of str
    # game_name_char, category_char, price_char   : str
    # mtrx_length                                 : int
    # space_game_name, space_category, space_price: str
    # i, idx                                      : int   (untuk pengulangan)

    # ALGORITMA
    game_name_char = max_length(my_mtrx, 1) # Maksimum karakter untuk nama game
    category_char = max_length(my_mtrx, 2)  # Maksumum karakter untuk kategori
    price_char = max_length(my_mtrx, 4) # Maksimum karakter untuk harga
    mtrx_length = length(my_mtrx)

    for elements_idx in range(mtrx_length):
        space_game_name = ''
        space_category = ''
        space_price = ''

        for i in range(game_name_char - length(my_mtrx[elements_idx][1])):
            space_game_name += ' '
        for i in range(category_char - length(my_mtrx[elements_idx][2])):
            space_category += ' '
        for i in range(price_char - length(my_mtrx[elements_idx][4])):
            space_price += ' '

        print(f'{elements_idx + 1}. {my_mtrx[elements_idx][header_list[0]]} ', end='')
        for idx in header_list:
            if idx > 0:
                print(f'| {my_mtrx[elements_idx][idx]}', end='')
                if idx == 1:
                    print(space_game_name, end=' ')
                elif idx == 2:
                    print(space_category, end=' ')
                elif idx == 4:
                    print(space_price, end=' ')