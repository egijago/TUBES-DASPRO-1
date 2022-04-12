import argparse
import os
def load():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Nama foldernya")
    dir = parser.parse_args().folder
    path = str(os.getcwd()) + "\\" + dir
    if os.path.exists(dir):
        os.chdir(path)
        print("Loading...")
        print("Selamat datang di antarmuka \"Binomo\"")
    else:
        print("Folder \""+ str(dir) +"\" tidka ditemukan.")
if __name__ == "__main__":
    load()