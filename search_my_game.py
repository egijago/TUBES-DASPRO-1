from module import *

def search_my_game(userArr, kepemilikanDs, gameDs):
    # Prosedur search_my_game
    # Mencari data game yang ada pada library user
    # Input : userArr           : array of str              ( Data user yung sedang login )
    #         kepemilikanDs     : array of array of str     ( Data dari file "kepemilikan.csv" )
    #         gameDs            : array of array of str     ( Data dari file "game.csv" )

    # KAMUS LOKAL 
    # userId              : str             (id user yang sedang login)
    # gameId, gameRls     : str            
    # isNullId, isNullRls : Bool            
    # owned               : array of str    

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
        if user_id == userId: owned += [game_id]

    # Menampilkan game yang dimiliki yang sesuai dengan kriteria
    isNothingPrinted = True
    index = 1
    for game_id in owned: 
        for [id,nama,kategori,tahun_rilis,harga,stok] in gameDs:
            if game_id == id: 
                if isNullId : gameId = id
                if isNullRls : gameRls = tahun_rilis
                if gameId == id and gameRls == tahun_rilis:
                    isNothingPrinted = False
                    print(f"{uni(str(index),3)}. {id} | {uni(nama,25)} | {uni(harga,8)} | {uni(kategori,8)} | {uni(tahun_rilis,4)}")
                    index +=1
    if isNothingPrinted :
        if length(owned) > 0 : 
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
        else:
            print("Anda tidak memiliki game apapun di inventory. ")
    
if __name__ == "__main__":
    search_my_game()
