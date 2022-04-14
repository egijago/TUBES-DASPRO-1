import module as module

data_user = [['id', 'nama', 'username', 'password', 'role', 'saldo'], 
             ['1', 'raisya', 'raisyanath', '123', 'user', '100000'], 
             ['2', 'keanna', 'lunarchronne', '123', 'user', '100000']]

binomoAccess = [None, None, None, None, 'guest', None]

def isUsernameAvail(inputUsername, data_user) :
    usernameAvail = 0
    for i in data_user :
        if i[2] == inputUsername :
            usernameAvail += 1
        else :
            pass
    
    if usernameAvail != 0 :
        return True
    else :
        return False

def isPasswordValid(inputUsername, inputPassword, data_user) :

    userTemp = []
    for i in range(module.length(data_user) - 1):
        if (data_user[i + 1][2]):
            userTemp = data_user[i + 1]
            
    if (inputPassword == userTemp[3]):
        return True
    else:
        return False

def searchLoginId(data_user, inputUsername):
    id = 0
    for i in range(module.length(data_user) - 1):
        if (inputUsername == data_user[i + 1][2]):
            id = data_user[i + 1][0]
    return int(id)
  
def login(data_user, currentState) :
    inputUsername = input("Masukkan username : ")
    inputPassword = input("Masukkan password : ")

    while not isUsernameAvail(inputUsername, data_user) or not isPasswordValid(inputUsername, inputPassword, data_user):
        if inputUsername != '' and inputPassword != '' :
            print("Password atau username salah atau tidak ditemukan")
            inputUsername = input("Masukkan username : ")
            inputPassword = input("Masukkan password : ")
        if module.length(inputUsername) == 0 or module.length(inputPassword) == 0 :
            print("Mohon masukkan password dan username Anda")
            inputUsername = input("Masukkan username : ")
            inputPassword = input("Masukkan password : ")

    print(f'Halo {data_user[searchLoginId(data_user, inputUsername)][1]}! Selamat datang di "Binomo".')

    binomoAccess = data_user[searchLoginId(data_user, inputUsername)]
    return binomoAccess

print(binomoAccess)
binomoAccess = login(data_user, binomoAccess)
print(binomoAccess)
# if (currentState[4] == "admin"):
