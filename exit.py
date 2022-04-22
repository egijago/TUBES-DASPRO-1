from save import *

def exit(userDs, gameDs, riwayatDs, kepemilikanDs, role):
    # Prosedur exit()
    # Memberhentikan / keluar dari program

    # KAMUS LOKAL
    # choice : char

    # ALGORITMA
    while True and role != "guest": 
        choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
        if choice == 'y' or choice == 'n':
            if choice.lower() == 'y':
                save(userDs, gameDs, riwayatDs, kepemilikanDs)
            break
            
if __name__ == "__main__":
    exit()
