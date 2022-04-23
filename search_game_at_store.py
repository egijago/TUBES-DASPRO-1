from module import*
def validInput(word,arr,count):
    for i in range (count):
        cc = input(word)
        if isInArr(cc,arr): 
            return cc  
        elif i < count : 
            print(f"Masukan salah. Harap masukkan kembali.")
    print("Terlalu sering melakukan kesalahan. ")
    return ''
def search_game_at_store(gameDs):
    # Prosedur search_game_at_store
    # Mencari dan menampilkan data game 
    # Input : gameDs        : array of array of str     ( Data dari file "game.csv" )

    # KAMUS LOKAL
    # gameId, gameName, gameCtg, gameRls            : str
    # isNothingPrinted                              : bool

    # ALGORITMA
    # input parameter
    gameId = input("Masukkan ID Game: ")
    gameName = input("Masukkan Nama Game: ")
    gamePrc = input("Masukkan Harga Game: ")
    gameCtg = input("Masukkan Kategori Game: ")
    gameRls = input("Masukkan Tahun Rilis Game: ")

    # print data sesuai parameter jika ada
    isNothingPrinted = print_game(gameId,gameName,gamePrc,gameCtg,gameRls,gameDs)

    # jika tidak ada maka akan di kira-kira data yang sekiranya sesuai
    if isNothingPrinted:
        # menebak nama game
        if gameName != '':
            probName = search(gameName,[row[1] for row in gameDs])
            probNameString = ''
            for i in range (length(probName)):
                if i != length(probName)-1: probNameString += probName[i] + " atau "
                else: probNameString += probName[i]
            ccName = validInput(f"Apakah nama game yang Anda maksud {probNameString} ? (y/n) ",['y','n'],3) 
        else:
            ccName = 'n'
        # menebak kategori
        if gameCtg != '':
            probCtg = search(gameCtg,[row[2] for row in gameDs])[0]
            ccCtg = validInput(f"Apakah yang Anda maksud {probCtg} ? (y/n) ",['y','n'],3)
        else:
            ccCtg = 'n'
        
        # print sesuai tebakan
        if ccCtg.lower() == 'y' and ccName.lower() == 'y' : 
            isNotPrinted = True
            for name in probName : 
                local_isNotPrinted = print_game('',name,'',probCtg,'',gameDs)
                if local_isNotPrinted == False :  isNotPrinted = False
            if isNotPrinted:print("Tidak ada game pada toko yang memenuhi kriteria. ")
        elif ccCtg.lower() == 'n' and ccName.lower() == 'y':
            isNotPrinted = True
            for name in probName : 
                local_isNotPrinted = print_game('',name,'','','',gameDs)
                if local_isNotPrinted == False :  isNotPrinted = False
            if isNotPrinted:print("Tidak ada game pada toko yang memenuhi kriteria. ")
        elif ccName.lower() == 'n' and ccCtg.lower() == 'y':
            isNotPrinted = print_game('','','',probCtg,'',gameDs)
            if isNotPrinted:print("Tidak ada game pada toko yang memenuhi kriteria. ")
        else: 
            print("Tidak ada game pada toko yang memenuhi kriteria. ")

def print_game(gameId,gameName,gamePrc,gameCtg,gameRls,gameDs): 
    # Prosedur print_game
    # Melakukan print data yang sesuai dengan parameter
    # input : gameId, gameName, gameCtg, gameRls            : str  (Parameter pencarian)

    # KAMUS LOKAL
    # IsNullId, IsNullName, IsNullCtg, IsNullRls    : bool

    # ALGORITMA
    isNothingPrinted = True
    isNullId = gameId == ""
    isNullName = gameName == ""
    isNullPrc = gamePrc == ""
    isNullCtg = gameCtg == ""
    isNullRls = gameRls == ""
    for [id,nama,kategori,tahun_rilis,harga,stok] in gameDs:
        if isNullId : gameId = id
        if isNullName  : gameName = nama
        if isNullPrc  : gamePrc = harga
        if isNullCtg  : gameCtg = kategori
        if isNullRls  : gameRls = tahun_rilis

        if isInWord(gameId.lower(),id.lower()) and isInWord(gameName.lower(), nama.lower()) and isInWord(gamePrc.lower(),harga.lower()) and isInWord(gameCtg.lower(),kategori.lower()) and isInWord(gameRls.lower(),tahun_rilis.lower()):
            print(f"{id} | {uni(nama,40)} | {uni(harga,8)} | {uni(kategori,11)} | {uni(tahun_rilis,4)} | {stok}") 
            isNothingPrinted = False
    return isNothingPrinted

def slice(word,start,end):
    # Fungsi Slice
    # Memotong string word dari index start sampai index end-1

    # KAMUS LOKAL
    # newWord       : str
    # idx           : int

    # ALGORITMA
    newWord =""
    for idx in range (start,end):
        newWord+=word[idx]
    return newWord

def noSpace(word):
    # Fungsi No Space
    # Menghilangkan space pada string word

    # KAMUS LOKAL 
    # newWord           : str
    # i                 : int
    
    # ALGORITMA
    newWord =''
    for i in word:
        if i!=" ": newWord+=i
    return newWord

def eval(string,word):
    # Fungsi Eval
    # Mengembalikan poin kecocokan antara string dan word

    # KAMUS 
    # string, word              : str
    # # 
    string = noSpace(string).lower() ;word = noSpace(word).lower()

    # Menyamakan panjang string dan word
    if length(string)>=length(word):
        for i in range (length(string)-length(word)):word= '`' + word
    else:
        for i in range (length(word)-length(string)):string+= '~'

    maxscore = 0
    # iterasi penggeseran word ke kanan
    for start in range (length(word)): 
        newWord = slice(word,start,length(word)) + slice(word,0,start)
        # menghitung skor dari tiap iterasi penggeseran word                                               
        totalscore = 0
        # iterasi pengecekan setiap huruf di string
        for idString in range (length(string)):
            score = 0
            for idWord in range (length(newWord)):
                # Mencari skor dari setiap huruf pada string sebagai fungsi posisi
                if string[idString] == newWord[idWord] and abs(idString-idWord)<5 : 
                    subScore = 1/(abs(idString-idWord)+1)
                    if subScore >= score:score = subScore
            totalscore += score
        if totalscore > maxscore:maxscore = totalscore 
    # mengembalikan nilai maksimum yang diperoleh dari skor pada tiap iterasi
    return maxscore

def search(string,arr):
    # Fungsi search
    # Mencari word yang paling cocok dengan string di array arr

    # KAMUS 
    # scr           : array of int
    # idx           : array of int
    # i             : int
    
    # ALGORITMA
    # mencari skor dari setiap word di array arr
    scr = [0 for i in range(length(arr))]
    for idx in range(length(arr)):
        scr[idx] = eval(string,arr[idx])

    # mencari index dari word yang memiliki skor maksimal
    maxScore = findMax(scr)
    idx = []
    for i in range (length(scr)):
        if scr[i] == maxScore: idx += [i]
    
    return [arr[i] for i in idx]


