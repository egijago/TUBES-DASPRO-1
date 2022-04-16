import module as module

'''
data_user = [['id', 'nama', 'username', 'password', 'role', 'saldo'], 
             ['1', 'raisya', 'raisyanath', '123', 'user', '100000'], 
             ['2', 'keanna', 'lunarchronne', '123', 'user', '100000']]


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

def searchLoginId(data_user, inputUsername):
    id = 0
    for i in range(module.length(data_user) - 1):
        if (inputUsername == data_user[i + 1][2]):
            id = data_user[i + 1][0]
    return int(id)

def topUpSaldo() :
    inputUsername = input("Masukkan username : ")
    inputSaldo = int(input("Masukkan saldo : "))

    while not isUsernameAvail(inputUsername, data_user) : 
        print(f'Username "{inputUsername}" tidak ditemukan.')
        inputUsername = input("Masukkan username : ")
        inputSaldo = int(input("Masukkan saldo : "))

    for i in data_user :
        if int(i[5]) > (inputSaldo) :
            i[5] = int(i[5]) + inputSaldo
        elif int(i[5]) < inputSaldo :
            if inputSaldo > 0 :
                i[5] = int(i[5]) + inputSaldo
            elif inputSaldo < 0 :
                if int(i[5]) - inputSaldo < 0 :
                    print("Masukan tidak valid.")
                elif int(i[5]) - inputSaldo > 0 :
                    i[5] = int(i[5]) - inputSaldo
    
    finalSaldo = i[5]
    print(f'Top up berhasil. Saldo {data_user[searchLoginId(data_user, inputUsername)][1]} bertambah menjadi {finalSaldo}.')
    return finalSaldo

 
topUpSaldo()'''

data_user = [['id', 'nama', 'username', 'password', 'role', 'saldo'],
             ['1', 'raisya', 'raisyanath', '123', 'user', '100000'],
             ['2', 'keanna', 'lunarchronne', '123', 'user', '100000']]


def isUsernameAvail(inputUsername, data_user):
    usernameAvail = 0
    for i in data_user:
        if i[2] == inputUsername:
            usernameAvail += 1
        else:
            pass

    if usernameAvail != 0:
        return True
    else:
        return False


def searchLoginId(data_user, inputUsername):
    id = 0
    # ga punya module lengthnya, jadi pake len dulu
    for i in range(len(data_user) - 1):
        if (inputUsername == data_user[i + 1][2]):
            id = data_user[i + 1][0]
    return int(id)


def isSaldoValid(inputUsername, inputSaldo, data_user):
    # saldo valid kalo input saldo lebih besar dari saldo user sekarang

    # Asumsi saldo nya valid jadi tetep dihitung
    SaldoFinalTemp = int(data_user[searchLoginId(
        data_user, inputUsername)][5]) + inputSaldo

    # Kalo saldo akhirnya ternyata negatif berarti saldo tidak valid
    if (SaldoFinalTemp < 0):
        return False
    else:
        return True


def topUpSaldo(data_user):  # Fungsi harus ngambil userdata biar bisa diproses
    inputUsername = input("Masukkan username : ")
    inputSaldo = int(input("Masukkan saldo : "))

    # Validasi username
    if (not isUsernameAvail(inputUsername, data_user)):
        print(f'Username "{inputUsername}" tidak ditemukan.')
        # Fungsi jg harus return data user sebagai update-an dari data user yg sebelumnya
        # Karena username tidak valid, data user tidak diupdate
        return data_user

    # Validasi saldo
    if (not isSaldoValid(inputUsername, inputSaldo, data_user)):
        print(f"Masukan tidak valid")
        # Karena username tidak valid, data user tidak diupdate
        return data_user

    # Kalo username dan saldo valid
    # Nentuin saldo bertambah atau berkurang
    if (inputSaldo >= 0):
        statusTopup = "bertambah"
    else:
        statusTopup = "berkurang"

    # data_user-nya diupdate terus direturn
    data_user[searchLoginId(data_user, inputUsername)][5] = int(
        data_user[searchLoginId(data_user, inputUsername)][5]) + inputSaldo
    print(
        f'Top up berhasil. Saldo {data_user[searchLoginId(data_user, inputUsername)][1]} {statusTopup} menjadi {data_user[searchLoginId(data_user, inputUsername)][5]}.')
    return data_user

    # ini syntaxnya kurang bener mangkannya error
    # for i in data_user:
    #     for j in range(1):
    #         if int(i[5][j+4]) > (inputSaldo):
    #             i[5][j+4] = int(i[5][j+4]) + inputSaldo
    #         elif int(i[5][j+4]) < inputSaldo:
    #             if inputSaldo > 0:
    #                 i[5][j+4] = int(i[5][j+4]) + inputSaldo
    #             elif inputSaldo < 0:
    #                 if int(i[5][j+4]) - inputSaldo < 0:
    #                     print("Masukan tidak valid.")
    #                 elif int(i[5][j+4]) - inputSaldo > 0:
    #                     i[5][j+4] = int(i[5][j+4]) - inputSaldo
    # finalSaldo = i[5][j+4]


print(f"Data user sebelum topup: {data_user}")
data_user = topUpSaldo(data_user)
print(f"Data user sesudah topup: {data_user}")

