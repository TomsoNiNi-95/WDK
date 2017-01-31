#!/usr/bin/env python
#importowane biblioteki
import hashlib
import ssdeep
plik = open('C:/Users/Tomek/Desktop/test.zip','rb')
#plik.mode - pokaze nam, w jakim trybie dzia³amy, w tym przypadku rb, czyli otwarcie pliku w trybie binarnym (dodanie 'b' do 'r' nam to daje)
#plik.name - tutaj zwróci nam œcie¿kê do pliku, który jest dostêpny z tego obiektu
try:
    czytaj_plik = plik.read();
finally:
    plik.close()

md = hashlib.md5(czytaj_plik).hexdigest() #generujemy skrót MD5
print("MD5:")
print(md)	#wypisujemy skrót MD5

sha = hashlib.sha256(czytaj_plik).hexdigest() #generujemy skrót SHA-256
print("SHA-256:")
print(sha)	#wypisujemy skrót SHA-256

ssdp = ssdeep.hash(czytaj_plik)	#generujemy skrót ssdeep
print("SSDEEP:")
print(ssdp)	#wypisujemy skrót ssdeep

blocksize = 65535

mddeep = " "
with open('C:/Users/Tomek/Desktop/test.zip',"rb") as file: 
	for wynik in iter(lambda: file.read(1025),""): #u¿ycie funkcji lambda
		md5dp=hashlib.md5(wynik)
		mddeep=mddeep+md5dp.hexdigest() #generujemy skrót md5deep
print("MD5DEEP:")
print(mddeep)	#wypisujemy skrót md5deep