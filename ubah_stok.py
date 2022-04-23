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

    found = False
    num_of_games = module.length(game_stocks)
    idx = 0
    chosen_game_idx = 0

    # Search for game data in game matrix
    while not found and idx < num_of_games:
        if game_stocks[idx][0] == game_id:
            chosen_game_idx = idx
            found = True
        idx += 1

    curr_amount = int(game_stocks[chosen_game_idx][5])  # Stok game yang ada
    if found:
        amount = int(input('Masukkan jumlah: '))
        if amount >= 0:
            game_stocks[chosen_game_idx][5] = curr_amount + amount
            print(f'Stok game {game_stocks[chosen_game_idx][1]} berhasil ditambah. Stok sekarang: {game_stocks[chosen_game_idx][5]}')
        else:
            if -1*amount <= curr_amount:
                game_stocks[chosen_game_idx][5] = str(curr_amount + amount)
                print(f'Stok game {game_stocks[chosen_game_idx][1]} berhasil dikurangi. Stok sekarang: {game_stocks[chosen_game_idx][5]}')
            else:
                print(f'Stok game {game_stocks[chosen_game_idx][1]} gagal dikurangi karena stok kurang. Stok sekarang: {curr_amount} (< {-1 * amount})')
    else:
        print('\nTidak ada game dengan ID tersebut')

    return game_stocks
