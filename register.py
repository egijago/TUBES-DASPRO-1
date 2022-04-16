import module as module
# from program_binomo import userDs
# data_user = userDs
# data_user = [['id', 'nama', 'username', 'password', 'role', 'saldo'], 
#              ['1', 'raisya', 'raisyanath', '123', 'user', '100000'], 
#              ['2', 'keanna', 'lunarchronne', '123', 'user', '100000']]

def register(userDs) :
    # global data_user
    data_user = userDs
    inputNama = str(input("Masukkan nama : "))
    inputUsername = str(input("Masukkan username: "))
    inputPassword = str(input("Masukkan password : "))

    while True :
        if not isUsernameValid(inputUsername) :
            print(f'username hanya boleh mengandung alfabet A-Z atau a-z, underscore "_", strip "-", dan angka 0-9')
            inputNama = str(input("Masukkan nama : "))
            inputUsername = str(input("Masukkan username: "))
            inputPassword = str(input("Masukkan password : "))
        elif isAlreadyUsed(inputUsername) :
            print(f'username {inputUsername} sudah terpakai, silakan menggunakan username lain')
            inputNama = str(input("Masukkan nama : "))
            inputUsername = str(input("Masukkan username: "))
            inputPassword = str(input("Masukkan password : "))
        else :
            break
    
    id = module.length(data_user)
    data_user = data_user + [id+1, inputNama, inputUsername, inputPassword, 'user', '0']
    print(f'Username {inputUsername} telah berhasil register ke dalam "Binomo"')
    return data_user

def isUsernameValid(inputUsername) :
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


def isAlreadyUsed(inputUsername) :
    global data_user
    sameUsername = 0
    for i in data_user :
        if i[2] == inputUsername :
            sameUsername += 1
        else :
            pass
    
    if sameUsername != 0 :
        return True
    else :
        return False


if __name__ == "__main__":
    register()
# Register()
# print(data_user)