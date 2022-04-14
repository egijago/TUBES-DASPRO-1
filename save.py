import os

def save():
    # Prosedur save()
    # Menyimpan perubahan dalam csv

    # KAMUS LOKAL
    # ds : array of str
    # dir, type : str
    # matrix : array of array of str
    # row : array of str
    # str : str
    
    #ALGORITMA
    from program_binomo import userDs, gameDs, riwayatDs, kepemilikanDs

    ds = ["game","kepemilikan","riwayat","user"]
    dir = input("Masukkan nama folder penyimpanan: ")
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
                str = ""
                for word in row:
                    str += word + ";"
                f.write(str +"\n")
    print(f"Data telah disimpan dalam folder {dir}!")
    os.chdir("..")

if __name__ == "__main__":
    save()
    

        