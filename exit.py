from save import *

def exit():
    # Prosedur exit()
    # Memberhentikan / keluar dari program

    # KAMUS LOKAL
    # choice : char

    # ALGORITMA
    while True: 
        choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
        if choice == 'y' or choice == 'n':
            if choice.lower() == 'y':
                save()
            break
            
if __name__ == "__main__":
    exit()
