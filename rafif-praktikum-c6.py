a= True

while a:
    jawab = input('Apakah ingin lanjutkan? (y/n)')
    if jawab == 'y':
        print('Selamat Datang Lagi!')
        a = True
    elif jawab == 'n':
        print ('Sampai Ketemu Lagi :)')
        a = False
    else:
        print ('Jangan Aneh-aneh deh :)')
        a = True
    