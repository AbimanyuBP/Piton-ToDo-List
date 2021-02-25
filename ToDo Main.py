todo = []
date = []
status = []
s = "Selesai"
b = "Tidak Selesai"


def Add():
    tsk = input('tambahkan list todo: ')
    tgl = input("Tanggal Berapa Deadlinenya?: ")
    todo.append(tsk)
    date.append(tgl)
    status.append(b)
'''

def Add():
    tsk = input('tambahkan list todo: ')
    tgl = input("Tanggal Berapa Deadlinenya?: ")
    todo["belum sukses"].append(tsk)
    date["belum sukses"].append(tgl)
'''

def display():
    l = 0
    while l < len(todo):
        print(l+1,".",todo[l], date[l], status[l])
        l += 1


def apudeto():
    m = ''
    while m != 'n': 
        display()
        updt = int(input('pilih nomer berapa: '))
        m = input("Apakah anda yakin ingin menyelesaikan task (y/n)")
        if m == 'y':
            status[updt-1] = s  
            display()
            break      

print('selamat datang di todolist')
p = ''
while p != '4':
    p = input("""MENu
            1. Add
            2. Display
            3. Update
            4. Exit
            """)
    if p == '1':
        Add()
    elif p == '2':
        display()
    elif p == '3':
        apudeto()
    elif p == '4':
        print('gudbay maderfaker')
    else:
        print('ketik yg bener bg')