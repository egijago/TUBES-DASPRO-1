import module as module


def isAllFilled(parameter) :
    # Fungsi isAllFilled
    # Mengecek apakah pengguna memasukkan input yang diminta atau tidak
    
    # ALGORITMA
    if (module.length(parameter) == 0 ) :
        return False
    else :
        return True

def gameId(idGame) :
    # Fungsi gameId
    # Memberi nomor pada game sesuai dengan yang belum terisi pada CSV
    # Input   :  idGame : int
    
    # ALGORITMA
    if (idGame // 10 == 0) :
        return ("GAME00" + str(idGame))
    if (1 <= idGame // 10 <= 9) :
        return ("GAME0" + str(idGame))
    if (10 <= idGame // 10) :
        return ("GAME" + str(idGame))

def TambahGame(gameDs) :
    # Fungsi TambahGame
    # Menambahkan game yang diinput oleh user untuk ditambahkan ke dalam CSV
    # Input : gameDs : array of array of str (Data dari file "game.csv" )
    
    # KAMUS LOKAL 
    # inputGame       : str
    # inputKategori   : str
    # inputTahunRilis : str
    # inputHarga      : str
    # inputStok       : str
    # array Game      : array of int
    
    # ALGORITMA
    data_game = gameDs
    inputGame = str(input("Masukkan nama game : "))
    inputKategori = str(input("Masukkan kategori : "))
    inputTahunRilis = str(input("Masukkan tahun rilis : "))
    inputHarga = str(input("Masukkan harga : "))
    inputStok = str(input("Masukkan stok awal : "))
   
    while (isAllFilled(inputGame) == False) or (isAllFilled(inputKategori) == False) or (isAllFilled(inputTahunRilis) == False) or ((isAllFilled(inputHarga) == False)) or (isAllFilled(inputStok) == False) :
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        inputGame = str(input("Masukkan nama game : "))
        inputKategori = str(input("Masukkan kategori : "))
        inputTahunRilis = str(input("Masukkan tahun rilis : "))
        inputHarga = str(input("Masukkan harga : "))
        inputStok = str(input("Masukkan stok awal : "))

    print("Selamat! Berhasil menambahkan game", inputGame)

    idGame = module.length(data_game)
    idGame = gameId(idGame)

    arrayGame = [" " for i in range (5)]
    for i in range (1) :
        for j in range(1) :
            arrayGame = [idGame, inputGame, inputKategori, inputTahunRilis, inputHarga, inputStok]
    
    # Menambahkan array baru
    data_game += [arrayGame]
    return gameDs
