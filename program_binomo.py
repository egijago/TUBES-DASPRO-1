

# from register import *; from login import *; from tambahgame import *; from ubahgame import *; from ubah_stok import *; from list_game_toko import *;
# from buy_game import *; from list_game import *; from search_my_game import *; from search_game_at_store import *; from topupsaldo import *
# from riwayat import *; from help import *; from load import *; from save import *; from exit import *
from module import isInArr
from tictactoe import tic_tac_toe


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
    userArr = [None, None, None, None, 'guest', None]
    cmdAdmin = ["register","tambah_game","ubah_game","ubah_stok","topup"]
    cmdUser = ["buy_game","list_game","search_my_game","riwayat"] 
    cmdGuest = ["login","help","exit"]  
    cmdAdminAndUser = ["login","list_game_toko","search_game_at_store","help","save","exit","kerangajaib","tictactoe"]
    cont = True
    while cont:
        kontinu = False
        cmd = input(">> ")
        if isInArr(cmd,cmdAdmin) or isInArr(cmd,cmdUser) or isInArr(cmd,cmdAdminAndUser):
            if userArr[4] == "guest":
                if isInArr(cmd,cmdGuest) : kontinu = True
                else: 
                    print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")
                    cc = input("Apakah Anda mempunyai akun? (y/n) ")
                    if cc.lower() == 'y':
                        print("Silakan login terlebih dahulu dengan memasukkan perintah login. ")
                    elif cc.lower() == 'n':
                        print("Silakan hubungi Admin untuk registrasi. ")
                    else:
                        print("Masukan salah. ")

            elif userArr[4] == "user" :
                if (isInArr(cmd,cmdUser) or isInArr(cmd,cmdAdminAndUser)):
                    kontinu = True 
                else: 
                    print("Maaf, Anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke Administrator untuk melakukan hal tersebut. ")

            elif userArr[4] == "admin" :
                if (isInArr(cmd,cmdAdmin) or isInArr(cmd,cmdAdminAndUser)):
                    kontinu = True
                else: 
                    print("Maaf, Anda harus menjadi user untuk melakukan hal tersebut. ")

            if kontinu: 
                if cmd.lower() == ("register"):
                    userDs = register(userDs)
                elif cmd.lower() == ("login"):
                    userArr = login(userDs,userArr) 
                elif cmd.lower() == ("tambah_game"):
                    gameDs = TambahGame(gameDs)
                elif cmd.lower() == ("ubah_game"):
                    gameDs = changeGame(gameDs)
                elif cmd.lower() == ("ubah_stok"):
                    gameDs = ubah_stok(gameDs)
                elif cmd.lower() == ("list_game_toko") : 
                    list_game_toko(gameDs)
                elif cmd.lower() == ("buy_game"):
                    userDs , kepemilikanDs , riwayatDs = buy_game(gameDs,kepemilikanDs,userDs,riwayatDs,userArr[0])
                elif cmd.lower() == ("list_game") : 
                    list_game(gameDs,kepemilikanDs,userArr[0])
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
                elif cmd.lower() == ("tictactoe"):
                    tic_tac_toe()
        else:
            print("Perintah salah, masukkan perintah \"help\"")
    exit(userDs, gameDs, riwayatDs, kepemilikanDs, userArr[4])

main()
