import os
import random as rd
os.system('clear')

limit = 3
com = rd.randint(1, 10)
a = True

print("Ayo tebak angka yang dipilih oleh komputer (1-10)")

while a:
    pilih = int(input("Tebak angka: "))
    
    if pilih == com:
        print("Selamat, tebakanmu benar!")
        a = False
    else:
        limit -= 1
        if limit > 0:
            print(f"Kesempatan Kamu tersisa {limit} kali.")
            a = True
        else:
            print(f"Maaf, angka yang dipilih oleh komputer adalah {com}. Kamu kalah!")
            a = False