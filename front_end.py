from tkinter import *

root = Tk()

root.geometry('1200x800')
root.title('PopUpPlazz')

# Achtergond van het hoofdscherm-------------

random_bg='blauwe_kaart.gif'
background_zoek_image = PhotoImage(file=random_bg)
background_zoek = Label(master=root,image=background_zoek_image)
background_zoek.pack(fill='both', side='left',expand=False)

# Titel van het hoofdscherm------------------

titel = Label(master=root, bg='#d2d6d8', text='PopUpPlazz',font='Tahoma')
titel.pack()
titel.place(y=0,width=1200,height=50)

# Labels boven keuzemenu's-------------------

regio = Label(master=root, bg='#d2d6d8', text='Regio', font='Tahoma')
regio.pack()
regio.place(y=100,x=20,width=150,height=20)

oppervlakte = Label(master=root, bg='#d2d6d8', text='Oppevlakte', font='Tahoma')
oppervlakte.pack()
oppervlakte.place(y=100,x=200,width=180,height=20)

drukte = Label(master=root, bg = '#d2d6d8', text='Drukte', font='Tahoma')
drukte.pack()
drukte.place(y=100,x=400,width=200,height=20)


# De drie keuzemenu's------------------------

selectregio = Listbox(master=root, bg='#d2d6d8',selectmode=MULTIPLE)
for regionaam in ['Kanaleneiland','Utrecht Science Park','Overvecht','Leidsche Rijn','Ondiep','Binnenstad']:
    selectregio.insert(END, regionaam)
selectregio.pack(padx=5,side=LEFT)
selectregio.place(x=20,y=120,width=150,height=140)

selectoppervlakte = Listbox(master=root, bg='#d2d6d8',selectmode=MULTIPLE)
for oppervlak in ['100m2','500m2','1000m2','1200m2']:
    selectoppervlakte.insert(END, oppervlak)
selectoppervlakte.pack(padx=5,side=LEFT)
selectoppervlakte.place(x=200,y=120,width=180,height=100)

selectdrukte = Listbox(master=root, bg='#d2d6d8',selectmode=MULTIPLE)
for drukteaantal in ['1000','1500','3000','4000']:
    selectdrukte.insert(END, drukteaantal)
selectdrukte.pack(padx=5,side=LEFT)
selectdrukte.place(x=400,y=120,width=200,height=100)

# Zoek button --------------------------------

zoeken = Button(master=root, bg='black',fg='black',text='Zoek')
zoeken.pack()
zoeken.place(x=750,y=100,width=50,height=20)

mainloop()