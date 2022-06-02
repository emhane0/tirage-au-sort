import tkinter
import random

m = 0
un = 0
deux = 0
trois = 0
quatre = 0
cinq = 0
six = 0
una = 0
dosa = 0
tresa = 0
cuatra = 0
cinca = 0
seisa = 0



def getentry():
    rvb = 0
    un = 0
    deux = 0
    trois = 0
    quatre = 0
    cinq = 0
    six = 0
    brg = 0
    while rvb < m:
        brg = random.randint(1, 6)
        rvb = rvb + 1
        if brg == 1:
            un = un + 1
        if brg == 2:
           deux = deux + 1
        if brg == 3:
           trois = trois + 1
        if brg == 4:
           quatre = quatre + 1
        if brg == 5:
           cinq = cinq + 1
        if brg == 6:
           six = six + 1
        prt()
def prt():
    una = 0
    dosa = 0
    tresa = 0
    cuatra = 0
    cinca = 0
    seisa = 0
    master = tkinter.Tk()
    una = tkinter.IntVar(master, name ="uno")
    master.setvar(name ="uno", value = un)
    dosa = tkinter.IntVar(master, name ="dos")
    master.setvar(name ="dos", value = deux)
    tresa = tkinter.IntVar(master, name ="tres")
    master.setvar(name ="tres", value = trois)
    cuatra = tkinter.IntVar(master, name ="quatro")
    master.setvar(name ="quatro", value = quatre)
    cinca = tkinter.IntVar(master, name ="cinco")
    master.setvar(name ="cinco", value = cinq)
    seisa = tkinter.IntVar(master, name ="seis")
    master.setvar(name ="seis", value = six)
    print("Value of 1()", master.getvar(name ="uno"))

    


fenetre = tkinter.Tk()

label = tkinter.Label(fenetre, text="combien de foit veut tu lancer le dé")
label.pack()

s = tkinter.Spinbox(fenetre, from_=0, to=10,)
m = int(s.get())
s.pack()

bouton=tkinter.Button(fenetre, text="entrer", command=getentry)
bouton.pack()

fenetre.mainloop()