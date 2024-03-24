# Modul math digunakan untuk operasi matematika, seperti sqrt(akar kuadrat) dan pi
import math

# Membuat set nums dengan elemen
nums= {1,3,7,6,5}
"""
Menghapus elemen 4 dari set nums...
Jika 4 tidak ada dalam set, discard() tidak melakukan apa-apa
"""
nums.discard(4)
print(nums)

# Apa Outputnya?

"""
String text, ekspresi 1 + 1 menghasilkan nilai 2...
Mengambil indeks ke 2 dari text
"""
print('text'[1+1])

# Apa Outputnya?

# Tuple nums dengan nilai
nums= (1,2,3,4,5)
"""
Menggunakan slicing untuk membuat tuple baru yaitu nums2...
Slicing [1:4] mengambil elemen dari index 1 hingga (4-1), yaitu 1,2 dan 3...
Operator kali 2 mengandakan tuple tersebut
"""
nums2= nums[1:4]*2
print(nums2)

# Apa Outputnya?

# Menambahkan atau menggabungkan list kosong
zeroz = [] + []
print(zeroz)

# Apa Outputnya?

# Membuat set kosong
nums= set()
# Melakukan iterasi dari 21 hingga 29 dan 30 tidak termasuk
for num in range(21,30):
    # Menambahkan setiap angka dalam rentang ke dalam set nums
    nums.add(num)
print(nums)

# Apa Outputnya?

# Membuat set kosong
nums = set()
# Melakukan iterasi dari 21 hingga 29 dan 30 tidak termasuk
for num in range(21,30):
    # Memeriksa apakah angka adalah ganjil
    if num % 2:
        # Jika angka ganjil, tambahkan ke dalam set nums
        nums.add(num)
print(nums)

# Apa Outputnya?

# membuat set kosong
nums = set()
# Melakukan itersi dari 21 hingga 29 dan 30 tidak termasuk
for num in range(21,30):
    # memeriksa apakah angka adalah genap
    if num % 2 == 0:
        # Jika angka genap, tambahkan ke dalam set nums
        nums.add(num)
print(nums)

# Apa Outputnya?

# Variable dengan nilai string
my_str = 'Python'
"""
Menggunakan operasi konkatenasi + untuk menggabungkan string dengan slicing string...
[2::2] artinya dimulai dari indeks 2 hingga akhir dengan langkah atau loncat 2...

"""
results = my_str + my_str[2::2]
print(results)

# Apa Outputnya?

# Mendefinisikan fungsi 'recurse' dengan dua parameter, 'n' dan 's'
def recurse (n,s):
    # Kondisional, jika 'n' sama dengan 0
    if n == 0:
        # Mencetak nilai 's' saat ini
        print(s)
    else:
        # Jika nilai 'n' tidak sama dengan 0, panggil diri sendiri dengan nilai 'n' dikurangi 1 dan 's' ditambah 'n'
        recurse(n-1, n+s)
# Penggunaan fungsi
recurse(3,0)

#Apa Outputnya?

# A. 6
# B. 5
# C. 3
# D. 2

# Fungsi segitiga dengan tiga parameter a,b dan c
def segitiga(a,b,c):
    # Memeriksa aturan sisi segitiga
    # A. Panjang sisi a + b harus lebih besar dari panjang sisi c
    # B. Panjang sisi b + a harus lebih besar dari panjang sisi c
    # C. Panjang sisi b + c harus lebih besar dari panjang sisi a
    # Jika terpenuhi segitiga terbentuk
    if a + b > c and b + a > c and b + c > a:
        # Cetak True 
        print(True)
    # Jika aturan sisi segitigatidak terpenuhi, segitiga tidak dapat dibentuk
    else:
        # Cetak False
        print(False)
# Penggunaan fungsi
segitiga(12,1,1)

#Apa Outputnya?

# A. True
# B. False
# C. None
# D. Error


def absolute_value(x):
    # Memeriksa apakah x kurang dari 0
    if x < 0 :
        # Jika x kurang dari 0, mengembalikan nilai x (mengembalikan nilai positif dari x)
        return x
    # Blok yang dijalankan jika x kurang dari 0
    else:
        # Jika x tidak kurang dari 0, mengembalikan nilai x ( tidak mengubah nilai)
        return x
# Penggunaan fungsi
print(absolute_value(-5))

#Apa Outputnya?

# A. 6
# B. -5
# C. 5
# D. 2

# Mendefinisikan fungsi absolute_value dengan satu parameter, yaitu a
def absolute_value(a):
    # Mengembalikan nilai absolute_value dari x menggunakan bulit in function abs()
    return abs(a)
# Penggunaan fungsi
print(absolute_value(-4))

#Apa Outputnya?

# A. 6
# B. -4
# C. 4
# D. 2

# Mendefinisikan fungsi absolute_value dengan satu parameter, yaitu c
def absolute_value(c):
    # Memeriksa apakah c kurang dari 0
    if c < 0:
        # Jika c kurang dari 0, maka mengembalikan nilai c (mengembalikan nilai positif dari c)
        return -c
    # Blok yang akan dijalankan jika c kurang dari 0 (tidak mengubah nilai)
    else:
        return c
# Penggunaan fungsi
print(absolute_value(-5))

#Apa Outputnya?

# A. 6
# B. 5
# C. -5
# D. 2

# Mendefinisikan fungsi compare dengan dua parameter, yaitu x dan y
def compare(x,y):
    # Memeriksa apakah x lebih besar dari y
    if x > y:
        # Jika x lebih besar dari y, maka mengembalikan nilai 1
        return 1
    # Blok dijalankan jika x tidak lebih besar dari y, tetapi x sama dengan y
    elif x == y:
        # Jika x sama dengan y, mengembalikan nilai 0
        return 0
    # Blok yang dijalankan jika x tidak lebih besar dari y, dan x tidak sama dengan y
    else:
        # Memeriksa apakah x lebih kecil dari y
        if x < y:
            # jika x lebih kecil dari y, maka mengembalikan nilai -1
            return -1
# Penggunaan fungsi
print(compare(-1,-2))

#Apa Outputnya?

# A. -1
# B. 1
# C. 0
# D. 2

# Mendefinisikan fungsi distance dengan empat parameter 
def distance(x1,y1,x2,y2):
    # Menghitung selisih antara x2 dan x1
    dx = x2 - x1
    # Menghitung selisih antara y2 dan y1
    dy = y2 - y1
    # Menghitung kuadarat jarak antara dua titik menggunakan pyhtgoras
    squared = dx**2 + dy**2
    # Mencetak nilai
    print("Kuadrat: ", squared)

# Penggunaan fungsi
distance(1,2,4,6)

#Apa Outputnya?

# A. 6
# B. 25
# C. 4
# D. 2

def distance(x1,y1,x2,y2):
    # Menghitung jaarak horizontal (dx) antara dua titik
    dx = x2 - x1
    # Menghitung jarak vertikal (dy) antara dua titik
    dy = y2 - y1
    # Menghitung jarak kuadrat (squared) menggunakan teorema pythagoras
    squared = dx**2 + dy**2
    # Menghitung jarak Euclidean dengan mengambil akar kuadrat dari jarak kuadrat
    result = math.sqrt(squared)
    # Menampilkan hasil
    return print("Hasil: ", result)
# Penggunaan fungsi
distance(1,2,4,6)

#Apa Outputnya?

# A. 6
# B. 5
# C. 5.0
# D. 2

# Fungsi untuk menghitung jarak antara dua titik (x1,y1) dan (x2,y2)
def distance(x1,y1,x2,y2):
    # Menggunakan rumus jarak Euclidean (pythagoras), untuk menghitung jarak
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
# Fungsi untuk mengitung luas lingkaran berdasarkan jari-jari
def area(radius):
    # Menggunakan rumus luas lingkaran pi * r^2
    return math.pi * radius**2
# Fungsi untuk menghitung luas lingkaran berdasarkan dua titik pusat (xc, yc) dan (xp, yp)
def circel_area(xc,yc,xp,yp):
    # Menggunakan fungsi distance untuk menghitung jari-jari lingkaran
    radius = distance(xc,yc,xp,yp)
    # Menggunakan fungsi area untuk menghitung luas lingkaran berdasarkan jari-jari
    result = area(radius)
    # Menampilkan hasil luas lingkaran
    return print("Hasil: ",result)
# Penggunaan fungsi
circel_area(1,2,3,4)

#Apa Outputnya?

# A. 26
# B. 25
# C. 25.132741228718352
# D. 2

# Fungsi is_between dengan tiga parameter
def is_between(x,y,z):
    # Mengembalikan True jika x kurang dari atau sama dengan y dan y kurang dari atau sama dengan z
    return x<=y<=z
# Penggunaan fungsi
print(is_between(1,1,1))

#Apa Outputnya?

# A. True
# B. 1
# C. False
# D. 3

# Fungsi rekrusif untuk menghitung faktorial dari suatu angka n
def factorial(n):
    # Basis dari rekurasi, jika n sama dengan 0, kembalikan 1 (0! = 1)
    if n == 0:
        return 1
    else:
        # Rekursi, panggil fungsi factorial dengan parameter (n-1)
        recurse = factorial(n-1)
        # Hitung hasil factorial dengan mengalikan n dengan hasil rekursi
        result = n * recurse
        # kembalikan hasil factorial
        return result
# Penggunaan fungsi
print("Hasil: ",factorial(3))

#Apa Outputnya?

# A. 6
# B. 1
# C. 2
# D. 3

# Fungsi rekursif untuk menghitung bilangan fibonancci ke-n
def fibonacci(n):
    # Basis rekursi, jika n sama dengan 0, kembalikan 0
    if n == 0:
        return 0
    # Basis rekursi, jika n sama dengan 1, kembalikan 1
    elif n == 1:
        return 1
    else:
        # Rekursi, jumlahkan dua panggilan rekursif sebelumnya untuk n-1 dan n-2
        return fibonacci(n-1) + fibonacci(n-2)
# Penggunaan fungsi
print(fibonacci(6))

#Apa Outputnya?

# A. 0
# B. 1
# C. 2
# D. 8

# Fungsi yang mengembalikan karakter pertama dari suatu string
def first(word):
    # Menggunakan indeks 0 untuk mengakses karakter pertama dari string
    return word[0]
# Penggunaan fungsi
print(first("Muhamad Zaki"))

#Apa Outputnya?

# A. M
# B. Z
# C. u
# D. i

# Fungsi yang mengembalikan karakter terakhir dari suatu string
def last(word):
    # Menggunakan indeks -1 untuk mengakses karakter terakhir dari string
    return word[-1]
# Penggunaan fungsi
print(last("Muhamad Zaki"))

#Apa Outputnya?

# A. M
# B. Z
# C. u
# D. i

# Fungsi yang mengembalikan bagian tengah dari suatu string
def middle(word):
    # Menggunakan slicing dengan indeks 1 hingga -1 untuk mendapatkan bagian tengah dari string
    return word[1:-1]
# Penggunaan fungsi
print(middle("Muhamad Zaki"))

#Apa Outputnya?

# A. Muhamad Zaki
# B. hamadZak
# C. dZ
# D. uhamad Zak

# Fungsi untuk mengecek apakah string merupakan palindrome atau bukan
def palindrome(middle):
    # Menggunakan slicing dengan indeks 1 hingga -1 untuk mendapatkan bagian tengah dari string
    return middle [1:-1]
# Penggunaan fungsi
print(palindrome("ab"))

#Apa Outputnya?

# A. ab
# B. 
# C. a
# D. b

def palindrome(middle):
    # Mengembalikan bagian dari string 'middle' dimulai dari indeks 1 hingga indeks terakhir -1
    return middle [1:-1]
# Penggunaan fungsi
print(palindrome(" "))

#Apa Outputnya?

# A. " "
# B. 
# C. Error
# D. 1

def is_palindrome(karakter):
    # Memeriksa apakah string 'karakter' sama ketika dibaca dari depan maupun dari belakang
    if karakter == karakter[::-1]:
        # Jika kondisinya di atas benar, mencetak True
        print (True)
    else:
        # Jika kondisi di atas salah, mencetak False
        print(False)
# Penggunaan fungsi
is_palindrome("radar")

#Apa Outputnya?

# A. False
# B. True
# C. Error
# D. 5


def is_palindrome(num):
    # Mengembalikan hasil perbandingan apakah isi dari 'num' sama saat dibaca dari depam maupun dari belakang
    return num == num[::-1]
# Penggunaan fungsi
print(is_palindrome([1,2,1]))

#Apa Outputnya?

# A. False
# B. True
# C. Error
# D. 4

# Mendefisikan variabel x dengan memberikan value 5
x = 5
# Mencetak value variable x
print(x)

#Apa Outputnya?

# A. False
# B. True
# C. 5.0
# D. 5

# Mendefisikan variabel x dengan memberikan value 7
x = 7
# Mencetak value variable x
print(x)

#Apa Outputnya?

# A. False
# B. True
# C. 7.0
# D. 7

# Mendefisikan variable a dan memerikan nilai 5
a = 5
# Mendefisikan variable b dan memberikan nilai sama seperti a
b = a
# Mengubah nilai variable a menjadi 3
a = 3
# mencetak nilai variable a
print(a)

#Apa Outputnya?

# A. False
# B. True
# C. 3
# D. 5

# Mendefisikan variable x dan memberikan nilai 4
x = 4
# Menambah 1 ke nilai variable x
x = x + 1
# Mengganti nilai variable x dengan 2
x = 2
# mencetak nilai variable x
print(x)

#Apa Outputnya?

# A. Error
# B. 2
# C. 4
# D. 5

# Mendefisikan variable x dan memberikan nilai 0
x = 0
# Menambah 1 ke nilai variable x
x = x + 1
# Mencetak nilai variable x
print(x)

#Apa Outputnya?

# A. 1 kenaikan
# B. 2
# C. 4
# D. 5

# Mendefisikan variable x dan memebrikan nilai 0
x = 0
# Mengurangi 1 nilai variable x
x = x - 1
# Mencetak nilai variable x
print(x)

#Apa Outputnya?

# A. 1
# B. -1 penurunan
# C. 4
# D. 5

def countdown(n):
    # Memulai loop while yang akan berjalan selama nilai n lebih besar dari 0
    while n > 0:
        # Mencetak nilai n
        print(n)
        # Mengurangi nilai n sebesar 1
        n = n - 1
        # Mencetak teks 'Meledak!'
        print("Meledak!")
# Penggunaan fungsi
countdown(1)

#Apa Outputnya?

# A. 1
# B. -1
# C. Meledak!
# D. 0

def sequence(n):
    # Memulai loop while yang akan berjaln selama n tidak sama dengan 1
    while n != 1:
        # Mencetak nilai n
        print(n)
        # Memerikasa apakah n adalah bilangan genap
        if n % 2 == 0:
            # Jika genap, bagi n dengan 2
            n = n / 2
        else:
            # Jika ganjil, lakukan operasi n * 3 + 1
            n - n * 3 + 1
# Penggunaan fungsi
sequence(2)

#Apa Outputnya?

# A. 1
# B. -1
# C. 2
# D. 0

#while True:
    #line = input("Ketik: ")
    #if line == 'done':
        #break
    #print(line)

#Apa Outputnya?

# A. done
# B. loop
# C. Error
# D. None

# Mendefisikan variable x dan memebrikan nilai 4
x = 4
# Mendefisikan variable a dan memberikan nilai 2
a = 2
# While loop yang akan terus berjalan
while True:
    # Mencetak nilai variable x
    print(x)
    # Menghitung nilai baru y berdasarkan rumus metode newthon raphson
    y = int((x + a / x) / 2)
    # Memeriksa apakah nilai y sama dengan nilai x
    if y == x: 
        # Jika ya, keluar dari loop
        break
    # Menetapkan nilai x menjadi nilai y untuk iterasi selanjutnya
    x = y
#Apa Outputnya?

# A. 4
# B. 2
# C. 1
# D. Semua benar!

# Mendefinisikan variable fruit dan memberikan nilai string 'Banana'
fruit = "Banana"
# Mengaksek karakter pertama dari string 'fruit' dan menyinpan dalam variable letter
letter = fruit [0]
# Mencetak nilai variable 'letter'
print(letter)

#Apa Outputnya?

# A. Banana
# B. B
# C. a
# D. n

# Mendefinisikan variable 'fruit' dan memberikan nilai string 'Banana'
fruit = "Banana"
# Mengaksek karakter kedua dari string 'fruit' (indeks 1), dan menyimpan dalam variabel 'i'
i = fruit[1]
# Membuat list baru yang berisi nilai dari variable 'i'
result = [i]
# Mencetak nilai dari variable 'result
print(result)

#Apa Outputnya?

# A. Banana
# B. B
# C. a
# D. n

# Mendefiniksan variable 'fruit' dan memebrikan nilai string
fruit = "Banana"
# Menghitung panjang (jumlah karakter) dari string 'fruit' dan menyimpan dalam variable 'result'
result = len(fruit)
# Mencetak nilai dari variable result
print(result)

#Apa Outputnya?

# A. 6
# B. B
# C. a
# D. n

# Mendefiniksan variable 'fruit' dan memebrikan nilai string
fruit = "Banana"
# Menghitung panjang (jumlah karakter) dari string 'fruit' dan menyimpan dalam variable 'length'
length = len(fruit)
# Mengaksek karakter terakhir dari strig 'fruit' dan menyimpan dalam variable 'lasts'
lasts = fruit[-1]
# mencetak panajang string dan karakter terakhit
print(length, lasts)

#Apa Outputnya?

# A. 6
# B. B
# C. a
# D. n

# Mendefinisikan variable 'fruit' dan memberikan nilai string
fruit = "Banana"
# Mendefinisikan variable index dan memberikan nilai 3
index = 3
# Memulai loop while dengan kondisi, selama nilai 'index' kurang dari panjang string 'fruit'
while index < len(fruit):
    # Mengakses karakter pada indeks 'index' dari string 'fruit' dan menyimpan dalam variable 'letter'
    latter = fruit[index]
    # Mencetak nilai variable letter
    print(latter)
    # Menambahkan 1 ke nilai 'index' untuk beralih ke indeks berilitnya dalam iterasi selanjutnya
    index = index + 1

#Apa Outputnya?

# A. 6
# B. B
# C. ana
# D. n

# Mendefinisikan string "prefixes" yang berisi huruf-huruf 'JKLMNOPQ'
prefixes = "JKLMNOPQ"
# Mendefinisikan string "suffix" yang berisi 'ack'
suffix = 'ack'
# Melakukan iterasi pada setiap huruf dalam string "prefixes"
for latter in prefixes:
     # Mencetak gabungan antara huruf dan string "suffix"
    print(latter + suffix)

#Apa Outputnya?

# A. Jack, Kack, 
# B. Mack, Lack
# C. Nack, Oack
# D. Pack, Qack

def karakter(satu):
     # Memeriksa apakah parameter "satu" bernilai True (tidak kosong atau tidak None)
    if satu:
        # Mengambil substring dari "satu" dari indeks 0 hingga 3 (indeks ke-4) dan menyimpannya dalam variabel "dua"
        dua = satu [0:4]
        # Mencetak nilai dari variabel "dua"
        print(dua)
# Penggunaan fungsi
karakter("Ular Python")

#Apa Outputnya?

# A. Ular 
# B. Python
# C. Ular Python
# D. Semua benar!

def karakter(tiga):
     # Memeriksa apakah parameter "tiga" bernilai True (tidak kosong atau tidak None)
    if tiga:
        # Mengambil substring dari "tiga" dari indeks 5 hingga 10 (indeks ke-11) dan menyimpannya dalam variabel "empat"
        empat = tiga [5:11]
        # Mencetak nilai dari variabel "empat"
        print(empat)
# Penggunaan fungsi
karakter("Ular Python")

#Apa Outputnya?

# A. Ular 
# B. Python
# C. Ular Python
# D. Semua benar!

def fruit(apel):
    # Memeriksa apakah parameter "apel" bernilai True (tidak kosong atau tidak None)
    if apel:
        # Mengambil substring dari "apel" mulai dari indeks 0 hingga indeks 2 (indeks ke-3) dan menyimpannya dalam variabel "result"
        result = apel[:3]
        # Mencetak nilai dari variabel "result"
        print(result)
# Penggunaan fungsi
fruit("Apel")

#Apa Outputnya?

# A. Apel 
# B. Ape
# C. l
# D. Semua benar!

def fruit(apel):
    # Memeriksa apakah parameter "apel" bernilai True (tidak kosong atau tidak None)
    if apel:
        # Mengambil substring dari "apel" mulai dari indeks 3 hingga akhir dan menyimpannya dalam variabel "result"
        result = apel[3:]
        # Mencetak nilai dari variabel "result"
        print(result)
# Penggunaan fungsi
fruit("Apel")

#Apa Outputnya?

# A. Apel 
# B. Ape
# C. l
# D. Semua benar!

def fruit(apel):
    # Memeriksa apakah parameter "apel" bernilai True (tidak kosong atau tidak None)
    if apel:
        # Mengambil substring dari "apel" mulai dari indeks 3 hingga (indeks 3 - 1), yang menghasilkan string kosong, dan menyimpannya dalam variabel "result"
        result = apel[3:3]
         # Mencetak nilai dari variabel "result"
        print(result)
# Penggunaan fungsi
fruit("Apel")

#Apa Outputnya?

# A. Apel 
# B. Ape
# C. l
# D. Empty string

def greeting(a):
    # Memeriksa apakah parameter "a" bernilai True (tidak kosong atau tidak None)
    if a:
        # Mengganti karakter pertama dalam string "a" dengan "M" dan menyimpannya dalam variabel "new_greeting"
        new_gretting = "M" + a[1:]
        # Mencetak nilai dari variabel "new_greeting"
        print(new_gretting)
# Penggunaan fungsi
greeting("Hallo, Tante Panas!")

#Apa Outputnya?

# A. Hallo, Tante Panas!
# B. H
# C. a
# D. Mallo, Tante Panas!

def find(word, letter,):
    # Inisialisasi variabel "index" dengan nilai 0
    index = 0
    # Memulai loop while untuk iterasi melalui setiap karakter dalam string "word"
    while index < len(word):
        # Memeriksa apakah karakter pada indeks "index" sama dengan karakter "letter"
        if word[index] == letter:
            # Jika ya, kembalikan nilai indeks
            return index
        # Jika tidak, tambahkan 1 ke nilai "index" untuk beralih ke karakter berikutnya
        index += 1
    # Jika tidak ada karakter yang sesuai, kembalikan nilai -1
    return -1
# Penggunaan fungsi
print(find("Zaki", "Zaki"))

#Apa Outputnya?

# A. Apa kabar!
# B. Surat
# C. None
# D. -1

# Mendfinisikan fungsi 'find' untuk mencari indeks pertama kemunculan suatu karakter dalam sebuah kata
def find(word, letter, s_index=0):
    # Inisialisasi variable 'index' dengan nilai awal s_index
    index = s_index
    # Loop 'while' untuk iterasi melalui karakter dalam kata 'word'
    while index < len(word):
        # Kondisional, jika karakter saat ini sama dengan karakter yang dicari 'letter'
        if word[index] == letter:
            # Mengembalikan indeks pertama kemunculan karakter yang dicari
            return index
        # Peningkatan nilai 'index' untuk melanjutkan pencarian
        index += 1
    # mengembalikan - 1 jika karakter tidak ditemukan dalam kata 'word'
    return - 1
# Penggunaan fungsi
print(find("Tangan Zaki", "k", 2))

#Apa Outputnya?

# A. 0
# B. 2
# C. 9
# D. -1

# Mendefinisikan fungsi 'fruit' untuk menghitung jumlah kemunculan karakter 'a' dalam seuah kata
def fruit(word, count= 0):
    # Loop untuk iterasi melalui setiap karakter dalam kata 'word'
    for letter in word:
        # Kondisional, jika karakter saat ini sama dengan karakter 'a'
        if letter == "a":
            # Tambahkan 1 ke jumlah kemunculan karakter 'a'
            count = count + 1
            # Cetak jumlah kemunculan karakter 'a' saat ini
            print(count)
# Penggunaan fungsi    
fruit("Banana", 0)

#Apa Outputnya?

# A. 0
# B. Banana
# C. 2
# D. 3

# Mendefinisikan fungsi 'couse' untuk menghitung jumlah kemunculan suatu karakter dalam sebuah kata
def cous(word, karakter):
    # Inisialisasi variable hitung untuk menyimpan jumlah kemunculan karakter
    hitung = 0
    # Loop untuk iterasi melalui setiap karakter dalam kata 'word'
    for char in word:
        # Kondisional, jika karakter saat ini sama dengan karakter yang dicari
        if char == karakter:
            # Jika karakter ditemukan, tambah jumlah kemunculan
            hitung +=1
            # Kembalikan jumlah kemunculan saat ini
    if hitung > 0:
        # Mengembalikan jumlah kemunculan karakter jika lebih dari 0
        return hitung
    else:
        # Mengembalikan - 1 jika karakter tidak ditemukan sama sekali
        return -1
# Penggunaan fungsi   
print('Hasil = ', cous("Mendesah",'e'))

#Apa Outputnya?

# A. 3
# B. 1
# C. 2
# D. Kosong sayang

def hitung (text, karakter):
    count = 0
    s_index = 0
    while True:
        index = find(text, karakter, s_index)
        if index == -1:
            break
        count +=1
        s_index = index + 1
    return count

def find (word, alfa, s_index = 0):
    index = s_index
    while index < len(word):
        if word[index] == alfa:
            return index
        index += 1
    return -1

text = "Apa kabar!"
char_count = "a"
result = hitung(text, char_count)

text = "Apa kabar!"
char_to_count = "a"
result = hitung(text, char_to_count)
print(f"Jumlah karakter '{char_to_count}' dalam teks adalah {result}")
#Apa Outputnya?

# A. Jumlah karakter 'a' dalam teks adalah 1
# B. Jumlah karakter 'a' dalam teks adalah 4
# C. Jumlah karakter 'a' dalam teks adalah 2
# D. Jumlah karakter 'a' dalam teks adalah 3

def fruit(banana):
    # Pengecekan kebenaran (truthiness) dari string banana
    if banana:
        # Jika string banan tidak kosong, ubah semua huruf menjadi huruf besar
        satu = banana.upper()
        # Cetak string yang sudah diubah ke huruf besar
        print(satu)
# Penggunaan fungsi
fruit("banana")
#Apa Outputnya?

# A. Banana
# B. BANANA
# C. banana
# D. none

def fruit(find):
    # Pengecekan kebenaran (truthiness) dari string find
    if find:
        # Jika string find tidak kosong, cari indeks pertama karakter 'a' dalam find
        satu = find.find("a")
        # Cetak indeks pertama 'a' jika ditemukan
        print(satu)
    # Mengembalikan nilai -1 jika string find kosong atau 'a' tidak ditemukan
    return -1
# Penggunaan fungsi
fruit("Banana")

#Apa Outputnya?

# A. Banana
# B. 4
# C. None
# D. 1

def find(fruit):
    # Pengecekan kebenaran (truthiness) dari string fruit
    if fruit:
        # Jika string fruit tidak kosong, cari indeks pertama karekter 'a' dalam fruit
        satu = fruit.find('a')
        # cetak indeks pertama 'a' jika ditemukan
        print(satu)
    # Mengembalikan nilai -1 jika string fruit kosong atau 'a' tidak ditemukan
    return -1
# Penggunaan fungsi
find("pel")

#Apa Outputnya?

# A. 2
# B. 1
# C. pel
# D. -1

def fruit(find):
    # Pengecekan kebenaran (truthiness) dari string find
    if find:
        # Jika string find tidak kosong, cari index pertama substring 'na' dalam find
        satu = find.find("na")
        # Cetak indeks pertama 'na' jika ditemukan
        print(satu)
    # Mengembalikan nilai -1, jika string find kosong atau 'na' tidak ditemukan
    return -1
# Penggunaan fungsi
fruit("Banana")

#Apa Outputnya?

# A. Banana
# B. 4
# C. 2
# D. 1

# Inisialisasi vaeiable atau mendfisinikan variable dan memberikan nilai
word = "banana"
# Pencarian substring
new_word = word.find("na", 3)
print(new_word)

#Apa Outputnya?

# A. 0
# B. 4
# C. 2
# D. 1

#name = "jilbobs"
#new_name = name.find(b, 1, 2)
#print(new_name)

#Apa Outputnya?

# A. error
# B. Jilbobs
# C. 2
# D. 1

def fruit(banana1, banana2):
    # Pengecekan keberadaan huruf 'a' dalam banana1
    if "a" in banana1:
        print(True)
    else:
        print(False)
    # Pengecekan keberadaan huruf 'd' dalam banana2
    if "d" in banana2:
        print(True)
    else:
        print(False)
# Penggunaan fungsi
fruit("banana", "banana")
#Apa Outputnya?

# A. True
# B. False
# C. A & B benar
# D. None

def in_both(fruit1, fruit2):
    # Iterasi melalui setiap huruf dalam fruit1
    for letter in fruit1:
        # Memeriksa apakah huruf tersebut juga ada dalam fruit2
        if letter in fruit2:
            # Jika ada maka huruf tersebut dicetak
            print(letter)
# Penggunaan fungsi
in_both("apples", "oranges")

#Apa Outputnya?

# A. a
# B. e
# C. s
# D. Semua benar!

def fruit(fruit1):
    # Pengecekan jenis buah
    if fruit1 == "banana":
        print("All right, bananas")
    else:
        print("Not a bananas")
    # Pengecekan urutan alfabet
    if fruit1 < "banana":
        print("Your word, ' + fruit1 + ', comes before banana.")
    elif fruit1 > "banana":
        print("Your word, ' + fruit1 + ', comes after banana.")
    else:
        print("All right, bananas")
# Penggunaan fungsi
fruit("banana")

#Apa Outputnya?

# A. All right, bananas
# B. All right, bananas
# C. Error
# D. A & B benar!

def is_reverse(word1,word2):
    # Memeriksa apakah panjang kedua kata sama
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2) -1

    # Membandingkan karakter dari kedua kata
    while j > 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    # Mengmbalikan True, jika kata merupakan kebalikan satu sama lain
    return True
# Penggunaan fungsi
result = is_reverse("pots", "stop")
print(result)

#Apa Outputnya?

# A. True
# B. False
# C. Error
# D. A & B benar!

print('\n')

def reads(file_name, encoding='utf-8'):
    try:
        # Membuka file dengan menentukan encoding
        with open(file_name, encoding=encoding) as find:
            # Membaca baris pertama dari file
            line = find.readline()
            # Menghapus karakter whitespace (seperti newline) di awal dan akhir baris
            word = line.strip()
            # Mengembalikan text dari baris pertama
            return word
        
    except FileNotFoundError:
        # Menangani kasus jika file tidak ditemukan
        return f'File {file_name} tidak ditemukan!'
    
    except UnicodeEncodeError:
        # Menangani kesalahan encoding jika encoding salah
        return f'Gagal mendecode {file_name},karena menggunakan encoding yang salah!'
    
    except Exception as z:
        # Meneangani kesalahan umum lainnya
        return f'Terjadi kesalahan! {z}'
# Penggunaan fungsi
print(reads(file_name = 'satu.txt'))

#Apa Outputnya?


print('\n')

def new_reads (data, encoding = 'utf-8'):
    # Membuka file dengan nama yang diberikan dalam metode 'r', dengan ecoding yang diberikan
    pin = open(data, encoding=encoding)
    # Iterasi melalui setiap baris dalam file
    for line in pin:
        # Menghapus karakter whitespace di awal dan akhir setiap baris, kemudian menyimpan dalam variable word
        word = line.strip()
        # Menampilkan setiap baris yang telah distrip ke layar
        print(word)
# Penggunaan fungsi
new_reads(data ='satu.txt')

#Apa Outputnya?


print('\n')

def reads_one(datas):
    try:
        # Membuka file dengan nama yang diberikan dalam parameter'datas'
        with open(datas, encoding='utf-8') as files:
            # Membuat list kosong untuk menyimpan kata-kata yang memiliki panjang lebih dari atau sama dengan 20 karakter
            long_words = []
            # Iterasi melalui setiap baris dalam file
            for line in files:
                # Menghilangkan karakter whitespace dan memisahakn kata-kata dalam satu baris
                words = line.strip().split()
                # Menambahkan-kata-kata yang memiliki panjang lebih dari atau sama dengan 20 karakter, ke dalam list 'long_words'
                long_words.extend([word for word in words if len(word) >= 20])
            # Mengembalikan list 'long_words yang berisi kata-kata dengan panjang lebih dari atau sama dengan 20 karakter
            return long_words
    # Menangkap ekspresi (Exception) jila file tidak ditemukan
    except FileNotFoundError:
        # Mengembalikan pesan kesalahn beserta informasi 
        return f'File {datas} File tidak ditemukan!'
    # Menangkap ekpresi (Exception) jika terjadi kesalahan saat membuka atau membaca file
    except Exception as no:
        # Mengembalikan pesan kesalahn berupa informasi
        return f'{no}, Invalid!'
# Penggunaan fungsi
print(reads_one('satu.txt'))

#Apa Outputnya?


# Membaca isi berkas dan mengembalikan list kata-kata yang tidak mengandung huruf 'e'.
def has_no_e(datas, encoding='utf-8'):
    try:
        # Mencoba membuka files menggunakan enkoding yang ditentukan.
        with open(datas, encoding=encoding) as files:
            # Inisialisasi list kosong untuk menyimpan kata-kata tanpa huruf 'e'.
            no_e  =[]
             # Iterasi melalui setiap baris dalam files.
            for line in files:
                 # Menghilangkan spasi di awal dan akhir, kemudian membagi baris menjadi kata-kata.
                words = line.strip().split()
                # Menambahkan kata-kata tanpa huruf 'e' ke dalam list no_e.
                no_e.extend([word for word in words if 'e' not in word])
            # Mengembalikan list kata-kata tanpa 'e'.
            return no_e
    # Menangani UnicodeEncodeError, yang terjadi ketika ada masalah dengan enkoding yang ditentukan.
    except UnicodeEncodeError:
        return f'{datas}, menggunakan encoding yang salah!'
     # Menangani pengecualian lainnya.
    except Exception as no:
        return f'{no} Invalid!'
# Penggunaan fungsi
print(has_no_e(datas='satu.txt'))

#Apa Outputnya?

"""
def avoids(word, forbidden_word):
    return not any(letter in forbidden_word for letter in word)

def main():
    forbidden_word = input('Masukan kata terlarang, tanpa sepasi = ')
    with open('dua.txt', 'r', encoding = 'utf-8') as files:
        words = files.read().strip().split()
        without_forbidden_words = [word for word in words if avoids(word,forbidden_word)]
        print(f'Jmlah kata tidak terlarang = {without_forbidden_words}, {len(without_forbidden_words)}')
if __name__ == '__main__':
    main()

# Apa Outputnya?


def avoids(word, forbidden_words):
    #Mengembalikan True jika kata tidak mengandung huruf terlarang
    return not any(letter in forbidden_words for letter in word)

def main():
    #Meminta pengguna untuk memasukan huruf terlarang tanpa sepasi
    forbidden_words = input("Masukkan huruf terlarang (tanpa spasi): ")
    #Membuka file 'more.txt' dengan mode baca ('r') dan menggunakan encoding utf-8
    with open('dua.txt', 'r', encoding='utf-8') as files:
        # Membaca isi file, menghapus whitespace di kedua ujungnya, dan memisahkan kata-kata menjadi list
        words = files.read().strip().split()
    #Menggunakan list comprehension untuk membuat list kata tanpa huruf terlarang
    words_without_forbidden_words = [word for word in words if avoids(word, forbidden_words)]
    #Mencetak jumlah kata tanpa huruf terlarang
    print(f"Huruf terlarang: {words_without_forbidden_words}, Jumlah = {len(words_without_forbidden_words)}")
#Program utama
if __name__ == "__main__":
    main()

#Apa Outputnya?
"""

def uses_only(words, letters):
    # Memeriksa apakah semua huruf dalam 'words' ada dalam string 'letters'
    try:
        return all(letter in letters for letter in words)
    # Menangani TypeError jika input bukan string
    except TypeError:
        print('Invalid! Masukan tipe string!')


# Blok utama
try:
    # Mendefinisikan variable dengan nilai string
    word_contents= 'Muhamad Zaki'
    # Casefold mencegah case sensitif ya mamas gemoi
    letter_contents='Acefhlo'
    
    # Memeriksa apakah fungsi mengembalikan True dan False
    if uses_only(word_contents, letter_contents.casefold().strip()):
        print(f' Kalimat {word_contents}, hanya menggunakan huruf {letter_contents}')
    else:
        print(f' Kalimat {word_contents}, tidak menggunakan huruf {letter_contents}')
# Menangani segala pengecualian yang mungkin terjadi
except Exception as n:
    print(f'Terjadi kesalahan! {n}')
# Blok lain untuk pengujian yang berbeda
try:
    # Mendefinisikan variable dengan nilai string
    another_letters = 'aceofhello'
    # memeriksa apakah fungsi mengembalikan True dan False (baru)
    if uses_only(another_letters, letter_contents.casefold().strip()):
        print(f' Kalimat {another_letters}, hanya menggunakan huruf {letter_contents}')
    else:
        print(f' Kalimat {another_letters}, tidak menggunakan huruf {letter_contents}')
# Menangani segala pengecualian yang mungkin terjadi
except Exception as n:
    print(f'Terjadi kesalahan! {n}')

# Apa Outputnya?

def uses_all(words,required_letters):
    # Menggunakan blok try-except untuk menangani potensi TypeError (misalnya, jika words tidak dapat di-iterasi).
    try:
         # Menggunakan fungsi all() untuk memeriksa apakah semua huruf dalam required_letters ada di dalam string words.
        return all(letter in required_letters for letter in words)
    except TypeError:
        return False
# Mendefinisian variable bernilai string, contoh berisi vokal
example_words = 'aeiouy'
# Mendefinisikan dua variable bernilai string, untuk pengujian
vokal_ones = 'aeiou'
vokal_twos = 'aeiouy'
try:
    # Memanggil fungsi use_all dengan example_words, vokal_ones dan menyimpan hasilnya di result_ones
    result_ones = uses_all(example_words, vokal_ones)
    print(f'Apakah kata {example_words}, menggunakan huruf {vokal_ones} = {result_ones}')
    # Memanggil fungsi use_all dengan example_words, vokal_twos dan menyimpan hasilnya di result_twos
    result_twos = uses_all(example_words, vokal_twos)
    print(f'Apakah kata {example_words}, menggunakan huruf {vokal_twos} = {result_twos} ')
# Menangani segala jenis kesalahan yang mungkin terjadi
except Exception as n:
    print(f'Terjadi kesalahan!{n}')

# Apa Outputnya?
    
def is_abecedarian(word):
    """
    Fungsi untuk memeriksa apakah huruf-huruf dalam sebuah kata muncul dalam urutan abjad.
    Menangani kemungkinan kesalahan jika input tidak dapat diurutkan.
    """
    try:
        # Menggunakan sorted() untuk mengurutkan huruf-huruf dalam kata dan membandingkannya dengan kata asli.
        return word == ''.join(sorted(word))
    except TypeError:
        # Menangani TypeError jika input tidak dapat diurutkan (bukan string).
        print(f"Kesalahan: Input {word} tidak dapat diurutkan.")
        return False

def count_abecedarian_words(word_list):
    """
    Fungsi untuk menghitung jumlah kata abecedarian dalam sebuah daftar kata.
    """
    # Menggunakan list comprehension untuk memfilter kata-kata yang bersifat abecedarian.
    abecedarian_words = [word for word in word_list if is_abecedarian(word)]
    
    # Mengembalikan jumlah kata abecedarian dan daftar kata-kata tersebut.
    return len(abecedarian_words), abecedarian_words

# Daftar kata untuk diuji
word_list = ["abc", "hello", "aberration", "alphabet", "ace", "aab", "xyz", 123]

try:
    # Memanggil fungsi count_abecedarian_words untuk mendapatkan hasil.
    num_abecedarian, abecedarian_list = count_abecedarian_words(word_list)

    # Mencetak hasil
    print(f"Jumlah kata abecedarian: {num_abecedarian}")
    print(f"Kata-kata abecedarian: {abecedarian_list}")

except Exception as e:
    # Menangkap exception apapun yang mungkin terjadi selama eksekusi.
    print(f"Terjadi kesalahan: {e}")

# Apa Outputnya?
    
def has_no_e(word):

    for letter in word:
        if letter == 'e':
            return True
    return False

print(has_no_e('a'))

# Apa Outputnya?

def avoids(words, forbiddens):
    for letter in words:
        if letter == forbiddens:
            return False
    return True
print(avoids('e', 'e'))

# Apa Outputnya?

def uses_only(words,avaible):
    for letter in words:
        if letter not in avaible:
            return False
    return True
print(uses_only('c', 'b'))

# Apa Outputnya?

def user_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

# Apa Outputnya?

def is_abecedarian(word):
    # Menginisialisasi variable 'previous' dengan karakter pertama dari word atau list
    previous = word[0]
    # Melakukan iterasi melalui karakter-karakter dari indeks kedua hingga akhir dari word atau list
    for letter in word[1:]:
        # Memeriksa apakah karakter saat ini kurang dari karakter sebelumnya
        if letter < previous:
            # Jika iya, mengambalikan False, karena tidak dalam urutan abjad
            return False
        # Memperbarui 'previous' dengan karakter saat ini untuk digunakan pada iterasi berikutnya
        previous = letter
    # Jika semua karakter telah diperiksa dan tidak ada yang melanggar aturan, mengembalikan True
    return True
# Penggunaan fungsi
print(is_abecedarian([1,2,3,4,5]))

# Apa Outputnya?

def is_abecedarian(word):
    # Jika panjang word atau list kurang dari atau sama dengan 1, itu sudah benar secara abjad
    if len(word) <=1:
        return True
    # Memeriksa apakah karakter pertama lebih besar dari karakter kedua
    if word[0] > word[1]:
        return False
    # Memanggil fungsi is_abecedarian secara rekursif dangan memotong karakter pertama dari word atau list
    return is_abecedarian(word[1:])
# Pengguaan fungsi
print(is_abecedarian([1,2,3,4,5]))

# Apa Outputnya?

def is_abecedarian(word):
    # Inisialisasi variable i sebagai indeks awal
    i = 0
    # Selama i kurang dari panjang word dikurangi 1
    while i < len(word)-1:
        # Memeriksa apakah karakter berikutnya lebih kecil dari karakter saat ini
        if word[i+1] < word[i]:
            return False
        # Memperbarui nilai i, untuk melanjutkan ke karakter berikutnya
        i = i+1
    return True
# Penggunaan fungsi
print(is_abecedarian([1,2,3,4,5]))

# Apa outputnya?

def is_palindrome(word):
    # Inisialisasi dua indeks i dan j
    i = 0
    j = len(word)-1
    """
    Iterasi, selama i kurang dari j (belum mencapai pertengahan atau lebih)...
    dilakukan perbandingan karakter dari kedua ujung word atau list

    """
    
    while i<j:
        if word[i] != word[j]:
            return False
        # Memperbarui nilai i dan j untuk melanjutkan ke karakter sebelumnya
        i = i+1
        j = j-1
    return True
# Penggunaan fungsi
print(is_palindrome([1,2,3,4,5]))

# Apa Outputnya?

def is_reverse(word1, word2):
    # Memeriksa apakah panjang kedua word atau list sama
    if len(word1) != len(word2):
        return False
    
    # Memeriksa apakah setiap karakter pada posisi yang sesuai sama dalam urutan terbalik
    for i in range(len(word1)):
        if word1[i] != word2[len(word2) -1 - i]:
            return False
    
    # Jika semua karakter cocok, mengembalikan True
    return True

def is_palindrome(word):
    # Memanggil fungsi is_reverse dengan dua parameter yang sama
    return is_reverse(word, word)

# Penggunaan fungsi
print(is_palindrome(['radar']))

# Apa Outputnya?

# Membuat list yang berisi elemen
list_satu = [10,20,30,40]
print(list_satu)

# Apa Outputnya?

# Membuat list yang berisi elemen
list_dua = ['crunchy frog', 'ram bladder', 'lark vomit']
print(list_dua)

# Apa Outputnya?

# membuat list yang berisi elemen
list_nested = ['spam', 2.0, 5, [10,20]]
print(list_nested)

# Apa Outputnya?

# membuat list dengan elemen
list_str = ['Cheddar', 'Edam', 'Gouda']
list_nums = [42, 123]
# membuat list kosong
list_empty = []
print(list_str, list_nums, list_empty)

# Apa Outputnya?

# Membuat list yang berisi elemen
list_str = ['cheddar', 'kiw-kiw']
# Mengakses indeks ke 1 dari list_str dan menyimpan dalam variable resuluts
results = list_str[1]
print(results)

# Membuat list, yang berisi elemen
nums = [42, 123]
# Mengubah nilai elemen ke 1 dari nums menjadi nilai 5
nums[1] = 5
print(nums)

# Apa Outputnya?

# Membuat tuple, yang berisi elemen dan list sebagai elemen keempat
my_tuple = (1, 2, 3, ['a', 'b'])
"""
Mengakses elemen ke 3 dari my_tuple..
Mengakses elemen pertama dari list yang ada di dalam tuple...
Mengganti nilai elemen tersebut dengan c

"""
# Mengubah elemen pertama dari elemen keempat tuple menjadi 'c'
my_tuple[3][0] = 'c'  
print(my_tuple)

# Apa Outputnya?

# Mendefinisikan fungsi keju yang menerima satu parameter bernama item
def keju(item):
    # Menggunakan variable lokal item untuk menyimpan nilai parameter yang diterima oleh fungsi
    items = item
    # Itersi melalui setiap elemen dalam parameter item
    for item in items:
        # Mencetan setiap elemen
        print(item)
# Memanggil fungsi keju dengan sebuah list sebagai argumen
keju([1,2,3])

# Mendefinisikan fungsi keju yang menerima satu parameter bernama nums
def keju(nums):
    # Itersi melalui setiap indeks dalam range panjang dari nums
    for items in range(len(nums)):
        # Menggandakan setiap elemen nums pada indeks tertentu
        nums[items] = nums[items] * 2
    # Mengembalikan list yang sudah dimodifikasi
    return nums
# Memenggil fungsi keju dengan sebuah list sebagai argumen dan mencetak hasilnya
print(keju([1,2,3]))

# Mendefinisikan fungsi bernama list yang menerima satu parameter bernama isi
def daftar(isi):
    # Mengembalikan panjang dari list yang diterima
    return len(isi)
# Memanggil fungsi daftar dengan sebuah daftar sebagai argumen dan mencetak hasilnya.
print(daftar(['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
))

# Apa Outputnya?

# Membuat sebuah list nums1 dengan tiga elemen
nums1 = [1,2,3]
# Membuat sebuah list nums2 dengan tiga elemen
nums2 = [4,5,6]
# Menggabungkan dua list nums1 dan nums2 menjadi sebuah list baru dan menyimpan dalam variable results
results = nums1 + nums2
print(results)

# Apa Outputnya?

# Membuat sebuah list nums yang terdiri dari empat elemen yang diulangi sebanyak 4 kali
nums = [0] * 4
print(nums)

# Apa Outpunya?

# Membuat sebuah list nums yang berisi tiga elemen yang diulangi sebanyak 3 kali
nums = [1,2,3] * 3
print(nums)

# Apa Outputnya?

# membuat sebuah list dengan enem elemen
list_slices = ['a', 'b', 'c', 'd', 'e', 'f']
# Mengambil irisan dari indeks 1 hingga 2 dan menyimpan dalam variable results
results = list_slices[1:3]
print(results)

# Apa Outputnya?

# Membuat sebuh list dengan enam elemen
list_slices = ['a', 'b', 'c', 'd', 'e', 'f']
# Mengambil irisan dari awal hingga indeks empat dan menyimpan dalam variale results
results = list_slices[:4]
print(results)

# Apa Outputnya?

# Membuat sebuh list dengan enam elemen
list_slices = ['a', 'b', 'c', 'd', 'e', 'f']
# Mengambil irisan dari indeks 3 hingga akhir dan menyimpan dalam variable results
results = list_slices[3:]
print(results)

# Apa outputnya?

# Membuat sebuh list dengan enam elemen
list_slices = ['a', 'b', 'c', 'd', 'e', 'f']
# Melakukan slicing pada list_slices dengan menggunakan seluruh rentang indeks...
# sehingga membuat salinan (copy) dari seluruh isi list
results = list_slices[:]
# Ini akan mencetak list baru dengan elemen yang sama dengan list_slices
print(results)

# Apa outputnya?

# Membuat sebuh list dengan enam elemen
list_slices = ['a', 'b', 'c', 'd', 'e', 'f']
# Mengganti elemen pada indeks 1 dan 2 (indeks 3 tidak termasuk) dari results dengan elemen 'x' dan 'y'
results[1:3] = ['x', 'y']
# Ini akan mencetak list baru dengan perubahan sesuai yang telah dijelaskan
print(results)

# Apa outputnya

# Membuat sebuh list dengan enam elemen
list_slices = ['a', 'b', 'c', 'd', 'e', 'f']
# Melakukan slicing pada list_slices dimulai...
# dari indeks 0 hingga akhir dengan langkah 2, sehingga menghasilkan elemen-elemen pada indeks genap
results = list_slices[0::2]
# Mencetak hasil slicing, yaitu elemen-elemen pada indeks genap dari list_slices
print(results)

# Apa outputnya?

# Membuat sebuah list kosong dan menyimpannya dalam variabel plus
plus = []
# Menambahkan elemen 'a' ke list plus menggunakan method append()
plus.append('a')
print(plus)

# Apa Outputnya?

# Membuat sebuah list kosong dan menyimpannya dalam variabel plus
plus = []
 # Membuat list plu_plus dengan elemen 'a', 'b', dan 'c'
plu_plus = ['a','b','c']
# Menggabungkan (menambahkan semua elemen) dari list plu_plus ke dalam list plus menggunakan method extend()
plus.extend(plu_plus)
print(plus)

# Apa Outputnya?

# Membuat list plus dengan elemen yang tidak berurutan
plus = [2,1,4,3,6,5,8,7,9]
# Mengurutkan elemen-elemen dalam list plus secara ascending menggunakan method sort()
plus.sort()
print(plus)

# Apa outputnya?

# Mendefinisikan fungsi bernama add_all yang menerima satu parameter, yaitu nums
def add_all(nums):
    # Mendeklarasikan variabel total dan menginisialisasinya dengan nilai 0
    total = 0
    # Melakukan iterasi melalui setiap elemen dalam nums
    for num in nums:
        # Menambahkan nilai setiap elemen ke variabel total
        total +=  num
        # Mengembalikan nilai total setelah iterasi selesai
    return total
print(add_all([5]))

# Apa outputnya?

# Membuat list count dengan elemen 1, 2, dan 3
count = [1,2,3]
# Menghitung jumlah (penjumlahan) seluruh elemen dalam list count menggunakan fungsi sum()
counts = sum(count)
print(counts)

# Apa Outputnya?

# Mendefinisikan fungsi bernama capitalize_all yang menerima satu parameter, yaitu nums
def capitalize_all(nums):
     # Membuat list kosong yang akan menyimpan hasil operasi capitalize
    results = []
    # Melakukan iterasi melalui setiap karakter dalam nums
    for num in nums:
        # Mengubah setiap karakter menjadi...
        # huruf kapital menggunakan method capitalize() dan menambahkannya ke dalam list results
        results.append(num.capitalize()) # upper()
    # Mengembalikan list results yang berisi karakter-karakter dari nums yang telah diubah menjadi huruf kapital
    return results
print(capitalize_all('zaki'))

# Apa Outputnya?

# Mendefinisikan fungsi bernama only_uppers yang menerima satu parameter, yaitu nums
def only_uppers(nums):
    # Membuat list kosong yang akan menyimpan karakter-karakter yang merupakan huruf kapital
    results = []
    # Melakukan iterasi melalui setiap karakter dalam nums
    for num in nums:
        # Memeriksa apakah karakter tersebut adalah huruf kapital
        if num.isupper():
            # Jika ya, maka karakter tersebut ditambahkan ke dalam list results
            results.append(num)
    # Mengembalikan list results yang berisi karakter-karakter dari nums yang merupakan huruf kapital
    return results
print(only_uppers('Zaki'))

# Apa Outputnya?

# Membuat sebuah list dengan tiga elemen
hapus = ['a', 'b', 'c']
# Menghapus elemen indeks 0 dari list
results = hapus.pop(0)
print(results)

# Apa Outputnya?

# Membuat sebuah list dengan tiga elemen
hapus = ['a', 'b', 'c']
# Menghapus elemen indeks dua dari list
hapus.pop(2)
print(hapus)

# Apa Outputnya?

# Membuat sebuah list dengan tiga elemen
hapus = ['a', 'b', 'c']
# Menghapus elemen indeks 1 dari list
del hapus[1]
print(hapus)

# Apa Outputnya?

# membuat sebuah list dengan enam elemen
hapus = ['a', 'b', 'c','d','e','f']
# Menghapus elemen dari indeks 1 hingga 4 dari list
del hapus[1:5]
print(hapus)

# Apa Outputnya?

# Membuat sebuah list dengan tiga elemen
hapus = ['a', 'b', 'c']
# Menghapus elemen atau 'a' dari list
hapus.remove('a')
print(hapus)

# Apa outputnya?

# String yang akan diubah menjadi list, dengan setiap karakter menjadi elemen dari list
karakters = 'spam'
# Mengonversi string 'karakter' menjadi list dengan setiap karakter sebagai elemen dari list
results = list(karakters)
print(results)

# Apa Outputnya?

# String yang akan dipisahkan, jika no ada argumen yang diberikan ke split(), string akan dipisahkan...
# berdasarkan spasi atau (karakter whitespace lainnya)
karakters = 'pining for the jords'
# Memsisahkan string 'karakter' berdasarkan spasi (karakter whitespace) dan menyimpan hasilnya dalam bentuk list
results = karakters.split()
print(results)

# Apa Outputnya?

# String yang akan dipisahkan berdasarkan pemisah yang telah ditentukan
karakters = 'spam-spam-spam'
# String yang akan digunakan sebagai pemisah untuk memisahkan potongan-potongan string
pembatas = '-'
# Memisahkan string 'karakter' berdasarkan 'pembatas' dan menyimpan hasilnya dalam bentuk list
results = karakters.split(pembatas)
print(results)

# Apa Outputnya?

# Menyimpan string yang akan dipecah menjadi potongan-potongan
karakters = 'pining for the jords'
# Menyimpan string yang akan digunakan sebagai pembatas antara potongan-potongan
pembatas = ' '
# Menggabungkan  potongan-potongan string menggunakan pembatas yang telah ditentukan
results = pembatas.join(karakters)
print(results)

# Apa Outputnya?

"""
Di Python saat Anda menggunakan == operator, Anda menguji identitas objek berdasarkan nilainya.
Saat Anda menggunakan is operator, Anda sedang menguji identitas objek.

Jadi secara konseptual, value objectsdigunakan seolah-olah mereka adalah nilai...
namun secara teknis mereka masih berupa objek dan ada baiknya mengingat perbedaan tersebut.
"""
# Variable a dan b yang berisi nilai string
a = 'bananas'
b = 'bananas'
# Apakah kedua variable merujuk objek yang sama? Aku sarankan gunakan operator ==
c = a is b
print(c)

# Apa Outputnya?

# Variable a dengan nilai list yang berisi elemen
a = [1,2,3]
a = [1,2,3]
# Apakah variable merujuk objek yang sama
c = a is a
print(c)

# Apa Outputnya?


def delete_head(t):
    # Menghapus elemen pertama dari list
    del t[0]
# Insisialisasi list(elemen)
letters = ['a','b','c']
# Memanggil fungsi
delete_head(letters)
print(letters)

# Apa Outputnya?

# Membuat sebuah list dengan dua elemen, yang disipan di variable nums
nums = [1,2]
# Menambahkan satu elemen 3 ke list nums, menggunakan metode append() dan disimpan dalam variable results
results = nums.append(3)
# Metode append() dalam list tidak mengembalikan nilai yang dapat disimpan, sehingga hasilnya None
print(results)

# Apa Outputnya?

# Membuat sebuah list dengan dua elemen, yang disimpan di variable nums
nums = [1,2]
# Menambahkan elemen 3 ke list nums, menggunakan metode append() dan disimpan dalam variable results
results = nums.append(3)
# perubahan pada list, maka list nums akan mencangkup tiga elemen 1,2,3
print(nums)

# Apa Outputnya?

# membuat sebuah listt dengan 2 elemen dan disimpan pada variable nums
nums = [1,2]
# Menambahkan elemen 3 ke list nums menggunakan operator + dan hasilnya disimpan pada variable results
results = nums + [3]
# Menghasilkan list baru dengan tiga elemen, dan list asli (belum dimodifikasi) tidak berubah.
print(results)

# Apa Outputnya?

# Mendefinisikan sebuah fungsi yang menerima satu parameter
def bad_delete_head(nums):
    # Menghapus elemen partama dari list nums dan menetapkan hasilnya kembali ke variable nums...
    # (tetapi tidak mengubah list asli yang dilewati sebagai argumen)
    nums = nums[1:]
    # Membuat list baru yang disimpan pada variable num dengan empat elemen
    num = [1,2,3,4]
    # Mencetak isi list nums setelah penghapusan elemen pertama
    print(nums)
    # Mencetak isi dari list num
    print(num)
# Penggunaan fungsi dengan argumen
bad_delete_head([1,2,3])

# Apa Outputnya?

# Mendefinisikan sebuah fungsi yang bernama tail, mengembalikan list nums tanpa elemen pertamanya
def tail(nums):
    # Mengembalikan potongan list nums mulai dari indeks 1 hingga akhir...
    # yang menghasilkan list baru tanpa elemen pertama
    return nums[1:]
# Membuat list letters yang berisi tiga elemen (huruf)
letters = ['a','b','c']
# Memanggil fungsi tail dengan list letters sebagai argumen, dan hasilnya disimpan dalam variabel rests
rests = tail(letters)
# Mencetak nilai yang dikembalikan oleh fungsi tail...
# yaitu potongan list letters mulai dari indeks 1, sehingga mencetak list baru tanpa huruf 'a'
print(rests)

# Apa Outputnya?

# Mendefinisikan fungsi nums yang menerima satu parameter yaitu x
def nums(x):
    # Membuat list kosong yang akan menyimpan hasil
    t = []
    # Menambahkan semua elemen dari list x ke dalam list t menggunakan operator
    t += x
    # Mengembalikan list t yang sudah di isi dari elemen list x
    return t
# Penggunaan fungsi
print(nums([1,2,3]))

# Apa outputnya?

# Mendefinisikan fungsi nums yang menerima satu parameter yaitu x
def nums(x):
    # Membuat list kosong yang akan menyimpan hasil
    t = []
    # Menambahkan elemen x kedalam list t menggunakan metode append()
    t.append(x)
    # Mengembalikan list t yang telah di isi list x
    return t
print(nums([1,2,3]))

# Apa Outputnya?

# Mendefinisikan fungsi nums dengan satu parameter, yang dibuat defaultnya False
def nums(asli=False):
    # Mendfinisikan list asli dengan nilai default jika tidak diberikan argumen
    asli= [6,3,1,5,2,4]
    # Membuat salinan dari list asli untuk diurutkan nanti tanpa mempengaruhi list asli
    hasil_asli= asli[:]
    # Mengurutkan list haisl_asli secara ascending
    hasil_asli.sort()
    # Mencetak hasil yang telah diurutkan
    print(hasil_asli)
# Pneggunaan fungsi tanpa argumen
nums()

# Apa Outputnya?

# Mendefinisikan fungsi nested_sums dengan satu parameter services yang merupakan list...
# berisi list (nested list) dari angka
def nested_sums(services):
    # Inisialisasi list kosong results untuk menyimpan angka-angka yang memenuhi kondisi
    results = []
    # Inisialisasi variabel totals untuk menghitung total dari semua angka di dalam nested list
    totals = 0
    # Melakukan iterasi melalui setiap elemen di dalam list services
    for service in services:
        # Melakukan iterasi melalui setiap elemen di dalam nested list yang sedang diiterasi
        for subs in service:
            # Memeriksa apakah elemen tersebut merupakan bilangan genap
            if subs % 2 == 0:
                # Jika iya, tambahkan elemen tersebut ke dalam list results
                results.append(subs)
            # Menambahkan nilai elemen ke dalam total
            totals += subs
    # Mengembalikan list results dan total
    return results, totals
# Memanggil fungsi nested_sums dengan parameter sebuah nested list. Kemudian mencetak hasilnya
print(nested_sums([[1,2],[3],[4,5,6]]))

# Apa Outputnya?

def cumsum(services):
    # Inisialisasi list kosong untuk menyimpan hasil penjumlahan kumulatif
    results = []
    # Inisialisasi variabel totals untuk menyimpan total kumulatif sementara 
    totals = 0 
    # Melakukan iterasi dari 0 hingga panjang services - 1 
    for service in range(0, len(services)):  
        # Menambahkan nilai service saat ini ke totals
        totals += services[service]  
        # Menambahkan total kumulatif saat ini ke dalam list results
        results.append(totals)  
    # Mengembalikan list hasil penjumlahan kumulatif
    return results  

print(cumsum([1, 2, 3]))  # Memanggil fungsi cumsum dengan list [1, 2, 3] sebagai argumen

# Apa Outputnya?

def middle(services):
    # Inisialisasi list kosong untuk menyimpan hasil
    results = [] 
    # Melakukan iterasi pada setiap elemen dalam list services 
    for service in services:
        # Mengambil potongan dari indeks 1 hingga 2 dari list services  
        service = services[1:3]
        # Menambahkan potongan ke list results  
        results.append(service) 
        # Mengembalikan hasil setelah menambahkan potongan pertama, kemudian keluar dari fungsi 
        return results 
# Memanggil fungsi middle dengan list [1, 2, 3, 4] sebagai argumen 
print(middle([1, 2, 3, 4]))  

# Apa Outputnya?

def cohops(services):
    # Menghapus setiap elemen ketiga dari list services menggunakan slicing
    del services[0::3]
    # Mengembalikan list services yang sudah dimodifikasi
    return services  

# Memanggil fungsi cohop dengan list [1, 2, 3, 4] sebagai argumen
print(cohops([1, 2, 3, 4])) 

# Apa Outputnya?

# Mendefinisikan fungsi is_sorted dengan satu parameter, yaitu services (list)
def is_sorteds(services):
    # Mengurutkan list services dan menyimpannya dalam variabel service
    service = sorted(services)
    
    # Memeriksa apakah list asli sama dengan list yang telah diurutkan
    if services == service:
        # Jika kedua list sama, mengembalikan True
        return True
    else:
        # Jika kedua list tidak sama, mengembalikan False
        return False

# Contoh penggunaan fungsi
new1 = [1, 2, 2]
# new2 = ['b', 'a'] # Baris ini dikomentari karena tidak digunakan

# Memanggil fungsi is_sorted dengan list new1 sebagai argumen dan mencetak hasilnya
print(is_sorteds(new1))

# Apa Outputnya?

# Mendefinisikan fungsi untuk mengecek apakah dua kata adalah anagram
def is_angarams(permainan, kata):  
    # Mengurutkan huruf-huruf dalam kata permainan
    word = sorted(permainan) 
    # Mengurutkan huruf-huruf dalam kata
    words = sorted(kata)  
    # Membandingkan kata yang sudah diurutkan. Jika sama, maka kata-kata tersebut adalah anagram
    if word == words:  
        # Jika kata-kata adalah anagram, mencetak True
        print('True') 
    else:
        # Jika kata-kata bukan anagram, mencetak False
        print(False)  
# Memanggil fungsi is_angaram dengan kata-kata yang diberikan sebagai argumen
is_angarams('mycar','camry')  

# Apa Outptnya?

# Mendefinisikan fungsi untuk mengecek apakah dua kata adalah anagram
def is_anagrams(kata_satu, kata_dua):  

    # Mengubah kedua kata menjadi huruf kecil untuk memastikan pengecekan yang tidak peka terhadap huruf besar-kecil
    satu = kata_satu.lower()
    dua = kata_dua.lower()

    # Menghilangkan spasi di sekitar kata, jika ada, atau bisa menggunakan replace(" ", " ")
    tiga = satu.strip()
    empat = dua.strip()

    # Mengurutkan huruf-huruf dalam kata-kata untuk mempermudah perbandingan
    kata_sorted_satu = sorted(tiga)
    kata_sorted_dua = sorted(empat)

    # Membandingkan kedua kata yang sudah diurutkan. Jika sama, maka kata-kata tersebut adalah anagram
    if kata_sorted_satu == kata_sorted_dua:
        return True
    else:
        return False
# Memanggil fungsi is_anagrams dengan kata-kata yang diberikan sebagai argumen
print(is_anagrams('camry','mycar'))  

# Apa Outputnya?

def has_dulicates(lisa):
    # Buat elemen dari list untuk memmastikan list asli tidak dirubah
    copy_lisa = lisa[:]
    # Buat sebuah set untuk menyimpan elemen yang telah ditemui
    sets = set()
    # Melakukan iterasi melalui setiap elemen dalam list
    for elemen in copy_lisa:
        # Jika elemen sudah ada dalam set, berarti ada duplikat
        if elemen in sets:
            return True
        # Tambah elemen ke set
        sets.add(elemen)
    return False
print(has_dulicates([1,2,3,4,1])) # [1,2,3,4,5,6]

# Mengimpor modul random untuk menghasilkan angka acak
import random
# Mendefinisikan fungsi dengan satu parameter
def random_britdays(days): 
    # Inisialisasi list kosong untuk menyimpan dari britdays
    results = []
    # Melakukan iterasi sebanyak jumlah dari yang diminta
    for day in range(days):
        # Menghasilkan angka acak antara 1 dan 365(representasi hari dalam setahun)
        britdays = random.randint(1, 365)
        # Menambahkan britdays ke list
        results.append(britdays)
    # Mengembalikan list yang berisi britdays
    return results
# Penggunaan fungsi kiw-kiw
print(random_britdays(23))



def reads(file):
    try:
        # Membuka file dengan mode baca ('r') dan menggunakan encoding utf-8
        with open(file,'r', encoding='utf-8') as files:
            # Inisialisasi list kosong untuk menyimpan nama file
            file_names =[]
            # iterasi, melalui (membaca) setiap baris dalam file, satu persatu
            for line in files:
                # Membersihkan setiap baris dari spasi tambahan di awal dan akhir(whitespace),
                # kemudian membagi baris menjadi list kata-kata
                lines = line.strip().split()
                # Menambahkan semua kata dari baris saat ini ke dalam list file_names
                file_names += lines
            # Mengembalikan list yang berisi semua nama file yang berhasil dibaca dari file
            return file_names
    except Exception as no:
        # Mengembalikan pesan kesalahan jika terjadi kesalahan saat membaca file
        return f"{no} terjadi kesahalah!"
# Penggunaan fungsi
print(reads('tiga.txt'))

def reads(file):
    try:
        # Membuka file dengan mode baca ('r') dan menggunakan encoding utf-8
        with open(file,'r', encoding='utf-8') as files:
            # Inisialisasi list untuk menyimpan nama file
            file_names =[]
            # Iterasi melalui setiap baris dalam file
            for line in files:
                # Menghapus spasi tambahan di awal dan akhir baris,
                # kemudian membagi baris menjadi list kata-kata
                lines = line.strip().split()
                # Menambahkan list kata-kata dari baris saat ini ke dalam list file_names
                file_names.append(lines)
            # Mengembalikan list yang berisi list kata-kata dari setiap baris dalam file
            return file_names
    # Mengembalikan pesan kesalahan jika terjadi kesalahan saat membaca file
    except Exception as no:
        return f"{no} terjadi kesahalah!"
# Penggunaan fungsi 
print(reads('tiga.txt'))

def finds(file):
    try:
        # Membuka file dengan mode baca ('r') dan menggunakan encoding utf-8
        with open(file, 'r', encoding='utf-8') as files:
            # Membuat set kosong untuk menyimpan kata-kata unik
            format_txts = set()  
            
            # Iterasi melalui setiap baris dalam file
            for line in files:
                # Mengubah setiap baris menjadi lowercase, membersihkan dari spasi tambahan di awal dan akhir, 
                # lalu membagi baris menjadi list kata-kata
                words = line.casefold().strip().split()
                
                # Menambahkan semua kata dari baris saat ini ke dalam set format_txts
                format_txts.update(words)
            
            # Mengembalikan set yang berisi semua kata unik yang ada dalam file
            return format_txts
            
    except Exception:
        # Mengembalikan pesan "Invalid!" jika terjadi kesalahan saat membuka atau membaca file
        return "Invalid!"

txts = "empat.txt"
uniques = finds(txts)  # Memanggil fungsi finds untuk mencari kata-kata unik dalam file "empat.txt"

targets = 'anggur'
if targets in uniques:
    print(f"{targets}, ditemukan!")  # Cetak pesan jika target ditemukan dalam set uniques
else:
    print(f"{targets}, tidak ditemukan!")  # Cetak pesan jika target tidak ditemukan dalam set uniques


# Fungsi ini memeriksa apakah dua kata merupakan pasangan terbalik dengan membandingkan apakah kata pertama adalah kebalikan dari kata kedua
def is_reverse_pair(one, two):
    return one[::-1] == two

def find_reverse_pair(trea):
    # Inisialisasi list untuk menyimpan pasangan kewalik
    reverse_pairs = []  
    for tres in range(len(trea)):
        # Gunakan tres + 1 untuk memastikan tidak ada pasangan yang sama
        for fours in range(tres + 1, len(trea)):  
            # Memeriksa apakah pasangan kata terbalik
            if is_reverse_pair(trea[tres], trea[fours]): 
                # Menambahkan pasangan terbalik ke dalam list 
                reverse_pairs.append((trea[tres], trea[fours]))  
    return reverse_pairs

tre_lists = ["radar", "malam", "rotor", "malam"]
# Memanggil fungsi untuk menemukan pasangan terbalik
reverse_is_pairs = find_reverse_pair(tre_lists)  

if reverse_is_pairs:
    print("Pasangan terbalik ditemukan: ")
    for fives in reverse_is_pairs:
        # Mencetak setiap pasangan kewalik
        print(fives[0], "_", fives[1])  
else:
    print("Pasangan terbalik tidak ditemukan!")



def are_linked(word1, word2):

    #Fungsi ini memeriksa apakah dua kata saling bertautan

    if len(word1) != len(word2):
        # Jika panjang kata tidak sama, tidak mungkin saling bertautan
        return False  
    # Inisialisasi string kosong untuk menyimpan hasil penggabungan huruf
    linked_word = ""  
    for char1, char2 in zip(word1, word2):
        # Menggabungkan huruf bergantian dari kedua kata
        linked_word += char1 + char2  
    return linked_word


def find_linked_pairs(words):
    
    # Fungsi ini menemukan semua pasangan kata yang saling bertautan dalam daftar kata
    
    # Inisialisasi list untuk menyimpan pasangan kata yang saling bertautan
    linked_pairs = []  
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            # Memeriksa apakah dua kata saling bertautan
            linked_word = are_linked(words[i], words[j])  
            if linked_word:
                # Menambahkan pasangan kata yang saling bertautan ke dalam list
                linked_pairs.append((words[i], words[j], linked_word))  
    return linked_pairs

# Daftar kata yang akan diperiksa
words_list = ["sepatu", "dingin", "bersekolah", "jalan", "pulang", "dipakai"]

# Mencari pasangan kata yang saling bertautan dalam daftar kata
linked_pairs = find_linked_pairs(words_list)

# Cetak pasangan kata yang saling bertautan
if linked_pairs:
    print("Pasangan kata yang saling bertautan:")
    for pair in linked_pairs:
        # Cetak pasangan kata yang saling bertautan beserta kata yang dihasilkan
        print(f"{pair[0]} dan {pair[1]} membentuk: {pair[2]}")  
else:
    print("Tidak ada pasangan kata yang saling bertautan dalam daftar.")



# Fungsi untuk menemukan kata-kata yang saling bertautan tiga arah
def find_triple_linked_words(words):
    # Inisialisasi daftar kosong untuk menyimpan kata-kata yang ditemukan
    result = []  

    # Membuat set kata untuk pencarian yang lebih efisien
    word_set = set(words)

    # Iterasi melalui setiap kata dalam daftar kata yang diberikan
    for word1 in words:
        # Iterasi melalui setiap indeks dalam panjang kata saat ini
        for i in range(len(word1)):
            # Iterasi melalui setiap kata dalam daftar kata yang diberikan
            for word2 in words:
                # Memeriksa apakah kata kedua tidak sama dengan kata pertama dan panjangnya lebih besar dari indeks
                if word2 != word1 and len(word2) > i:
                    # Membuat kata baru dengan menggabungkan bagian-bagian dari kata pertama dan kedua
                    new_word = word1[:i] + word2[i] + word1[i+1:]
                    # Memeriksa apakah kata baru ada di dalam set kata
                    if new_word in word_set:
                        # Jika ya, tambahkan triple kata yang saling bertautan ke dalam daftar hasil
                        result.append((word1, word2, new_word))

    # Mengembalikan daftar kata-kata yang saling bertautan tiga arah
    return result

# Daftar kata yang diberikan
words = ["cat", "act", "dog", "god", "mat"]
# Memanggil fungsi untuk menemukan kata-kata yang saling bertautan tiga arah
triple_linked_words = find_triple_linked_words(words)
# Mencetak hasilnya
print(triple_linked_words)

# Dictionary kosong built-in
eng2sp = dict()
print(eng2sp)

# Dictionary dengan key dan value
eng2sp['one']= 'uno'
print(eng2sp)

# Dictionary dengan tiga item
eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
print(eng2sp)

# Mencari value dengan key
eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
results = eng2sp['two']
print(results)

# Jumlah pasangan key-value
eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
print(len(eng2sp))

# Apa key ada di eng2sp
eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
if 'two' in eng2sp:
    print(True)
else:
    print(False)

# Apakah sesuatu muncul sebagai value dalam dict, gunakan metode values()
eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
results = eng2sp.values()
if 'uno' in results:
    print(True)
else:
    print(False)

# Fungsi histrogram, parameter s(iterbel(dict))
def histogram(s):
    # Inisialisasi d dengan dic kosong, untuk menyimpan hasil
    d = {}
    # Iterasi item atau key c dalam itrabel s(dict/item/key)
    for c in s:
        # kondisi c(key) belum ada di dalam d
        if c not in d:
            # Menetampkan c sebagai key dalam d, dengan value 1 (telah ditemukan satu kali)
            d[c] = 1
            
        else:
            # Value yang terkait dengan c di dalam d, ditingkatkan 1 (utk mencerminkan frkuensi +)
            d[c] +=1
    return d
print(histogram({'one':'uno', 'two':'dos', 'three':'tres'}))

# Fungsi histrogram, parameter s(iterbel(dict))
def histogram(s):
    # Inisialisasi d dengan dic kosong, untuk menyimpan hasil
    d = dict()
    # Iterasi item atau key c dalam itrabel s(dict/item/key)
    for c in s:
        # kondisi c(key) belum ada di dalam d
        if c not in d:
            # Menetampkan c sebagai key dalam d, dengan value 1 (telah ditemukan satu kali)
            d[c] = 1
            
        else:
            # Value yang terkait dengan c di dalam d, ditingkatkan 1 (utk mencerminkan frkuensi +)
            d[c] +=1
    return d
print(histogram('onetwothree'))




"""
Buatkan dengan fungsi histogram utk menghitung frekuensi..
berapa kali setiap nilai/value unik dalam dictionary muncul

"""

def histogram(s):
    results = dict()
    for n in s.values():
        if n not in results:
            results[n] = 1
        else:
            results[n] += 1
    return results
print(histogram({'satu':'gajah', 'dua':'gajah', 'tiga':'cat'}))

def hitogram(a):
    hasil = dict()
    for v in a.values():
        hasil[v] = hasil.get(v, 0) + 1
    return hasil

all_hasil = histogram({'satu':'gajah', 'dua':'gajah', 'tiga':'cat'})
print(all_hasil)
print(all_hasil.get('a', 0))

""""""
def histogram(mas):
    results = {}
    for zak in mas:
        results[zak] = results.get(zak, 0) + 1
    return results

def modifikasi(unyu):
    for c, hit in unyu.items(): # sorted(unyu.items())
        print(c, hit)
unyu = histogram('parrot')
modifikasi(unyu)