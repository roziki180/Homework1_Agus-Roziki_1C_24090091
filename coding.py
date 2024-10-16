#Data Penerima BLT
print('DATA DIRI')
nama = (input('Masukkan Nama : '))
nik = int(input('Masukkan NIK : ')) 
no = int(input('Masukkan Nomor HP : '))
tempat = str(input('Masukkan Tempat Tinggal : '))
print()

#syarat mendapatkan BLT
print('SYARAT MENDAPATKAN BLT')
usia =int(input ('Masukan Usia : '))
wni = (input ('masukan wni : '))
pekerjaan = (input ('masukan pekerjaan : '))

win = ("indonesia")
pekerjaan_kecuali = ['pns','dokter','tni','polri','bumn']

if (usia > 50 ) and (wni in win)  and (pekerjaan not in pekerjaan_kecuali ):
    hasil = ('MENDAPATKAN BANTUAN BLT')
else:
    hasil = ('TIDAK MENDAPAT BANTUAN BLT')

print('-'*50)
print ('DATA PENERIMA')
print('Nama : ', nama)
print("NIK : ", nik)
print('Nomor Hp : ', no)
print(hasil)