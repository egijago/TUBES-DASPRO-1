import os
from datetime import datetime, date

def func(time):
    # Fungsi f(time)
    # Memperbaiki format penulisan waktu (time) agar tepat 2 digit

    # KAMUS LOKAL
    # count : int
    # let : char

    # ALGORITMA
    count = 0
    for let in str(time):
        count+=1 
    if count < 2 :
        return func("0"+str(time))
    else: 
        return str(time)
    
def save(userDs, gameDs, riwayatDs, kepemilikanDs):
    # Prosedur save()
    # Menyimpan perubahan dalam csv

    # KAMUS LOKAL
    # ds : array of str
    # dir, type : str
    # matrix : array of array of str
    # row : array of str
    # str : str
    
    #ALGORITMA
    # from program_binomo import userDs, gameDs, riwayatDs, kepemilikanDs

    ds = ["game","kepemilikan","riwayat","user"]
    dir = input("Masukkan nama folder penyimpanan: ")
    if dir == "":
        dt = datetime.today()
        dir = str(date.today()) + "_" + func(dt.hour) + func(dt.minute) + func(dt.second)
    if not os.path.exists(dir):
        os.makedirs(dir)
        os.chdir(dir)
    else:
        os.chdir(dir)
        for type in ds:
            os.remove(type + ".csv")

    print("Saving...")

    for type in ds:
        with open(type + ".csv", "x") as f:
            matrix = locals()[type + "Ds"]
            for row in matrix:
                string = ""
                for word in row:
                    string += word + ";"
                f.write(string +"\n")
    print(f"Data telah disimpan dalam folder {dir}!")
    os.chdir("..")

if __name__ == "__main__":
    save()
    

        