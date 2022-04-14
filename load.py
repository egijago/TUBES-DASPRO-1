import argparse
import os

def read(file):
    # Fungsi read(csv)
    # Menginisialisasikan matrix dari file.csv

    # KAMUS LOKAL
    # dataset :  array of str
    # matrix : array of array of str
    # arr : array of str
    # word : str
    # leter : char

    # ALGORITMA
    dataset= open(str(file)+".csv").readlines()
    matrix = []
    for row in dataset:
        arr = []
        word = ''
        for letter in row:
            if letter != '"':
                if letter != ';':
                    word += letter
                else:
                    arr += [word]
                    word = ''
        matrix += [arr]
    return matrix

def load():
    # Fungsi Load()
    # Melakukan loading data yang akan digunakan pada aplikasi
    
    # KAMUS LOKAL
    # parser : ArgumentParser
    # dir, path : str

    # ALGORITMA
    global userDs, gameDs, riwayatDs, kepemilikanDs

    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Directory name")
    dir = parser.parse_args().dir
    path = str(os.getcwd()) + "\\" + dir
    if os.path.exists(dir):
        os.chdir(path)
        print("Loading...")

        # Loading file di selected directory
        userDs = read("user")
        gameDs = read("game")
        riwayatDs = read("riwayat")
        kepemilikanDs = read("kepemilikan")
        print("Selamat datang di antarmuka \"Binomo\"")
    else:
        print("Folder \""+ str(dir) +"\" tidak ditemukan.")

if __name__ == "__main__":
    load()
