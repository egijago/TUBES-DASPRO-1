# Spesifikasi Program F07 - Listing Game di Toko Berdasarkan ID, Tahun Rilis dan Harga
import module
store_data = [['GAME008','AC Unity','Adventure','2014','430000','0'],
            ['GAME009','Elder Ring','Adventure','2022','861000','1'],
            ['GAME008','GoW: Ragnarok','Adventure','2021','1000000','5']]
def list_game_toko(store_mtrx):
    # Prosedur untuk list game di toko berdasarkan ID atau Tahun Rilis atau Harga
    # Input: store_mtrx       : array of array of str       ( Data dari file "game.csv" )

    # KAMUS LOKAL
    # scheme  : str

    # ALGORITMA
    scheme = str(input('Skema sorting: '))

    if scheme == '':
        module.matrix_print(store_mtrx, [0,1,2,3,4,5])
    elif scheme == 'harga+':
        module.matrix_print(module.ascend_sort(store_mtrx,4), [0,1,2,3,4,5])
    elif scheme == 'harga-':
        module.matrix_print(module.descend_sort(store_mtrx,4), [0,1,2,3,4,5])
    elif scheme == 'tahun+':
        module.matrix_print(module.ascend_sort(store_mtrx,3), [0,1,2,3,4,5])
    elif scheme == 'tahun-':
        module.matrix_print(module.descend_sort(store_mtrx,3), [0,1,2,3,4,5])
    else:
        print('Skema sorting tidak valid')
list_game_toko(store_data)