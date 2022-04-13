import globalmodule as Global

def isAllFilled(parameter) :
    if (Global.length(parameter) == 0 ) :
        return False
    else :
        return True

def TambahGame() :
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

    arrayGame = [" " for i in range (5)]
    for i in range (1) :
        for j in range(1) :
            arrayGame = [inputGame, inputKategori, inputTahunRilis, inputHarga, inputStok]
    return arrayGame

# YANG KURANG : BELUM ADA GAME ID NYA
print(TambahGame())


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