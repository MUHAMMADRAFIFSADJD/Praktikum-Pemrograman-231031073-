pwd_benar = 'si23c'
a = True
i = 0
limit = 3
while a:
    i +=1
    pwd = input('Masukkan Password')
    if pwd == pwd_benar:
        print('Selamat Anda  berhasil Login!')
        a = False
    else:
        print('Password Salah')
        if i == limit:
            a = False
            print('Anda Kehabisan Kesepatan')
        else:
            print('Kesempatan anda tersisa',limit-i, 'kali') 










 