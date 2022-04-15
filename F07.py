# Spesifikasi Program F07 - Listing Game di Toko Berdasarkan ID, Tahun Rilis dan Harga
import module

def list_game(my_mtrx):
    # Prosedur untuk list game di toko berdasarkan ID atau Tahun Rilis atau Harga
    # Input: my_mtrx       : array of array of str

    # KAMUS LOKAL
    # scheme  : str

    # ALGORITMA
    scheme = str(input('Skema sorting: '))

    if scheme == '':
        module.matrix_print(my_mtrx, [0,1,2,3,4,5])
    elif scheme == 'harga+':
        module.matrix_print(module.ascend_sort(my_mtrx,4), [0,1,2,3,4,5])
    elif scheme == 'harga-':
        module.matrix_print(module.descend_sort(my_mtrx,4), [0,1,2,3,4,5])
    elif scheme == 'tahun+':
        module.matrix_print(module.ascend_sort(my_mtrx,3), [0,1,2,3,4,5])
    elif scheme == 'tahun-':
        module.matrix_print(module.ascend_sort(my_mtrx,3), [0,1,2,3,4,5])
    else:
        print('Skema sorting tidak valid')