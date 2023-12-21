import os
import random as rd
os.system

warna = ['merah','putih','hitam']
com = rd.choice(warna)
a = True

while a: 
    pilih = input('Masukan Pilihan [merah,putih,hitam]: ')
    if pilih == com:
        print(f'Pilihan anda benar yaitu {pilih}')
        a = False
    else:
        print('Tebakan anda salah! coba lagi.')
    