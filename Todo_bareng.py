class Kopi:

    global listkopi
    listkopi = []

    def __init__(self):
        pass

    def add(self):
        inpKopi = input('masukan nama')
        listkopi.append(inpKopi)
        print('kopi dimasukan',inpKopi)

    def display(self):
        for i,j in enumerate(listkopi):
            print(i,'.',j)

    def menu(self):
        while True:
            pilih = input('''menu
        1.tambah
        2.tampil
        3.exit
        pilih = ''')
        if pilih == '1':
            self.add()
            continue
        elif pilih == '2':
            self.display()
        elif pilih == '3':
            print('bye')
            break
        else:
            print('ketik yg bener gblgkkgkgkgkg')

golda = Kopi()

golda.menu()

#han msh ada lu?
