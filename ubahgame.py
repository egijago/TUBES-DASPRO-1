# F05 - Ubah Game

import module as module

def changeGame(gameDs) :
    # Fungsi changeGame 
    # Mengubah game pada data
    # Input : gameDs : array of array of str ( Data dari file "game.csv" )
    
    # KAMUS LOKAL
    # gameId           : str
    # inputGame        : str
    # inputKategori    : str
    # inputTahunRilis  : int
    # inputHarga       : int

    # ALGORITMA
    data_game = gameDs
    
    gameId = input("Masukkan ID game : ")
    inputGame = input("Masukkan nama game : ")
    inputKategori = input("Masukkan kategori : ")
    inputTahunRilis = input("Masukkan tahun rilis : ")
    inputHarga = input("Masukkan harga : ")

    while (isIdValid(gameId,data_game) == False) or module.length(gameId) == 0 :
        # Apabila tidak memasukkan ID dari game yang ingin diubah
        if module.length(gameId) == 0 :
            print("Mohon masukkan ID game untuk mengubah game")
            gameId = input("Masukkan ID game : ")
            inputGame = input("Masukkan nama game : ")
            inputKategori = input("Masukkan kategori : ")
            inputTahunRilis = input("Masukkan tahun rilis : ")
            inputHarga = input("Masukkan harga : ")
        # Apabila ID game yang diinput tidak valid (tidak terdapat pada file)
        elif (isIdValid(gameId,data_game) == False)  :
            print("Tidak ada game dengan ID tersebut")
            gameId = input("Masukkan ID game : ")
            inputGame = input("Masukkan nama game : ")
            inputKategori = input("Masukkan kategori : ")
            inputTahunRilis = input("Masukkan tahun rilis : ")
            inputHarga = input("Masukkan harga : ")
            
    # Mengubah data game
    for i in range (module.length(data_game)) :
        for j in range (1) :
            if data_game[i][j] == gameId :
                if module.length(inputGame) != 0:
                    data_game[i][j+1] = inputGame
                if module.length(inputKategori) != 0:
                    data_game[i][j+2] = inputKategori
                if module.length(inputTahunRilis) != 0:
                    data_game[i][j+3] = inputTahunRilis
                if module.length(inputHarga) != 0 :
                    data_game[i][j+4] = inputHarga
    print("Game telah berhasil diubah")
    return data_game

def isIdValid(gameId,data_game) :
    # Fungsi isIdValid
    # Mengecek apakah ID game yang diinput valid atau tidak
    # Input : gameId    : int
    #         data_game : array of array in int ( Data dari file "game.csv" )
    
    # KAMUS LOKAL
    # sameid : int
    
    # ALGORITMA
    sameid = 0
    
    # Mengecek kemunculan ID dalam data
    for i in range (module.length(data_game)): 
        for j in range (1) : 
            if data_game [i][j] == gameId : 
                sameid += 1
            else :
                pass 
    
    if sameid != 0 :
        return True
    else :
        return False

