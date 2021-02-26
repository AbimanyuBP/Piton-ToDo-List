class User(object):
    def __init__(self, name):
        self.name = name
        self.todoname = []
        self.todoprio = []
        self.tododate = []

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

users_object = []
yo = ''
p = 0
    
def name_list():
    if users_object:
        for i, e in enumerate(users_object):
            print(e.name)
    else:
        print("Belum Ada User yang Terdaftar!")

def search_index(name):
    for i, e in enumerate(users_object):
        if e.name == name:
            return i
    return -1   

def search_name(name):
    for i, e in enumerate(users_object):
        if e.name == name:
            return e.name
    return -1

def todo_list(name):
    for i, e in enumerate(users_object):
        if e.name == name:
            e.list()

def addemgud(name):
    for i, e in enumerate(users_object):
        if e.name == name:
            e.add()

def menu(moi):
    print("Halo",moi )
    isi = ''
    while isi != 'E':
        isi = input("""Menu
                L. List ToDo Anda
                A. Buat List Baru
                E. Exit\n""")
        poi = search_index(moi)
        if isi == 'L':
            print('List ToDo User ', moi)
            todo_list(moi)
        elif isi == 'A':
            addemgud(moi)
        elif isi == 'E':
            print('Bye Bitch!')
        else:
            print('Invalid Command Homie...')

def identifier(username):
    if username != search_name(username):
        print('Sepertinya anda belum terdaftar')
        le = input('Ingin Mendaftar (y/n)?')
        if le == 'y':
            pe = input('Nama anda: ')
            users_object.append(User(pe))
            print('Nama anda Sudah Terdaftar!')
            lo = input('Ingin masuk ke todo list anda (y/n)?')
            if lo == 'y':
                menu(pe)
            elif lo == 'n':
                print('Baiklah Kembali ke menu login...')
                mainmenu()
        elif le == 'n':
            print('Aight Im outtie')
        else:
            print('That aint right')
    elif username == search_name(username):
        menu(username)

def mainmenu():
    huha = ''
    while huha != 'n':
        print('Selamat datang di aplikasi ToDo list ini')
        huha = input('''Menu
        1.Login
        2.Exit
        ''')
        if huha == '1':
            print('User Yang Sudah Terdaftar Adalah')
            name_list()
            meong = input('Masukkan Nama User: ')
            identifier(meong)
        elif huha == 'n':
            print('Very Well Goodbye...')
            break
        else:
            print('Error Command')

    
mainmenu()