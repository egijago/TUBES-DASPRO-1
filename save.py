import os
import csv
def save():
    dir = input("Masukkan nama folder penyimpanan")
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.chdir(dir)
    for type in ["user","game","kepemilikan","riwayat"]:
        file = open(str(type)+".csv",'w',newline = '')
        arr = []
        for row in matrix{type}:
            str = []
            for letter in row:
                str += letter + ';'  
            arr += str
        with file:
            write = csv.writer(file)
            write.writerows(arr)