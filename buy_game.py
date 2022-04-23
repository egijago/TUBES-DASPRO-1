# Spesifikasi Program F08 - Membeli Game
import module
from datetime import date

def buy_game(store_mtrx, ownership_mtrx, user_mtrx, history_mtrx, user_id):
    # Prosedur jika user ingin membeli game
    # Input : store_mtrx        : array of array of str     ( Data dari file "game.csv" )
    #         ownership_mtrx    : array of array of str     ( Data dari file "kepemilikan.csv" )
    #         user_mtrx         : array of array of str     ( Data dari file "user.csv" )
    #         history_mtrx      : array of array of str     ( Data dari file "riwayat.csv" )
    #         user_id           : str

    # KAMUS LOKAL
    # game_bought                                 : str
    # current_year                                : str
    # found                                       : bool
    # ownership_idx, games_idx, users_idx         : int
    # store_length, ownership_length, user_length : int
    # chosen_game_idx, chosen_user_idx            : int

    # ALGORITMA
    current_year = str(date.today().year)
    game_in_store = False

    game_bought = input('Masukkan ID Game: ')   # ID Game yang dibeli
    
    for games in store_mtrx:
        if games[0] == game_bought:
            print()
            game_in_store = True
            break
    if game_in_store:
        found = False
        ownership_idx = 0
        store_length = module.length(store_mtrx)
        ownership_length = module.length(ownership_mtrx)
        user_length = module.length(user_mtrx)

        # Searching for specified games index in the store_mtrx
        for games_idx in range(store_length):
            if store_mtrx[games_idx][0] == game_bought:
                chosen_game_idx = games_idx
                break    # Terminate loop
        
        # Searching if user already have the game or not
        while not found and ownership_idx < ownership_length:
            if ownership_mtrx[ownership_idx][0] == game_bought and ownership_mtrx[ownership_idx][1] == user_id:
                found = True
            ownership_idx += 1

        # Searching for specified user index in the user_mtrx
        for users_idx in range(user_length):
            if user_mtrx[users_idx][0] == user_id:
                chosen_user_idx = users_idx
                break

        if found:
            print('Anda sudah memiliki Game tersebut')
        else:
            if int(store_mtrx[chosen_game_idx][5]) == 0:
                print('Stok game tersebut sedang habis!')
            else:
                if int(store_mtrx[chosen_game_idx][4]) <= int(user_mtrx[chosen_user_idx][5]):
                    print(f'Game \"{store_mtrx[chosen_game_idx][1]}\" berhasil dibeli!')

                    ownership_mtrx += [store_mtrx[chosen_game_idx][0],user_mtrx[chosen_user_idx][0]]
                    history_mtrx += [[store_mtrx[chosen_game_idx][0],store_mtrx[chosen_game_idx][1],store_mtrx[chosen_game_idx][4],user_mtrx[chosen_user_idx][0],current_year]]
                    store_mtrx[chosen_game_idx][5] = str(int(store_mtrx[chosen_game_idx][5]) - 1)
                    user_mtrx[chosen_user_idx][5] = str(int(user_mtrx[chosen_user_idx][5]) - int(store_mtrx[chosen_game_idx][4]))
                else:
                    print('Saldo anda tidak cukup untuk membeli Game tersebut')

    else:
        print('ID Game yang dimasukkan salah (tidak ada di toko). Ketik \"list_game_toko\" untuk melihat game yang ada.\n')

    return (user_mtrx,ownership_mtrx,history_mtrx)