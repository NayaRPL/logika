print("mengerjakakan kasusu untuk logika yaitu memunculkan bilangan fibonanci")
deret=(int(input("masukkan panjang deret:")))
fibo =[0,1]

for i in range (2, deret):
   print("deret ke ",(i+1))

for i in range (2, deret):
    angka1= fibo[i-2]
    angka2=fibo[i-1]
    angkaselanjutnya=angka1+angka2

    fibo.append(angkaselanjutnya)
print(fibo)

print("cara ke 2")
panjang= int(input("panjang:"))
angka1, angka2=0,1

for i in range(panjang):
    if (i<2):
         print(i)
    else:
         angkasekarang = angka1+angka2
         print(angkasekarang, end=" ")

         angka1= angka2
         angka2= angkasekarang
