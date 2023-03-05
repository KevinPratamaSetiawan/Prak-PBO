#Soal 1
n = int(input("n : "))

for i in range (n) :
    for j in range (n) :
        print("*",end="")
    print("")

#Soal 2
username = "informatika"
password = "12345678"
n = 0

while n < 3 :
    input_username = input("Username anda : ")
    input_password = input("Password anda : ")

    if input_username == username and input_password == password :
        print("Berhasil login !")
        n = 4
    else :
        print("Username atau password salah coba lagi")
        n += 1
