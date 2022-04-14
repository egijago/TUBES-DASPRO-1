import os

def save():
    dir = input("Masukkan nama folder penyimpanan")
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.chdir(dir)
    print("Saving...")
    

        