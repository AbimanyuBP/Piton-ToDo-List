username = str("user")
nama = str
todo = []
kondisi = []
default = "Belum Selesai"
finished = "Selesai"
p = 0

while nama != username:
    nama = input("Username anda:")
    if nama == username:
        print("Selamat datang " + nama)
        print("="*50)
        print("Todo anda saat ini adalah " + str(len(todo)) + " ingin menambahkan?")
        respon = input("Response y/n? : ")
        while respon == "y":
            list = input("Apa ToDo nya ")   
            todo.append(list)
            kondisi.append(default)
            respon = input("Mau tambah lagi y/n? ")
        print("List yang terbuat adalah ")
        while p < len(todo):
            print(str(p+1) + " " + todo[p] + " : " + kondisi[p])
            p += 1
        break
    else:
        print("Username Tidak Ada")
        continue
    print('pw salah masukan lagi')
    
    print('awkokdoaewkdoeaked'
