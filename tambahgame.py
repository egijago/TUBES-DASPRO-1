import module as module

data_game = [['id', 'nama', 'kategori', 'tahun rilis', 'harga', 'stok'], 
             ['G001', 'BNMO', 'Adventure', '2013', '120000', '2'], 
             ['G002', 'Barbie', 'Romance', '2020', '180000', '2']]

def isAllFilled(parameter) :
    if (module.length(parameter) == 0 ) :
        return False
    else :
        return True

def gameId(idGame) :
    if (idGame // 10 == 0) :
        return ("G00" + str(idGame))
    if (1 <= idGame // 10 <= 9) :
        return ("G0" + str(idGame))
    if (10 <= idGame // 10) :
        return ("G" + str(idGame))

def TambahGame() :
    global data_game
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
    
    data_game += arrayGame
    return data_game

TambahGame()
print(data_game)


'''
    if (inputGame == " ") or (inputKategori == " ") or (inputTahunRilis == " ") or (inputHarga == " ") or (inputStok == " ") :
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        TambahGame()
    else :
        print("Selamat! Berhasil menambahkan game", inputGame)
        arrayGame = [" " for i in range (5)]
        for i in range (1) :
            for j in range(1) :
                arrayGame[0] += inputGame
                arrayGame[1] += inputKategori
                arrayGame[2] += inputTahunRilis
                arrayGame[3] += inputHarga
                arrayGame[4] += inputStok
        return arrayGame

print(TambahGame())'''




'''
gamebaru = [inputGame, ',', inputKategori, ',', inputTahunRilis, ',', inputHarga, ',' ,inputStok]
file1 = open('/Users/raisyanabilat/Documents/College Things/DASPRO/TUGAS BESAR/TUGAS BESAR/Program/game.csv', 'w')
file1.writelines(gamebaru)'''