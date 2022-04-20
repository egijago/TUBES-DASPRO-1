from calendar import c
import time 

def magicConchShell() :
    inputQuestion = input("Tanya kerang ajaib : ")

    a = 1
    c = 1
    m = 5
    x = time.time()
    number = (((a*x) + c) % m)

    randomNumber = number

    if (randomNumber <= 0.5555) :
        print("Ya.")
    elif (0.5555 < randomNumber <= (2*0.5555)) :
        print("Tidak.")
    elif ((2*0.5555) < randomNumber <= (3*0.5555)) :
        print("Bisa Jadi.")
    elif ((3*0.5555) < randomNumber <= (4*0.5555)) :
        print("Mungkin.")
    elif ((4*0.5555) < randomNumber <= (5*0.5555)) :
        print("Tentunya.")
    elif((5*0.5555) < randomNumber <= (6*0.5555)):
        print("Tidak mungkin.")
    else :
        print("Tanya lagi nanti.")
    return number

# magicConchShell()
# Ya = 0
# Tidak = 0 
# Bisajadi = 0
# Mungkin = 0
# Tentu = 0
# Tidakmungkin = 0
# Tanyalaginanti = 0
# for i in range (10000): 
#     time
#     if (magicConchShell() <= 0.5555) :
#         Ya +=1 
#     elif (0.5555 < magicConchShell() <= (2*0.5555)) :
#         Tidak +=1
#     elif ((2*0.5555) < magicConchShell() <= (3*0.5555)) :
#         Bisajadi+=1
#     elif ((3*0.5555) < magicConchShell() <= (4*0.5555)) :
#         Mungkin+=1
#     elif ((4*0.5555) < magicConchShell() <= (5*0.5555)) :
#         Tentu+=1
#     elif((5*0.5555) < magicConchShell() <= (6*0.5555)):
#         Tidakmungkin+=1
#     else :
#         Tanyalaginanti+=1
# print(Ya,Tidak,Bisajadi,Mungkin,Tentu,Tidakmungkin,Tanyalaginanti)
