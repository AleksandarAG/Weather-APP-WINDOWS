from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar  
import os


#PROZOR SE POKRECE SA KURSOROM 1/2
class DraggableWindow:
    def __init__(self, root):
        self.root = root
        self.root.bind('<Button-1>', self.start_move)
        self.root.bind('<ButtonRelease-1>', self.stop_move)
        self.root.bind('<B1-Motion>', self.move_window)

    def start_move(self, event):
        self._drag_x = event.x
        self._drag_y = event.y

    def stop_move(self, event):
        self._drag_x = None
        self._drag_y = None

    def move_window(self, event):
        if self._drag_x is not None and self._drag_y is not None:
            x = self.root.winfo_x() + (event.x - self._drag_x)
            y = self.root.winfo_y() + (event.y - self._drag_y)
            self.root.geometry(f'+{x}+{y}')


# UBACIVANJE SLIKE
root = Tk()
image = PhotoImage(file = "slike//pozadina3.png")    # ovaj deo koda radi na verziji python 3.11.2 64-bit


# POZICIONIRANJE I SIRINA INTERFEJSA
height = 630
width = 950
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)


# PROZOR BEZ STRANICA
root.geometry('{}x{}+{}+{}'.format(width, height, x,y))
root.overrideredirect(True)

root.config(background="#5454FF")  # boja odabrana za pozadinu



# NASLOV FONT i POZICIONIRANJE
welcome_label = Label(text="VREMENSKA PROGNOZA", bg="#5454FF", font=("Trebuchet Ms", 25, "bold"), fg="#FFFFFF")
welcome_label.place(x=295, y=12)

bg_label = Label(root, image=image, bg="#5454FF")  # boja odabrana za pozadinu providne slike
bg_label.place(x=210, y=50)


# UCITAVANJE NATPIS,FONT I POZICIONIRANJE
progress_label = Label(root, text="Ucitavanje...",  font=("Trebuchet Ms", 14, "bold"), fg="#FFFFFF", bg="#5454FF")
progress_label.place(x=390, y=530)

progress = ttk.Style()
progress. theme_use('clam')
progress. configure("red.Horizontal.TProgressbar", background="#108cff")


# PROCENAT UCITAVANJA
progress = Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate', style="red.Horizontal.TProgressbar")
progress.place(x=165, y=570)

# PREBACIVANJE NA SLEDECU STRANU

def top():
    root.withdraw()
    os.system("python\\appinterfejs.py")
    root.destroy()


# BRZINA NAPRETKA PROGRESS BAR-A I PRIKAZ U PROCENTIMA
i = 0

def load():
    global i
    if i <= 10:
        txt = 'Ucitavanje...' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(600, load)
        progress['value'] = 10*i
        i += 1

    else:
        top()

#PROZOR SE POKRECE SA KURSOROM 2/2
draggable = DraggableWindow(root)
load()
root.resizable(False, False)


root.mainloop()
