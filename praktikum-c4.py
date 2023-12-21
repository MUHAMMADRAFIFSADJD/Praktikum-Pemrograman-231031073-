import os
os.system('clear')

nim = ['2','3','1','0','3','1','0','7','3']

print(nim)

print('item indeks pertama',nim[0])
print('item indeks kedua',nim[1])
print('item indeks ketiga',nim[2])

print(f'item indeks 0,(pertama) {nim [0]}')
print(f'item indeks 1, (kedua) {nim [1]}')
print(f'item indeks terakhir, {nim [len(nim)-1]}')
print(f'item indeks terakhir, {nim[-1]}')
print(f'item indeks (pertama), {nim[-len(nim)]}')


data = ['Muhammad rafif sadjid',2023,'Aktif']
nilai= [90,76,93,97,99]

print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])

print(f"{data[0]} status kuliah:{data[2]}")
print(f"data terbesar nilai adalah :{max(nilai)}")
print(f"data terkecil nilai adalah :{min(nilai)}")
x = sum(nilai) / len(nilai)
print(f"Rata-rata Nilai Adalah :",x)


data = [('Muhammad Rafif Sadjid',2023,'Aktif'),
        (90,76,93,97,99),
        (20,22),
        ('S1-Reguler','Ganjil')]

matkul = ['Agama Islam',
          'Pancasila',
          'Bahasa Indonesia',
          'Wawasan Cinta IPTEK dan IMTAQ',
          'Pengantar Pemrograman',
          'Pengantar Teknologi Informasi',
          'Kalkulus Dasar I',
          'Sains Terpadu',]
sks = [2,2,2,2,3,3,3,3]


print()
#>>Daftar Mata kuliah
print("Daftar Mata kuliah :")
#>>Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f"Mata kuliah 1 : {matkul[0]} dengan jumlah {sks[0]} sks")
#>>Mata kuliah 2: Matkul2 dengan jumlah 2 sks
print(f"Mata kuliah 2 : {matkul[1]} dengan jumlah {sks[1]} sks")
#>>Mata kuliah 3: Matkul3 dengan jumlah 2 sks
print(f"Mata kuliah 3 : {matkul[2]} dengan jumlah {sks[2]} sks")
#>>Mata kuliah 4: Matkul4 dengan jumlah 2 sks
print(f"Mata kuliah 4 : {matkul[3]} dengan jumlah {sks[3]} sks")
#>>Mata kuliah 5: Matkul5 dengan jumlah 3 sks
print(f"Mata kuliah 5 : {matkul[4]} dengan jumlah {sks[4]} sks")
#>>Mata kuliah 6: Matkul6 dengan jumlah 3 sks
print(f"Mata kuliah 6 : {matkul[5]} dengan jumlah {sks[5]} sks")
#>>Mata kuliah 7: Matkul7 dengan jumlah 3 sks
print(f"Mata kuliah 7 : {matkul[6]} dengan jumlah {sks[6]} sks")
#>>Mata kuliah 8: Matkul8 dengan jumlah 3 sks
print(f"Mata kuliah 8 : {matkul[7]} dengan jumlah {sks[7]} sks")
print(f"Total SKS     : {sum(sks)}")


print(data[0][0])
print(data[-1][0])
print(data[2][0:])

print()
#>>Nama Mahasiswa : Muhammad Rafif Sadjid
print(f'Nama Mahasisiwa : {data[0][0]}')
#>>Inisial Muhammad Rafif Sadjid : M R S
print(f'Inisial Muhammad Rafif Sadjid : {data[0][0][0]} {data[0][0][9]} {data[0][0][15]}')
#>>NIM Muhammad Rafif Sadjid : 231031073
a = ''.join(nim)
print(f'NIM {data[0][0]} : {a}')
#>>Program Muhammad Rafif Sadjid : S1-Reguler Sistem Informasi C
print(f'Program {data[0][0]} : {data[-1][0]}')
#>>Angkatan Muhammad Rafif Sadjid : Ganjil-2023
print(f'Angkatan {data[0][0]} : {data[-1][1]}-{data[0][1]}')
#>>Total sks Muhammad Rafif Sadjid adalah : 11
print(f'Total sks {data[0][0]} adalah : {sum(sks)}')
#>>Jumlah nilai Muhammad Rafif Sadjid : 5
print(f'Jumlah nilai {data[0][0]} adalah : {len(data[1])}')
#>>Nilai tertinggi Muhammad Rafif Sadjid : 99
print(f'Data terbesar {data[0][0]} adalah : {max(data[1])}')
#>>Nilai terendah Muhammad Rafif Sadjid : 76
print(f'Data terkecil {data[0][0]} adalah : {min(data[1])}')
#>>Rata-rata nilai Muhammad Rafif Sadjid : 91.0
x_bar = sum(data[1])/len(data[1])
print(f'Rata-rata nilai {data[0][0]} adalah : {x_bar}')

