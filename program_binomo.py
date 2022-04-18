# from register import *; from login import *; from tambahgame import *; from ubahgame import *; from ubah_stok import *; from list_game_toko import *;
# from buy_game import *; from list_game import *; from search_my_game import *; from search_game_at_store import *; from topupsaldo import *
# from riwayat import *; from help import *; from load import *; from save import *; from exit import *


# from load import *
# from search_game_at_store import *
# from  exit import *
# from list_game_toko import *
# from ubahgame import changeGame

# from register import *; from login import *; from tambahgame import *; from ubahgame import *; from ubah_stok import *; from list_game_toko import *;
# from buy_game import *; from list_game import *; from search_my_game import *; from search_game_at_store import *; from topupsaldo import *
# from riwayat import *; from help import *; from load import *; from save import *; from exit import *
def main():  
    from register import register; from login import login; from tambahgame import TambahGame; from ubahgame import changeGame; from ubah_stok import ubah_stok; from list_game_toko import list_game_toko;
    from buy_game import buy_game; from list_game import list_game; from search_my_game import search_my_game; from search_game_at_store import search_game_at_store; from topupsaldo import topUpSaldo
    from riwayat import riwayat; from help import help_; from load import load; from save import save; from exit import exit ; from kerangajaib import magicConchShell
    # Program Binomo
    # Menjalankan program_binomo sesuai spesifikasi

    # KAMUS 
    # gameDs           : array of array of str     ( Data dari file "game.csv" )
    # kemepilikanDs    : array of array of str     ( Data dari file "kepemilikan.csv" )
    # userDs           : array of array of str     ( Data dari file "user.csv" )
    # riwayatDs        : array of array of str     ( Data dari file "riwayat.csv" )
    # userArr          : array of str              ( Data user yang sedang log in )
    # cont             : bool                      


    # ALGORITMA
    userDs, gameDs, riwayatDs, kepemilikanDs = load()
    userArr = []
    cont = True
    while cont:
        cmd = input()
        if cmd.lower() == ("register"):
            userDs = register(userDs)
        elif cmd.lower() == ("login"):
            userArr = login(userDs) 
        elif cmd.lower() == ("tambah_game"):
            gameDs = TambahGame(gameDs)
        elif cmd.lower() == ("ubah_game"):
            gameDs = changeGame(gameDs)
        elif cmd.lower() == ("ubah_stok"):
            gameDs = ubah_stok(gameDs)
        elif cmd.lower() == ("list_game_toko") : 
            list_game_toko(userDs)
        elif cmd.lower() == ("buy_game"):
            kepemilikanDs , riwayatDs = buy_game(gameDs,kepemilikanDs,userDs,riwayatDs,userArr[0])
        elif cmd.lower == ("list_game") : 
            list_game(gameDs,kepemilikanDs,userDs)
        elif cmd.lower() == ("search_my_game") : 
            search_my_game(userArr,kepemilikanDs,gameDs)
        elif cmd.lower() == ("search_game_at_store") : 
            search_game_at_store(gameDs)
        elif cmd.lower() == ("topup") : 
            userDs = topUpSaldo(userDs)
        elif cmd.lower() == ("riwayat") : 
            riwayat(gameDs, kepemilikanDs, userArr[0], riwayatDs)
        elif cmd.lower() == ("help") : 
            help_(userArr)
        elif cmd.lower() == ("save") : 
            save(userDs, gameDs, riwayatDs, kepemilikanDs)
        elif cmd.lower() == ("exit"):
            cont = False
        elif cmd.lower() == ("kerangajaib"):
            magicConchShell()
        
    exit(userDs, gameDs, riwayatDs, kepemilikanDs)

if __name__ == "__main__":
    main()

