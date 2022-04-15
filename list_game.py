# Spesifikasi Program F09 - Melihat Game yang dimiliki
import module

def games_user_bought(store_mtrx, ownership_mtrx, user_id):
    # Fungsi yang mengembalikan game-game yang dimiliki user
    # Input : store_mtrx            : array of array of str     ( Data dari file "game.csv" )
    #         ownership_mtrx        : array of array of str     ( Data dari file "kepemilikan.csv" )
    #         user_id               : str
    # Output: bought_game_by_user   : array of array of str
    
    # KAMUS LOKAL
    # store_length          : int                       ( Pangjan matriks store )
    # user_game_id          : array of int              ( Menyimpan idx games yang dimiliki user di store )
    # games                 : str                       ( Untuk pengulangan )
    # store_idx             : int                       ( Untuk pengulangan )

    # ALGORITMA
    store_length = module.length(store_mtrx)
    user_game_id = []

    for games in ownership_mtrx:
        if games[1] == user_id:
            for store_idx in range(store_length):
                if store_mtrx[store_idx][0] == games[0]:
                    user_game_id += [store_idx]
                    store_idx = store_length
  
    bought_game_by_user = [['' for i in range(5)]]
    for store_idx in user_game_id:
        bought_game_by_user += [store_mtrx[store_idx][0],store_mtrx[store_idx][1],store_mtrx[store_idx][2],store_mtrx[store_idx][3],store_mtrx[store_idx][4]]
    
    return bought_game_by_user

def list_game(store_mtrx, ownership_mtrx, user_id):
    # Prosedur untuku list game yang dimiliki user
    # Input : store_mtrx            : array of array of str
    #         ownership_mtrx        : array of array of str
    #         user_id               : str

    # KAMUS LOKAL
    # bought_game           : array of array of str     ( Matriks untuk menyimpan data-data game yang pernah dibeli user )
    # buoght_game_length    : int                       ( Panjang matriks bought_game )

    # ALGORITMA
    bought_game = games_user_bought(store_mtrx, ownership_mtrx, user_id)
    bought_game_length = module.length(bought_game)

    if bought_game_length == 1:
        print('Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.')
    else:    
        print('Daftar game:')
        module.matrix_print(bought_game, [0,1,2,3,4])