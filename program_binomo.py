import register; import login; import tambah_game; import ubah_game; import ubah_stok; import list_game_toko();
import buy_game; import list_game; import search_my_game; import search_game_at_store(); import topup
import riwayat; import help; import load; import save; import exit
 
def main():
    load()
    cont = True
    while cont:
        cmd = input()
        if cmd.lower() == ("register"):
            register()
        elif cmd.lower() == ("login"):
            login()
        elif cmd.lower() == ("tambah_game"):
            tambah_game()
        elif cmd.lower() == ("ubah_game"):
            ubah_game()
        elif cmd.lower == ("ubah_stok"):
            ubah_stok()
        elif cmd.lower() == ("list_game_toko") : 
            list_game_toko()
        elif cmd.lower == ("buy_game"):
            buy_game()
        elif cmd.lower == ("list_game") : 
            list_game()
        elif cmd.lower == ("search_my_game") : 
            search_my_game()
        elif cmd.lower == ("search_game_at_store") : 
            search_game_at_store()
        elif cmd.lower == ("topup") : 
            topup()
        elif cmd.lower == ("riwayat") : 
            riwayat()
        elif cmd.lower == ("help") : 
            help()
        elif cmd.lower == ("load") : 
            load()
        elif cmd.lower == ("save") : 
            save()
        elif cmd.lower() == ("exit"):
            cont = False
        
    exit()
if __name__ == "__main__":
    main()
