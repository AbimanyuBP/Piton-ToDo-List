class User(object):
    def __init__(self, name):
        self.name = name
    
    todoname = []
    todoprio = []
    tododate = []

    def list(self):
        p = 0
        if p < len(self.todoname):
            print("To Do ", self.name," adalah:")
            while p < len(self.todoname):
                print('Anda memiliki task ',self.todoname[p],' yang memiliki prioritas', self.todoprio[p],' dengan deadline pada tanggal', self.tododate[p])
                p += 1
        else:
            print('List anda Kosong!')

    def add(self):
        print('Menambahkan ToDo Baru... \n')
        tsk = input('Nama Task?: ')
        prio = input('Seberapa Penting?: ')
        date = input('Tanggal Berapa Deadlinenya?: ')
        self.todoname.append(tsk)
        self.todoprio.append(prio)
        self.tododate.append(date)
        print('Data Berhasil Terinput')

users = ['Abim', 'Reihan', 'Arjun', 'Arip']
print('Selamat datang di aplikasi ToDo list ini')
print('List User yang terdaftar ', users)
uname = input('Masukkan Nama User = ')
print('Selamat Datang ', uname)
isi = ''
while isi != 'E':
    isi = input("""Menu
            L. List ToDo Anda
            A. Buat List Baru
            E. Exit\n""")
    a = User(uname)
    if isi == 'L':
        print('List ToDo User ', a.name)
        a.list()
    elif isi == 'A':
        a.add()
    elif isi == 'E':
        print('Bye Bitch!')
    else:
        print('Invalid Command Homie...')
