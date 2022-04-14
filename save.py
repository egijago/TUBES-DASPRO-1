import os
import csv
def save():
    dir = input("Masukkan nama folder penyimpanan")
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.chdir(dir)
    for type in ["user","game","kepemilikan","riwayat"]:
        file = open(str(type)+".csv",'w+',newline = '')
        