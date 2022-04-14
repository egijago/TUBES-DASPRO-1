import os

def save():
    from program_binomo import userDs, gameDs, riwayatDs, kepemilikanDs
    ds = ["game","kepemilikan","riwayat","user"]
    dir = input("Masukkan nama folder penyimpanan")
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
            matrix_name = type + "Ds"
            matrix = globals()[matrix_name]
            for row in matrix:
                str = ""
                for word in row:
                    str += word
                f.write(str +"\n")
        

if __name__ == "__main__":
    save()
    

        