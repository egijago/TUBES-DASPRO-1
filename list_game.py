# Spesifikasi Program F09 - Melihat Game yang dimiliki
import module

def list_game(store_mtrx, ownership_mtrx, user_id):
    # Prosedur untuku list game yang dimiliki user dan fungsi yang mengembalikan game-game yang dimiliki user
    # Input : store_mtrx            : array of array of str
    #         ownership_mtrx        : array of array of str
    #         user_id               : str
    # Output: bought_game_by_user   : array of array of stsr
    
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

    if user_game_id == []:
        print('Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.')
    else:    
        bought_game_by_user = [['' for i in range(5)]]
        for store_idx in user_game_id:
            bought_game_by_user += [store_mtrx[store_idx][0],store_mtrx[store_idx][1],store_mtrx[store_idx][2],store_mtrx[store_idx][3],store_mtrx[store_idx][4]]
        print('Daftar game:')
        module.matrix_print(bought_game_by_user, [0,1,2,3,4])
    
    return bought_game_by_user