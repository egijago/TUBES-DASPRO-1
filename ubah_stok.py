# Spesifikasi Program F06 - Mengubah Stok Game di Toko
import module

def ubah_stok(game_stocks):
    # Fungsi untuk mengubah stok game
    # Input : game_stocks (array of array of str)
    # Output: matrix game_stocks yang sudah diubah
    game_id = str(input('Masukkan ID game: '))
    amount = int(input('Masukkan jumlah'))

    found = False
    num_of_games = module.length(game_stocks)
    idx = 0

    while not found and idx < num_of_games:
        if game_stocks[1] == game_id:
            name = game_stocks[1]
            curr_amount = int(game_stocks[5]) - amount
            found = True
    
    if found:
        if curr_amount >= 0:
            print(f'Stok game {name} berhasil dikurangi. Stok sekarang: {curr_amount}')
        else:
            print(f'Stok game {name} gagal dikurangi karena stok kurang. Stok sekarang: {game_stocks[5]} (<{amount})')
    else:
        print('\n Tidak ada game dengan ID tersebut')

    return game_stocks