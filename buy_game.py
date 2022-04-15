# Spesifikasi Program F08 - Membeli Game
import module
from datetime import date

def buy_game(store_mtrx, ownership_mtrx, user_mtrx, history_mtrx, user_id):
    # Prosedur jika user ingin membeli game
    # Input : store_mtrx        : array of array of str
    #         ownership_mtrx    : array of array of str
    #         user_mtrx         : array of array of str
    #         history_mtrx      : array of array of str
    #         user_id           : str

    # KAMUS LOKAL
    # game_bought                                 : str
    # current_year                                : str
    # found                                       : bool
    # ownership_idx, games_idx, users_idx         : int
    # store_length, ownership_length, user_length : int
    # chosen_game_idx, chosen_user_idx            : int


    # ALGORITMA
    game_bought = input('Masukkan ID Game: ')   # ID Game yang dibeli
    current_year = str(date.today().year)
    
    found = False
    ownership_idx = 0
    store_length = module.length(store_mtrx)
    ownership_length = module.length(ownership_mtrx)
    user_length = module.length(user_mtrx)

    for games_idx in range(store_length):
        if store_mtrx[games_idx][0] == game_bought:
            chosen_game_idx = games_idx
            games_idx = store_length
    
    while not found and ownership_idx < ownership_length:
        if ownership_mtrx[ownership_idx][0] == game_bought and ownership_mtrx[ownership_idx][1] == user_id:
            found = True
        ownership_idx += 1

    for users_idx in range(user_length):
        if user_mtrx[users_idx][0] == user_id:
            chosen_user_idx = users_idx
            users_idx = user_length

    if store_mtrx[chosen_game_idx][5] == 0:
        print('Stok game tersebut sedang habis!')
    else:
        if found:
            print('Anda sudah memiliki Game tersebut')
        else:
            if store_mtrx[chosen_game_idx][4] <= user_mtrx[chosen_user_idx][5]:
                print(f'Game \"{store_mtrx[chosen_game_idx][1]}\" berhasil dibeli!')
                ownership_mtrx += [store_mtrx[chosen_game_idx][0],user_mtrx[chosen_user_idx][0]]
                history_mtrx += [store_mtrx[chosen_game_idx][0],store_mtrx[chosen_game_idx][1],store_mtrx[chosen_game_idx][4],user_mtrx[chosen_user_idx][0],current_year]
            else:
                print('Saldo anda tidak cukup untuk membeli Game tersebut')