from module import*
def search_game_at_store(gameDs):
    # Prosedur search_game_at_store
    # Mencari dan menampilkan data game 
    # Input : gameDs        : array of array of str     ( Data dari file "game.csv" )

    # KAMUS LOKAL
    # IsNullId, IsNullName, IsNullCtg, IsNullRls    : bool
    # gameId, gameName, gameCtg, gameRls            : str
    # isNothingPrinted                              : bool

    # ALGORITMA
    gameId = input("Masukkan ID Game: ")
    isNullId = gameId == ""
    gameName = input("Masukkan Nama Game: ")
    isNullName = gameName == ""
    gamePrc = input("Masukkan Harga Game: ")
    isNullPrc = gamePrc == ""
    gameCtg = input("Masukkan Kategori Game: ")
    isNullCtg = gameCtg == ""
    gameRls = input("Masukkan Tahun Rilis Game: ")
    isNullRls = gameRls == ""
    
    isNothingPrinted = True
    for [id,nama,kategori,tahun_rilis,harga,stok] in gameDs:
        if isNullId : gameId = id
        if isNullName  : gameName = nama
        if isNullPrc  : gamePrc = harga
        if isNullCtg  : gameCtg = kategori
        if isNullRls  : gameRls = tahun_rilis

        if isInWord(gameId.lower(),id.lower()) and isInWord(gameName.lower(), nama.lower()) and isInWord(gamePrc.lower(),harga.lower()) and isInWord(gameCtg.lower(),kategori.lower()) and isInWord(gameRls.lower(),tahun_rilis.lower()):
            print(f"{id} | {uni(nama,40)} | {uni(harga,8)} | {uni(kategori,11)} | {uni(tahun_rilis,4)} | {stok}") 
            isNothingPrinted = False
    if isNothingPrinted :
        search(gameName.lower(),[row[1] for row in gameDs] )

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
    idx = []
    for i in range (len(scr)):
        if scr[i] == findMax(scr): idx += [i]
    
    # menampilkan word yang memiliki skor maksimal
    for i in range (len(idx)):
        print(arr[idx[i]])
