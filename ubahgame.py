import module as module
# data_game = [['id', 'nama', 'kategori', 'tahun rilis', 'harga', 'stok'], 
#              ['G001', 'BNMO', 'Adventure', '2013', '120000', '2'], 
#              ['G002', 'Barbie', 'Romance', '2020', '180000', '2']]

def changeGame(gameDs) :
    data_game = gameDs
    # global data_game
    gameId = input("Masukkan ID game : ")
    inputGame = input("Masukkan nama game : ")
    inputKategori = input("Masukkan kategori : ")
    inputTahunRilis = input("Masukkan tahun rilis : ")
    inputHarga = input("Masukkan harga : ")

    while (isIdValid(gameId) == False) or module.length(gameId) == 0 :
        if (isIdValid(gameId) == False)  :
            print("Tidak ada game dengan ID tersebut")
            gameId = input("Masukkan ID game : ")
            inputGame = input("Masukkan nama game : ")
            inputKategori = input("Masukkan kategori : ")
            inputTahunRilis = input("Masukkan tahun rilis : ")
            inputHarga = input("Masukkan harga : ")
        if module.length(gameId) == 0 :
            print("Mohon masukkan ID game untuk mengubah game")
            gameId = input("Masukkan ID game : ")
            inputGame = input("Masukkan nama game : ")
            inputKategori = input("Masukkan kategori : ")
            inputTahunRilis = input("Masukkan tahun rilis : ")
            inputHarga = input("Masukkan harga : ")


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

def isIdValid(gameId) :
    sameid = 0
    
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

if __name__ == "__main__":
    changeGame()
