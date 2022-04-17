from module import *
Arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', 
    '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', 
    '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', 
    '^', '_', '`', '{', '|', '}', '~',' ']

def findOrd(char,Arr):
    # Fungsi findOrd(char,Arr)
    # mencari index dari karakter char dalam list karakter Arr

    # KAMUS 
    # char : char
    # Arr  : array of char

    # ALGORITMA
    for i in range (length(Arr)):
        if char == Arr[i]:
            return i

def findChar(ord,Arr):
    # Fungsi findChar(ordArr)
    # mencari karakter dari index ord dalam list karakter Arr

    # KAMUS 
    # ord  : int
    # Arr  : array of char

    # ALGORITMA
    idx = ord % length(Arr)
    return Arr[idx]

def encrypt(word,n,x):
    # Fungsi encrypt(word,n,x)
    # mengenkripsi kata word dengan kunci n dan x 

    # KAMUS 
    # newArr    : array of char
    # ord       : array of int
    # newWord   : str

    # ALGORITMA
    global Arr
    newArr = Arr[n:length(Arr)]+Arr[:n]
    ord = []
    for i in range (length(word)):
        ord += [int(x) * i + findOrd(word[i],newArr)]
    
    newWord = ''
    for i in ord: 
        newWord += findChar(i,Arr)
    newWord = newWord[n%length(newWord):length(newWord)] + newWord[:n%length(newWord)]
    return newWord

def decrypt(word,n,x): 
    # Fungsi decrypt(word,n,x)
    # mendekripsi kata word dengan kunci n dan x 

    # KAMUS 
    # newArr    : array of char
    # ord       : array of int
    # newWord   : str

    # ALGORITMA
    global Arr
    newArr = Arr[n:length(Arr)]+Arr[:n]
    word = word[length(word)-n%length(word):length(word)] + word[:length(word)-n%length(word)]
    ord = []
    for i in range (length(word)) : 
        ord+= [findOrd(word[i],Arr) - int(x) * i ]

    newWord = ""
    for i in ord: 
        newWord += findChar(i,newArr) 
    return newWord

# TESTING
# from random import *
# count = 0
# for i in range (10000):
#     x = randint(1,100)
#     y = randint(1,100)
#     leng = randint(1,100)
#     idx = []
#     for i in range (leng):
#         idx += [randint(0,len(Arr))] 
#     string = ''
#     for i in idx:
#         string += findChar(i,Arr)
#     newstring = encrypt(string,x,y)
#     destring = decrypt(newstring,x,y)
#     print(string,newstring,destring,string==destring)
#     if string != destring :
#         count+=1
# print(count)

