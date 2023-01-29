from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import csv
import sqlite3




###---------------------------------------------------------------------------Ana Ekran

def main_screen():

    window = Toplevel()
    window.title("Chess")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False)

    img = ImageTk.PhotoImage(file="chess.jpg")
    Label(window, image=img, bg="white").place(x=-100, y=60)

    frame = Frame(window, width=348, height=350, bg="white")
    frame.place(x=480, y=40)

    common_img1 = PhotoImage(width=1, height=1)
    new_game_button = Button(window, text="Yeni Oyun", image=common_img1, width=290, height=70,
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 15))

    new_game_button.place(x=500, y=90)

    common_img2 = PhotoImage(width=1, height=1)
    ongoing_games_button = Button(window, text="Devam Eden Oyunlarım", image=common_img2, width=290, height=70,
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 15))

    ongoing_games_button.place(x=500, y=190)

    common_img3 = PhotoImage(width=1, height=1)
    settings_button = Button(window, text="Ayarlar", image=common_img3, width=290, height=70,
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 15))

    settings_button.place(x=500, y=290)

    common_img4 = PhotoImage(width=1, height=1)
    account_settings_button = Button(window, text="Hesap Ayarları", image=common_img4, width=140, height=20,
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 10), command = account_settings)

    account_settings_button.place(x=770, y=5)

    window.mainloop()





def account_settings():

    ac = Toplevel()
    ac.title("Hesap Ayarları")
    ac.geometry("925x500+300+200")
    ac.configure(bg="#fff")
    ac.resizable(False, False)
    ac = Toplevel()
    ac.title("Hesap Ayarları")
    ac.geometry("925x500+300+200")
    ac.configure(bg="#fff")
    ac.resizable(False, False)

    def query():
        conn = sqlite3.connect("users.db")

        c = conn.cursor()

        c.execute("SELECT *, oid FROM users ORDER BY rowid DESC LIMIT 1;")
        records = c.fetchall()
        print(records)

        print_records = ""
        for record in records:
            print_records += record[0] + " " + record[1]

        query_label = Label(ac, text=print_records, bg="white", font = 23)
        query_label.place(x=500, y=200)


    img = ImageTk.PhotoImage(file="chess.jpg")
    Label(ac, image=img, bg="white").place(x=-100, y=60)

    frame = Frame(ac, width=348, height=350, bg="white")
    frame.place(x=480, y=40)

    query_button = PhotoImage(width=1, height=1)
    settings_button = Button(ac, text="Hesap Bilgilerini Göster", image=query_button, command = query, width=250, height=40,
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 15))
    settings_button.place(x=500, y=290)






    ac.mainloop()



























###---------------------------------------------------------------------------Ana Ekran Bitiş

###---------------------------------------------------------------------------Giriş sayfasının ilk kısmı
root =Tk()
root.title("Giriş")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)
###---------------------------------------------------------------------------Kullanıcı adı ve şifrenin kontrolü(database eklenecek)

def signin():
    global count
    username=user.get()
    password=code.get()
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Users where username=? AND password=?",(username,password))
    row = c.fetchone()
    if row:
        messagebox.showinfo("başarılı","giriş başarılı")
        main_screen()
    else:
        messagebox.showinfo("hata","giriş başarısız")

#########################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def signup_command():
    window=Toplevel(root)
    window.title("Kayıt")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False,False)
###---------------------------------------------------------------------------Kullanıcı adı ve şifrenin kontrolü(database eklenecek)
    def register():
        username = user.get()
        password = code.get()
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        if code.get() == code_check.get():
            c.execute("CREATE TABLE IF NOT EXISTS Users (username TEXT,password TEXT)")
            c.execute("INSERT INTO Users (username,password) VALUES (?,?)",(username,password))
            user.delete(0,END)
            code.delete(0,END)
            code_check.delete(0,END)
            messagebox.showinfo("Başarılı","Başarıyla Giriş Yapıldı")
            window.destroy()
            root.deiconify()
        else :
            messagebox.showerror("Hata","Lütfen şifrenizi kontrol edin.")
            root.iconify()
        conn.commit()
        conn.close()



    def sign():
        window.destroy()
        root.deiconify()
###---------------------------------------------------------------------------Kullanıcı adı ve şifrenin kontrolü bitiş(database eklenecek)



    img =ImageTk.PhotoImage(file = "chess.jpg")
    Label(window, image=img,bg="white").place(x=-100,y=60)

    frame=Frame(window,width=348,height=350,bg="white")
    frame.place(x=480,y=40)

    heading=Label(frame,text="Kayıt Ol",fg="#201b17",bg="white",font=("Microsoft YaHei UI Light",23,"bold" ))
    heading.place(x=100,y=40)


###---------------------------------------------------------------------------Kullanıcı Adı Kısmı
    def on_enter(e):
        user.delete(0,"end")

    def on_leave(e):
        name=user.get()
        if name =="":
            user.insert(0,"Kullanıcı Adı")


    user = Entry(frame,width=25,fg="#201b17",border=0,bg="white",font=("Microsoft YaHei UI Light",11 ))
    user.place(x=30,y=100)
    user.insert(0,"Kullanıcı Adı")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg="black").place(x=25,y=124)
###---------------------------------------------------------------------------Şifre Kısmı
    def on_enter(e):
        code.delete(0,"end")

    def on_leave(e):
        name=code.get()
        if name =="":
            code.insert(0,"Şifre")

    code = Entry(frame,width=25,fg="#201b17",border=0,bg="white",font=("Microsoft YaHei UI Light",11 ))
    code.place(x=30,y=150)
    code.insert(0,"Şifre")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg="black").place(x=25,y=173)

###---------------------------------------------------------------------------Şifre Kontrol Kısmı

    def on_enter(e):
        code_check.delete(0,"end")

    def on_leave(e):
        name=code_check.get()
        if name =="":
            code_check.insert(0,"Şifre Doğrula")

    code_check = Entry(frame,width=25,fg="#201b17",border=0,bg="white",font=("Microsoft YaHei UI Light",11 ))
    code_check.place(x=30,y=198)
    code_check.insert(0,"Şifreyi Doğrula")
    code_check.bind("<FocusIn>", on_enter)
    code_check.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg="black").place(x=25,y=220)

###############################################################################
    Button(frame,width=39,pady=7,text="Kayıt Ol",bg="#201b17",fg="white",border=0,command=register).place(x=35,y=254)
    label = Label(frame,text="Hesabım var",fg ="black",bg="white",font=("Microsoft YaHei UI Light",9 ))
    label.place(x=75,y=297)

    sign_in = Button(frame,width=6,text="Giriş Yap",border=0,bg="#201b17",cursor="hand2",fg="white",command=sign)
    sign_in.place(x=200,y=297)


    window.mainloop()

#########################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###---------------------------------------------------------------------------Kullanıcı adı ve şifrenin kontrolü bitiş(database eklenecek)



img =ImageTk.PhotoImage(file = "chess.jpg")
Label(root, image=img,bg="white").place(x=-100,y=60)

frame=Frame(root,width=348,height=350,bg="white")
frame.place(x=480,y=40)

heading=Label(frame,text="Giriş Yap",fg="#201b17",bg="white",font=("Microsoft YaHei UI Light",23,"bold" ))
heading.place(x=100,y=40)


###---------------------------------------------------------------------------Kullanıcı Adı Kısmı
def on_enter(e):
    user.delete(0,"end")

def on_leave(e):
    name=user.get()
    if name =="":
        user.insert(0,"Kullanıcı Adı")


user = Entry(frame,width=25,fg="#201b17",border=0,bg="white",font=("Microsoft YaHei UI Light",11 ))
user.place(x=30,y=100)
user.insert(0,"Kullanıcı Adı")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=124)
###---------------------------------------------------------------------------Şifre Kısmı
def on_enter(e):
    code.delete(0,"end")

def on_leave(e):
    name=code.get()
    if name =="":
        code.insert(0,"Şifre")

code = Entry(frame,width=25,fg="#201b17",border=0,bg="white",font=("Microsoft YaHei UI Light",11 ))
code.place(x=30,y=150)
code.insert(0,"Şifre")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=173)

###############################################################################
Button(frame,width=39,pady=7,text="Giriş Yap",bg="#201b17",fg="white",border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="Hesabın yok mu?",fg ="black",bg="white",font=("Microsoft YaHei UI Light",9 ))
label.place(x=75,y=270)

sign_up = Button(frame,width=6,text="Kayıt Ol",border=0,bg="#201b17",cursor="hand2",fg="white",command=signup_command)
sign_up.place(x=200,y=270)


root.mainloop()