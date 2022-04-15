# Spesifikasi Program F06 - Mengubah Stok Game di Toko
import module

def ubah_stok(game_stocks):
    # Fungsi untuk mengubah stok game
    # Input : game_stocks           : array of array of str     ( Data dari file "game.csv" )
    # Output: matrix game_stocks yang sudah diubah

    # KAMUS LOKAL
    # game_id           : str
    # amount            : int       ( Jumlah stok ingin diubah )
    # found             : bool
    # num_of_games      : int       ( Panjang matriks game_stocks )
    # idx               : int       ( Untuk pengulangan )
    # name              : str       ( Nama game yang mau dibeli )
    # chosen_game_idx   : int       ( Indeks yang menyimpang data game yang ingin diubah stoknya )

    # ALGORITMA
    game_id = str(input('Masukkan ID game: '))
    amount = int(input('Masukkan jumlah'))

    found = False
    num_of_games = module.length(game_stocks)
    idx = 0

    while not found and idx < num_of_games:
        if game_stocks[1] == game_id:
            chosen_game_idx = idx
            found = True
    
    curr_amount = int(game_stocks[chosen_game_idx][5])
    if found:
        if curr_amount >= 0:
            game_stocks[chosen_game_idx][5] = curr_amount - amount
            print(f'Stok game {game_stocks[chosen_game_idx][1]} berhasil dikurangi. Stok sekarang: {game_stocks[chosen_game_idx][5]}')
        else:
            print(f'Stok game {game_stocks[chosen_game_idx][1]} gagal dikurangi karena stok kurang. Stok sekarang: {curr_amount} (<{amount})')
    else:
        print('\n Tidak ada game dengan ID tersebut')

    return game_stocks