from module import *

def search_game_at_store(gameDs):
    gameId = input("Masukkan ID Game: ")
    isNullId = gameId == ""
    gameName = input("Masukkan Nama Game: ")
    isNullName = gameName == ""
    gamePrc = input("Masukkan Harga Game: ")
    isNullPrc = gamePrc == ""
    gameCtg = input("Masukkan Kategori Game: ")
    isNullCtg = gameCtg == ""
    gameRls = input("Masukkan Tahun Rilis Game: ")
    isNullRls = gameRls == ""
    
    
    for [id,nama,kategori,tahun_rilis,harga,stok] in gameDs:
        if isNullId : gameId = id
        if isNullName == '' : gameName = nama
        if isNullPrc == '' : gamePrc = harga
        if isNullCtg == '' : gameCtg = kategori
        if isNullRls == '' : gameRls = tahun_rilis

        if gameId == id and gameName == nama and gamePrc == harga and gameCtg == kategori and gameRls == tahun_rilis:
            print(f"{id} | {uni(nama,25)} | {uni(harga,8)} | {uni(kategori,8)} | {uni(tahun_rilis,4)} | {stok}") 