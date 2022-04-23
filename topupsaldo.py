import module as module

# data_user = [['id', 'nama', 'username', 'password', 'role', 'saldo'],
#              ['1', 'raisya', 'raisyanath', '123', 'user', '100000'],
#              ['2', 'keanna', 'lunarchronne', '123', 'user', '100000']]


def isUsernameAvail(inputUsername, data_user) :
    usernameAvail = 0
    for i in range(module.length(data_user)) :
        if data_user[i][1] == inputUsername :
            usernameAvail += 1
        else :
            pass
    
    if usernameAvail != 0 :
        return True
    else :
        return False


def searchLoginId(data_user, inputUsername):
    id = 0
    for i in range(module.length(data_user) ):
        if (inputUsername == data_user[i][1]):
            id = data_user[i][0]
    return int(id)


def isSaldoValid(inputUsername, inputSaldo, data_user):
   
    SaldoFinalTemp = int(data_user[searchLoginId(
        data_user, inputUsername)][5]) + inputSaldo
    
    if (SaldoFinalTemp < 0):
        return False
    else:
        return True


def topUpSaldo(data_user): 
    inputUsername = input("Masukkan username : ")
    inputSaldo = int(input("Masukkan saldo : "))

    if (not isUsernameAvail(inputUsername, data_user)):
        print(f'Username "{inputUsername}" tidak ditemukan.')
        return data_user

    if (not isSaldoValid(inputUsername, inputSaldo, data_user)):
        print(f"Masukan tidak valid")
        return data_user

    if (inputSaldo >= 0):
        statusTopup = "bertambah"
    else:
        statusTopup = "berkurang"

    data_user[searchLoginId(data_user, inputUsername)][5] = int(
        data_user[searchLoginId(data_user, inputUsername)][5]) + inputSaldo
    print(
        f'Top up berhasil. Saldo {data_user[searchLoginId(data_user, inputUsername)][1]} {statusTopup} menjadi {data_user[searchLoginId(data_user, inputUsername)][5]}.')
    return data_user

# print(f"Data user sebelum top up: {data_user}")
# data_user = topUpSaldo(data_user)
# print(f"Data user sesudah top up: {data_user}")
