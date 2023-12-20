# Modul math digunakan untuk operasi matematika, seperti sqrt(akar kuadrat) dan pi
import math

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
print(reads(file_name = 'zaki.txt'))

#Apa Outputnya?

# A. Author: Muhamad Zaki
# B. Junior Python Developer
# C. Error
# D. A & B benar!

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
new_reads(data ='zaki.txt')
#Apa Outputnya?

# A. Author: Muhamad Zaki
# B. Junior Python Developer
# C. Error
# D. A & B benar!

print('\n')


def reads_two(datas):
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
print(reads_two('zaki.txt'))


