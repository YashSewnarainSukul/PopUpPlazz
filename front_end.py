from tkinter import *

root = Tk()
root.configure(background='#e5f6ff')
root.geometry('1500x950')
root.title('PopUpPlazz')


selectregio = Listbox(master=root, bg='#d2d6d8')
selectregio.insert(END,'Selecteer uw regio')
for regionaam in ['Kanaleneiland','Utrecht Science Park','Overvecht','Leidsche Rijn','Ondiep','Binnenstad']:
    selectregio.insert(END, regionaam)
selectregio.pack(padx=5,pady=5,side=LEFT)

selectoppervlakte = Listbox(master=root, bg='#d2d6d8')
selectoppervlakte.insert(END,'Selecteer uw oppervlakte')
for oppervlak in ['100m2','500m2','1000m2','1200m2']:
    selectoppervlakte.insert(END, oppervlak)
selectoppervlakte.pack(padx=5,pady=5,side=LEFT)

selectdrukte = Listbox(master=root, bg='#d2d6d8')
selectdrukte.insert(END,'Selecteer bezoekersdichtheid')
for drukteaantal in ['1000','1500','3000','4000']:
    selectdrukte.insert(END, drukteaantal)
selectdrukte.pack(padx=5,pady=5,side=LEFT)

mainloop()