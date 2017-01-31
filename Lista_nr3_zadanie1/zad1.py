#!/usr/bin/env python
#importowane biblioteki
import hashlib
import ssdeep
plik = open('C:/Users/Tomek/Desktop/test.zip','rb')
#plik.mode - pokaze nam, w jakim trybie dzia�amy, w tym przypadku rb, czyli otwarcie pliku w trybie binarnym (dodanie 'b' do 'r' nam to daje)
#plik.name - tutaj zwr�ci nam �cie�k� do pliku, kt�ry jest dost�pny z tego obiektu
try:
    czytaj_plik = plik.read();
finally:
    plik.close()

md = hashlib.md5(czytaj_plik).hexdigest() #generujemy skr�t MD5
print("MD5:")
print(md)	#wypisujemy skr�t MD5

sha = hashlib.sha256(czytaj_plik).hexdigest() #generujemy skr�t SHA-256
print("SHA-256:")
print(sha)	#wypisujemy skr�t SHA-256

ssdp = ssdeep.hash(czytaj_plik)	#generujemy skr�t ssdeep
print("SSDEEP:")
print(ssdp)	#wypisujemy skr�t ssdeep

blocksize = 65535

mddeep = " "
with open('C:/Users/Tomek/Desktop/test.zip',"rb") as file: 
	for wynik in iter(lambda: file.read(1025),""): #u�ycie funkcji lambda
		md5dp=hashlib.md5(wynik)
		mddeep=mddeep+md5dp.hexdigest() #generujemy skr�t md5deep
print("MD5DEEP:")
print(mddeep)	#wypisujemy skr�t md5deep