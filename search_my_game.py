from module import *

def search_my_game(userArr, kepemilikanDs, gameDs):
    # Prosedur search_my_game
    # Mencari data game yang ada pada library user

    # KAMUS LOKAL 
    # userId : str
    # gameId, gameRls : str
    # isNullId, isNullRls : Bool
    # owned : array of str

    # ALGORITMA
    # Mengakses user id
    userId = userArr[0]

    # Inisialisasi variable
    gameId = input("Masukkan ID Game: ")
    isNullId = gameId == ""
    gameRls = input("Masukkan Tahun Rilis Game: ")
    isNullRls = gameRls == ""

    # Mencari daftar game yang dimiliki
    owned = []
    for [game_id,user_id] in kepemilikanDs:
        if user_id == userId:
            owned += gameId

    # Menampilkan game yang dimiliki yang sesuai degan kriteria
    for game_id in owned: 
        for [id,nama,kategori,tahun_rilis,harga,stok] in gameDs:
            if game_id == id: 
                if isNullId : gameId == id
                if isNullRls : gameRls == tahun_rilis
                if gameId == id and gameRls == tahun_rilis:
                    print(f"{id} | {uni(nama,25)} | {uni(harga,8)} | {uni(kategori,8)} | {uni(tahun_rilis,4)}")
    
if __name__ == "__main__":
    search_my_game()
