# from register import *; from login import *; from tambah_game import *; from ubah_game import *; from ubah_stok import *; from list_game_toko() import *;
# from buy_game import *; from list_game import *; from search_my_game import *; from search_game_at_store() import *; from topup import *
# from riwayat import *; from help import *; from load import *; from save import *; from exit import *

from load import *
from  exit import *

def main():
    load()
    from load import userDs, gameDs, riwayatDs, kepemilikanDs
    cont = True
    while cont:
        cmd = input()
        # if cmd.lower() == ("register"):
        #     register()
        # elif cmd.lower() == ("login"):
        #     login()
        # elif cmd.lower() == ("tambah_game"):
        #     tambah_game()
        # elif cmd.lower() == ("ubah_game"):
        #     ubah_game()
        # elif cmd.lower == ("ubah_stok"):
        #     ubah_stok()
        # elif cmd.lower() == ("list_game_toko") : 
        #     list_game_toko()
        # elif cmd.lower == ("buy_game"):
        #     buy_game()
        # elif cmd.lower == ("list_game") : 
        #     list_game()
        # elif cmd.lower == ("search_my_game") : 
        #     search_my_game()
        # elif cmd.lower == ("search_game_at_store") : 
        #     search_game_at_store()
        # elif cmd.lower == ("topup") : 
        #     topup()
        # elif cmd.lower == ("riwayat") : 
        #     riwayat()
        # elif cmd.lower == ("help") : 
        #     help()
        # elif cmd.lower == ("load") : 
        #     load()
        # elif cmd.lower == ("save") : 
        #     save()
        # el
        if cmd.lower() == ("exit"):
            cont = False
        
    exit()

if __name__ == "__main__":
    main()

