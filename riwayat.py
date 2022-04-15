# Spesifikasi Program F13 - Melihat Riwayat Pembelian
import module
import list_game

def riwayat(store_mtrx, ownership_mtrx, user_id, history_mtrx):
    # Prosedur untuk print riwayat pemebelian user
    # Input : store_mtrx            : array of array of str     ( Data dari file "game.csv" )
    #         ownership_mtrx        : array of array of str     ( Data dari file "kepemilikan.csv" )
    #         user_id               : str
    #         history_mtrx          : array of array of str     ( Data dari file " riwayat.csv" )

    # KAMUS LOKAL
    # bought_games      : array of array of str         ( variabel menyimpan data game yang pernah dibeli user )
    # user_buy_history  : array of array of str         ( Variabel menyimpan riwayat pembelian game yang dimiliki user )

    # ALGORITMA
    bought_games = list_game.games_user_buoght(store_mtrx, ownership_mtrx, user_id)

    user_buy_history = [['' for i in range(4)]]
    for games in bought_games:
        for histories in history_mtrx:
            if games[0] == histories[0]:
                user_buy_history += [histories[0],histories[1],histories[2], histories[4]]
    
    if user_buy_history == [['', '', '', '']]:
        print('Maaf, kamu tidaka da riwayat pembelian game. Ketik perintah beli_game untuk membeli.')
    else:
        print('Daftar game:')
        module.matrix_print(user_buy_history,[0,1,2,3])