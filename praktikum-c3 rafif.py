nama="Muhammad Rafif Sadjid"
nim="231031073"
meet="Praktikum 3(string)"
prodi="Sistem Informasi C"
email="-muhrafif687@gmail.com"
ttl= "Parepare, 29-april-2005"
alamat= "Jalan kelapa gading"
asal= "Parepare"
hobi= "olahraga"
tinggi= "161"
print()
print("-"*110)
str1= "muhammad rafif sadjid"

sp = 110
print("-"*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print("\n"*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.rjust(sp))
print("-"*sp)
    

print ("""\tHalo, nama saya {nama} dengan NIM {nim} dari prodi{prodi}, ini adalah file {meet}.Terim kasih.\n""")


print(f"""Biodata saya,
nama\t: {nama.upper()}
Nim\t: {nim}
Prodi\t: {prodi}
TTL\t: {ttl}
Alamat\t: {alamat}
Asal\t: {asal}
Hobi\t: {hobi}
Tinggi\t: {tinggi}cm
""")

# Stat1: Issac duFort Frankel Sir
stat1 = 'duFort Frankel Sir Issac'
result1 = stat1.split()
result1 = result1[-1] + ' ' + ' '.join(result1[:-1])
print(result1)

# Stat2: d F S Issac
stat2 = 'duFort Frankel Sir Issac'
result2 = stat2.split()
result2 = ' '.join([word[0] for word in result2]) + ' ' + result2[-1]
print(result2)

# Stat3: duFort F S I
stat3 = 'duFort Frankel Sir Issac'
result3 = stat3.split()
result3 = ' '.join([word if word == 'duFort' else word[0] for word in result3])
print(result3)

# Stat4: I duFort Frankel Sir
stat4 = 'duFort Frankel Sir Issac'
result4 = stat4.split()
result4 = result4[-1] + ' ' + ' '.join(result4[:-1])
result4 = result4[0] + ' ' + result4[1:]
print(result4)

# Stat5: Issac d F S
stat5 = 'duFort Frankel Sir Issac'
result5 = stat5.split()
result5 = result5[-1] + ' ' + ' '.join(result5[:-1])
result5 = result5[0] + ' ' + result5[1:]
print(result5)

# Stat6: ISSAC D F S
stat6 = 'duFort Frankel Sir Issac'
result6 = stat6.split()
result6 = result6[-1].upper() + ' ' + ' '.join([word[0].upper() for word in result6[:-1]])
print(result6)

stat7 = '#duFort Frankel Sir Issac$'
# duFort Frankel Sir Issac
stat7 = stat7.strip("#$")
print(stat7)

stat8 = '#duFort-Frankel-Sir-Issac$'
# duFort Frankel Sir Issac
stat8 = stat8.strip("#$").replace("-"," ")
print(stat8)

stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
# duFort Frankel Sir Issac
import re
stat9 = re.findall(r'\w+', stat9)
hasil = ' '.join(stat9)
print(hasil)

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
# DUFORT FRANKEL SIR ISSAC
import re
stat10 = re.findall(r'\w+', stat10)
hasil = ' '.join(stat10.upper() for stat10 in stat10)
print(hasil)


print()





