from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
import webbrowser
import time 


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



root = tk.Tk()
root.geometry('950x500')
root.resizable(0, 0)
root.title('VREME')
root.configure(background="white")


def getWeather():
    global textfield, t, c, clock, name

    city = textfield.get()

    geolocator = Nominatim(user_agent="geopy-exercises")
    location = geolocator.geocode(city)
    finder = TimezoneFinder()
    result = finder.timezone_at(lng=location.longitude, lat=location.latitude)
    print(result)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="TRENUTNO VREME")

    lat = location.latitude
    lon = location.longitude
    api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=1e2b56c900ca6221cecb1770fc041541"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=("Cisto","|" ,"OSECAJ","KAO",(temp),"°"))

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text="cisto nebo")
    #d.config(text=description)
    p.config(text=pressure)




def GRADOVI_page():
    global textfield, clock, name, t, c, w, h, d, p



    GRADOVI_frame = tk.Frame(main_frame)

    Search_image = PhotoImage(file="slike//search.png")

    lb = tk.Label(GRADOVI_frame, image=Search_image ,text='', compound='top', font=('Bold', 30))
    lb.image = Search_image  
    lb.pack(padx=12, pady=6)

    label_text = tk.Label(GRADOVI_frame, text="Unesite grad:")
    label_text.place(x= 90, y=56)
    

    textfield = tk.Entry(GRADOVI_frame, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0,  fg="white")
    textfield.place(x=240, y=27)
    textfield.focus()

    Search_icon = PhotoImage(file="slike//search_icon.png")
    myimage_icon = Button(GRADOVI_frame, image=Search_icon, width=40, height=40, borderwidth=0, cursor="hand2", bg='#404040' , command=getWeather)
    myimage_icon.image = Search_icon
    myimage_icon.place(x=550, y=25)

    

    Frame_image = tk.PhotoImage(file="slike//box.png")
   
    lb = tk.Label(GRADOVI_frame, image=Frame_image)
    lb.image = Frame_image  
    lb.pack(padx=0, pady=0, side=BOTTOM)

    
    
    Label1=Label(GRADOVI_frame,text="VETAR", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
    Label1.place(x=70, y=360)

    Label2=Label(GRADOVI_frame,text="SVEZINA", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
    Label2.place(x=240, y=360)

    Label3=Label(GRADOVI_frame,text="OPIS", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
    Label3.place(x=425, y=360)

    Label4=Label(GRADOVI_frame,text="PRITISAK", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
    Label4.place(x=600, y=360)

    #FRAME VREMENA
    t=Label(GRADOVI_frame, font=("arial", 70, "bold"), fg="#ee666d")
    t.place(x=530, y=120)
    c=Label(GRADOVI_frame, font=("arial",15, 'bold'))
    c.place(x=530,y=250)

    w=Label(GRADOVI_frame, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
    w.place(x=87, y=390)
    h=Label(GRADOVI_frame, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
    h.place(x=268, y=390)
    d=Label(GRADOVI_frame, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
    d.place(x=430, y=390)
    p=Label(GRADOVI_frame, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
    p.place(x=633, y=390)


    Logo_image = tk.PhotoImage(file="slike//logo.png")
   
    lb = tk.Label(GRADOVI_frame, image=Logo_image)
    lb.image = Logo_image  
    lb.pack(padx=0, pady=0)


    name = tk.Label(GRADOVI_frame, text="TRENUTNO VREME", font=("arial", 15, "bold"))
    name.place(x=30,y=100)
    clock = tk.Label(GRADOVI_frame, text="", font=("Helvetica", 20))
    clock.place(x=30, y=130)

    
    GRADOVI_frame.pack(pady=20)




def DANAS_page():
    DANAS_frame = tk.Frame(main_frame)
    DANAS_frame.pack(pady=20)
    current_rating = 0


 
    #LABEL ZA OCENJIVANJE
    rating_label = tk.Label(DANAS_frame, text="Ocenite aplikaciju:" , font=("Italic" , 14, "bold"))
    rating_label.pack(side=tk.LEFT, pady=25)

    rating_frame = tk.Frame(DANAS_frame)
    rating_frame.pack(side=tk.LEFT)

    rating_buttons = []

    #DUGME I KLIK
    def handle_rating_click(rating):
        #BOJA OCENE NA RATINGU 
        for i in range(5):
            if i < rating:
                rating_buttons[i].config(bg="gold")
            else:
                rating_buttons[i].config(bg="white")

    #PET OCENA
    for i in range(5):
        rating_button = tk.Button(rating_frame, text=str(i+1), width=2, command=lambda rating=i+1: handle_rating_click(rating))
        rating_button.pack(side=tk.LEFT, padx=5)
        rating_buttons.append(rating_button)

   
    DANAS_frame = tk.Frame(main_frame)
    DANAS_frame.pack(pady=20)


   
    comment_label = ttk.Label(DANAS_frame, text="Ostavite komentar:")
    comment_label.pack(pady=0)


    name_label = ttk.Label(DANAS_frame, text="Ime:")
    name_label.pack()

    name_entry = ttk.Entry(DANAS_frame, width=30)
    name_entry.pack()
    
    
    email_label = ttk.Label(DANAS_frame, text="Email:")
    email_label.pack()

    email_entry = ttk.Entry(DANAS_frame, width=30)
    email_entry.pack()

    
    comment_box = tk.Text(DANAS_frame, width=50, height=5)
    comment_box.pack(pady=10)
    comment_box.config(borderwidth=2, highlightthickness=2, highlightbackground="black")
    

    def handle_rating_click(rating):
      global current_rating
      current_rating = rating
    #BOJA NA OSNOVU OCENE
      for i in range(5):
         if i < rating:
            rating_buttons[i].config(bg="gold")
         else:
            rating_buttons[i].config(bg="white")



    
    def submit_comment():
      #UZIMA KOMENTARE I OSTALE POD
     name_text = name_entry.get()
     email_text = email_entry.get()
     comment_text = comment_box.get("1.0", tk.END)
     rating = 0
     for i in range(5):
        if rating_buttons[i]["bg"] == "gold":
            rating = i + 1
    
    #PROVERAVA DALI OSTOJE ISTI KOMENTARI I OCENE
     with open("OCENE.txt", "r") as f:
        for line in f:
            if f"Ocena: {rating} : {comment_text}" in line:
                comment_display = ttk.Label(DANAS_frame, text="Komentar sa istom ocenom i tekstu već postoji.")
                comment_display.pack(pady=10)
                return
    
    #SACUVAJ KOMENTARE
     with open("OCENE.txt", "a") as f:
        f.write(f"{name_text} ({email_text}) Ocena: {rating} : {comment_text}\n")
    
    
    comment_display = ttk.Label(DANAS_frame, text="Hvala na izdvojenom vremenu!")
    comment_display.pack(pady=10)


    #DUGME ZA KOMENTAR
    submit_button = ttk.Button(DANAS_frame, text="POSALJI", command=submit_comment)
    submit_button.pack(pady=10)




def OPROGRAMU_page():
    OPROGRAMU_frame = tk.Frame(main_frame)

   
    def show_popup():
        #KREIRA ISKACUJUCI PROZOR
        popup_window = tk.Toplevel(OPROGRAMU_frame)
        popup_window.title("Podrzi osnivaca")
        popup_window.geometry("400x300+{}+{}".format(int(popup_window.winfo_screenwidth()/2 - 250), int(popup_window.winfo_screenheight()/2 - 250)))

        popup_window.configure(bg="#f2f2f2")
        popup_window.attributes('-alpha', 0.95)
        popup_window.overrideredirect(True)
        popup_window.config(borderwidth=2, highlightthickness=2, highlightbackground="black")
 

        #INPUT ZA KARTICE
        cc_label = tk.Label(popup_window, text="Unesite vase podateke na kartici:", font=("Helvetica", 14), bg="#f2f2f2")
        cc_label.pack(pady=10)

        #UNOS OKVIRI
        cc_num_label = tk.Label(popup_window, text="Broj kartice:", font=("Helvetica", 12), bg="#f2f2f2")
        cc_num_label.pack()

        cc_num_entry = tk.Entry(popup_window, font=("Helvetica", 12))
        cc_num_entry.pack()

        cc_exp_label = tk.Label(popup_window, text="Datum isteka:", font=("Helvetica", 12), bg="#f2f2f2")
        cc_exp_label.pack()

        cc_exp_entry = tk.Entry(popup_window, font=("Helvetica", 12))
        cc_exp_entry.pack()

        cc_cvv_label = tk.Label(popup_window, text="CVV:", font=("Helvetica", 12), bg="#f2f2f2")
        cc_cvv_label.pack()

        cc_cvv_entry = tk.Entry(popup_window, font=("Helvetica", 12))
        cc_cvv_entry.pack()


        amount_label = tk.Label(popup_window, text="Kolicina prilozenog novca:", font=("Helvetica", 12), bg="#f2f2f2")
        amount_label.pack()

        amount_entry = tk.Entry(popup_window, font=("Helvetica", 12))
        amount_entry.pack()


        def save_data():
         #čitanje unetih podataka
         cc_num = cc_num_entry.get()
         cc_exp = cc_exp_entry.get()
         cc_cvv = cc_cvv_entry.get()
         amount = amount_entry.get()

         #kreiranje novog reda u datoteci OCENE.txt
         with open("NOVAC.txt", "a") as f:
          f.write(f"{cc_num}, {cc_exp}, {cc_cvv}, {amount}\n")

         popup_window.destroy()


        #DUGME 
        buy_button = tk.Button(popup_window, text="Podrži osnivača", font=("Helvetica", 14), bg="#4CAF50", fg="white", activebackground="#3e8e41", command=save_data)
        buy_button.pack(pady=10)


        buy_button = tk.Button(popup_window, text="Podzi osnivaca", command=popup_window.destroy)
        buy_button.pack(pady=10)
        
     
   
        

    label_text = '\n\n\nVREME APP\n\n\nVerzija: 5.2.2\nDatum 06-03-2023\nSistem: Windows 7/10/11\nOsnivac: Aleksandar Gajic\n\n\n\nAplikaciju koja je dizajnirana da pruži korisnicima\ntrenutne informacije o vremenskim uslovima na njihovoj\nlokaciji, kao i prognoze za naredne dane.\n\n\n '
    lb = tk.Label(OPROGRAMU_frame, text=label_text, font=("Helvetica", 12, "bold"), justify="center", anchor="center", padx=20, pady=20)
    lb.pack()

    #LINK TEXT
    link_text = "Za više informacija o meni, posetite moj LinkedIn profil"
    link_label = tk.Label(OPROGRAMU_frame, text=link_text, font=("Helvetica", 12, "bold" ,"underline"), fg="blue", cursor="hand2")
    link_label.pack()

   
    def open_link(event):
        webbrowser.open("https://www.linkedin.com/in/aleksandar-gaji%C4%87-443947197")

    
    link_label.bind("<Button-1>", open_link)

    OPROGRAMU_frame.pack(pady=20)

    #ISKACUJUCI PROZOR
    timeout = 5

    
    countdown_label = tk.Label(OPROGRAMU_frame, text=f"Popup will show in {timeout} seconds")
    countdown_label.pack(pady=20)

    
    for i in range(timeout):
        countdown_label.config(text=f"Popup will show in {timeout-i} seconds")
        OPROGRAMU_frame.update()
        time.sleep(1)

    
    show_popup()




#SKLANJA INDIKATOR
def hide_indicators():
    GRADOVI_indicate.config(bg='#158aff')
    DANAS_indicate.config(bg='#158aff')
    OPROGRAMU_indicate.config(bg='#158aff')

#UNISTAVA I SPRECAVA DVA ILI VISE FREJMA U JEDNOM 
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


#PRAVI INDIKATOR
def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#c3c3c3')
    delete_pages()
    page()


# PROZOR BEZ STRANICA #
root.overrideredirect(True)

option_frame = tk.Frame(root, bg="#158aff")  ##5454FF   #c3c3c3


# MENI
GRADOVI_btn = tk.Button(option_frame, text='GRADOVI', font=("Times" , 18, "bold") ,fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(GRADOVI_indicate, GRADOVI_page))
GRADOVI_btn.place(x=14, y=50)

GRADOVI_indicate = tk.Label(option_frame, text='', bg='#158aff') 
GRADOVI_indicate.place(x=5, y=50, width=5, height=40)
                             

DANAS_btn = tk.Button(option_frame, text='UTISAK', font=("Times" , 18, "bold") ,fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(DANAS_indicate, DANAS_page))
DANAS_btn.place(x=14, y=100)

DANAS_indicate = tk.Label(option_frame, text='', bg='#158aff')
DANAS_indicate.place(x=5, y=100, width=5, height=40)


OPROGRAMU_btn = tk.Button(option_frame, text='O PROGRAMU', font=("Times" , 12, "bold") ,fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(OPROGRAMU_indicate, OPROGRAMU_page))
OPROGRAMU_btn.place(x=12, y=385)

OPROGRAMU_indicate = tk.Label(option_frame, text='', bg='#158aff')
OPROGRAMU_indicate.place(x=5, y=380, width=5, height=40)


# DUGME ZA GASENJE APP
def close_window():
    root.destroy()

APPKRAJ_btn = tk.Button(option_frame, text='IZLAZ', command=close_window, font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3')
APPKRAJ_btn.place(x=35, y=415)





option_frame.pack(side=tk.LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=150, height=500)

#PRVA PRAZNA STRANA
main_frame = tk.Frame(root, highlightbackground='black' , highlightthickness=2)
image_file = tk.PhotoImage(file="slike//GLAVNA1.png" , height=500, width=800)

image_label = tk.Label(main_frame, image=image_file, bg="#5454FF")
image_label.pack()



main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=500, width=800)

#PROZOR SE POKRECE SA KURSOROM 2/2
draggable = DraggableWindow(root)

root.mainloop()
