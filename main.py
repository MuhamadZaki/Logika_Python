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
    dx = x2 - x1
    dy = y2 - y1
    squared = dx**2 + dy**2
    result = math.sqrt(squared)
    return print("Hasil: ", result)
distance(1,2,4,6)

#Apa Outputnya?

# A. 6
# B. 5
# C. 5.0
# D. 2

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def area(radius):
    return math.pi * radius**2

def circel_area(xc,yc,xp,yp):
    radius = distance(xc,yc,xp,yp)
    result = area(radius)
    return print("Hasil: ",result)
circel_area(1,2,3,4)

#Apa Outputnya?

# A. 26
# B. 25
# C. 25.132741228718352
# D. 2

def is_between(x,y,z):
    return x<=y<=z
print(is_between(1,1,1))

#Apa Outputnya?

# A. True
# B. 1
# C. False
# D. 3

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
print("Hasil: ",factorial(3))

#Apa Outputnya?

# A. 6
# B. 1
# C. 2
# D. 3

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

#Apa Outputnya?

# A. 0
# B. 1
# C. 2
# D. 8

def first(word):
    return word[0]
print(first("Muhamad Zaki"))

#Apa Outputnya?

# A. M
# B. Z
# C. u
# D. i

def last(word):
    return word[-1]
print(last("Muhamad Zaki"))

#Apa Outputnya?

# A. M
# B. Z
# C. u
# D. i

def middle(word):
    return word[1:-1]
print(middle("Muhamad Zaki"))

#Apa Outputnya?

# A. Muhamad Zaki
# B. hamadZak
# C. dZ
# D. uhamad Zak

def palindrome(middle):
    return middle [1:-1]
print(palindrome("ab"))

#Apa Outputnya?

# A. ab
# B. 
# C. a
# D. b

def palindrome(middle):
    return middle [1:-1]
print(palindrome(" "))

#Apa Outputnya?

# A. " "
# B. 
# C. Error
# D. 1

def is_palindrome(karakter):
    if karakter == karakter[::-1]:
        print (True)
    else:
        print(False)
is_palindrome("radar")

#Apa Outputnya?

# A. False
# B. True
# C. Error
# D. 5


def is_palindrome(num):
    return num == num[::-1]
print(is_palindrome([1,2,1]))

#Apa Outputnya?

# A. False
# B. True
# C. Error
# D. 4

x = 5
print(x)

#Apa Outputnya?

# A. False
# B. True
# C. 5.0
# D. 5

x = 7
print(x)

#Apa Outputnya?

# A. False
# B. True
# C. 7.0
# D. 7

a = 5
b = a
a = 3
print(a)

#Apa Outputnya?

# A. False
# B. True
# C. 3
# D. 5

x = 4
x = x + 1
x = 2
print(x)

#Apa Outputnya?

# A. Error
# B. 2
# C. 4
# D. 5

x = 0
x = x + 1
print(x)

#Apa Outputnya?

# A. 1 kenaikan
# B. 2
# C. 4
# D. 5

x = 0
x = x - 1
print(x)

#Apa Outputnya?

# A. 1
# B. -1 penurunan
# C. 4
# D. 5

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
        print("Meledak!")
countdown(1)

#Apa Outputnya?

# A. 1
# B. -1
# C. Meledak!
# D. 0

def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n - n * 3 + 1
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


x = 4
a = 2
while True:
    print(x)
    y = int((x + a / x) / 2)
    if y == x: 
        break
    x = y
#Apa Outputnya?

# A. 4
# B. 2
# C. 1
# D. Semua benar!

fruit = "Banana"
letter = fruit [0]
print(letter)

#Apa Outputnya?

# A. Banana
# B. B
# C. a
# D. n

fruit = "Banana"
i = fruit[1]
result = [i]
print(result)

#Apa Outputnya?

# A. Banana
# B. B
# C. a
# D. n

fruit = "Banana"
result = len(fruit)
print(result)

#Apa Outputnya?

# A. 6
# B. B
# C. a
# D. n

fruit = "Banana"
length = len(fruit)
last = fruit[-1]
print(length, last)

#Apa Outputnya?

# A. 6
# B. B
# C. a
# D. n

fruit = "Banana"
index = 3
while index < len(fruit):
    latter = fruit[index]
    print(latter)
    index = index + 1

#Apa Outputnya?

# A. 6
# B. B
# C. ana
# D. n

prefixes = "JKLMNOPQ"
suffix = 'ack'

for latter in prefixes:
    print(latter + suffix)

#Apa Outputnya?

# A. Jack, Kack, 
# B. Mack, Lack
# C. Nack, Oack
# D. Pack, Qack

def karakter(satu):
    if satu:
        dua = satu [0:4]
        print(dua)
karakter("Ular Python")

#Apa Outputnya?

# A. Ular 
# B. Python
# C. Ular Python
# D. Semua benar!

def karakter(tiga):
    if tiga:
        empat = tiga [5:11]
        print(empat)
karakter("Ular Python")

#Apa Outputnya?

# A. Ular 
# B. Python
# C. Ular Python
# D. Semua benar!

def fruit(apel):
    if apel:
        result = apel[:3]
        print(result)
fruit("Apel")

#Apa Outputnya?

# A. Apel 
# B. Ape
# C. l
# D. Semua benar!

def fruit(apel):
    if apel:
        result = apel[3:]
        print(result)
fruit("Apel")

#Apa Outputnya?

# A. Apel 
# B. Ape
# C. l
# D. Semua benar!

def fruit(apel):
    if apel:
        result = apel[3:3]
        print(result)
fruit("Apel")

#Apa Outputnya?

# A. Apel 
# B. Ape
# C. l
# D. Empty string

def greeting(a):
    if a:
        new_gretting = "M" + a[1:]
        print(new_gretting)
greeting("Hallo, Tante Panas!")

#Apa Outputnya?

# A. Hallo, Tante Panas!
# B. H
# C. a
# D. Mallo, Tante Panas!

def find(word, letter,):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1
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

def membaca(file_name, encoding='utf-8'):
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
        # Menanangani kasus jika file tidak ditemukan
        return f'File {file_name} tidak ditemukan!'
    
    except UnicodeEncodeError:
        # Menangani kesalahan encoding, jika encoding salah
        return f'Gagal mendecode {file_name},karena menggunakan encoding yang salah!'
    
    except Exception as z:
        # Menangani kesalahan umum lainnya
        return f'Terjadi kesalahan! {z}'
# Penggunaan fungsi    
print(membaca(file_name = 'zaki.txt'))

#Apa Outputnya?

# A. Author: Muhamad Zaki
# B. "Seharusnya yang lebih kuat membantu yang lebih lemah, dan berlebih membantu yang kekurangan."
# C. Error
# D. A & B benar!

