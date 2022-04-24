# F02 - REGISTER
import module as module
# from program_binomo import userDs
# data_user = userDs


def register(userDs) :
    # Fungsi register
    # Registrasi pengguna baru
    # Input : userDs  : array of array of str (Data dari file "user.csv" )
    
    # KAMUS LOKAL
    # inputNama      : str
    # inputUsername  : str
    # inputPassword  : str
    
    # ALGORITMA
    data_user = userDs
    inputNama = str(input("Masukkan nama : "))
    inputUsername = str(input("Masukkan username: "))
    inputPassword = str(input("Masukkan password : "))
    # Apabila user menginput nama, username, atau password, tetapi tidak sesuai dengan ketentuan
    if inputNama != "" and inputPassword != "" and inputUsername!='' :
        while True :
            # Apabila username yang diinput tidak valid
            if not isUsernameValid(inputUsername) :
                print(f'username hanya boleh mengandung alfabet A-Z atau a-z, underscore "_", strip "-", dan angka 0-9')
                inputNama = str(input("Masukkan nama : "))
                inputUsername = str(input("Masukkan username: "))
                inputPassword = str(input("Masukkan password : "))
            # Apabila username yang diinput telah digunakan oleh pengguna ;ain
            elif isAlreadyUsed(inputUsername,data_user) :
                print(f'username {inputUsername} sudah terpakai, silakan menggunakan username lain')
                inputNama = str(input("Masukkan nama : "))
                inputUsername = str(input("Masukkan username: "))
                inputPassword = str(input("Masukkan password : "))
            else :
                break
        
        id = module.length(data_user)
        data_user = data_user + [[str(id), inputUsername, inputNama, inputPassword, 'user', '0']]
        print(f'Username {inputUsername} telah berhasil register ke dalam "Binomo"')
    # Apabila user tidak menginput salah satu dari nama, username, atau password
    else:
        print("Nama, username, dan password tidak boleh kosong. ")
    return data_user

def isUsernameValid(inputUsername) :
    # Fungsi isUsernameValid
    # Mengecek apakah username yang dimasukkan valid dan sesuai ketentuan yang ditetapkan
    # Input : inputUsername : str
    
    # KAMUS LOKAL
    # CharacterValid : str
    
    # ALGORITMA
    validCharacters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F','f', 'G', 'g', 'H', 'h', 'I', 'i', 'J',
                        'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's',
                        'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '_', '-', '0', '1', '2',
                        '3', '4', '5', '6', '7', '8', '9']
    
    matchedCharacters = [characters in validCharacters for characters in (inputUsername)] 

    CharacterValid = 0
    for index in range (module.length(inputUsername)) :
        if matchedCharacters[index] == True :
            CharacterValid += 1
        else :
            pass

    if CharacterValid == module.length(inputUsername) :
        return True
    else :
        return False


def isAlreadyUsed(inputUsername,data_user) :
    # Fungsi isAlreadyUsed
    # Mengecek apakah username yang diinput oleh pengguna telah digunakan atau belum
    # Input : inputUsername : str
    #         data_user     : array of array of str ( Data dari file "user.csv" )
    
    # KAMUS LOKAL
    # sameUsername : int
    
    # ALGORITMA
    sameUsername = 0
    for i in data_user :
        if i[1] == inputUsername :
            sameUsername += 1
        else :
            pass
    
    if sameUsername != 0 :
        return True
    else :
        return False

