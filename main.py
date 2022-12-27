from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import webbrowser



###---------------------------------------------------------------------------Ana Ekran

def main_screen():
    def link():
        webbrowser.open_new(r"https://www.chess.com/learn")

    window = Toplevel()
    window.title("Chess")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False)
    window.iconbitmap("chess.ico")

    img = ImageTk.PhotoImage(file="chess.jpg")
    Label(window, image=img, bg="white").place(x=-100, y=60)

    frame = Frame(window, width=348, height=350, bg="white")
    frame.place(x=480, y=40)

    common_img1 = PhotoImage(width=1, height=1)
    new_game_button = Button(window, text="Yeni Oyun", image=common_img1, width=290, height=70, ###-----Satranç Yeni Oyun Başlangıç Butonu
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 15))

    new_game_button.place(x=500, y=90)

    common_img2 = PhotoImage(width=1, height=1)
    ongoing_games_button = Button(window, text="Devam Eden Oyunlarım", image=common_img2, width=290, height=70,###-----Satranç Devam Eden Oyun Butonu
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 15))

    ongoing_games_button.place(x=500, y=190)

    common_img3 = PhotoImage(width=1, height=1)
    settings_button = Button(window, text="Nasıl Oynanır?", image=common_img3, width=290, height=70,
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 15), command=link)

    settings_button.place(x=500, y=290)

    common_img4 = PhotoImage(width=1, height=1)
    account_settings_button = Button(window, text="Hesap Ayarları", image=common_img4, width=140, height=20,
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 10), command = account_settings)

    account_settings_button.place(x=770, y=5)

    admin_panel_button = Button(window, text="Admin Paneli", image=common_img4, width=140, height=20,
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 10), command = admin_panel)

    admin_panel_button.place(x=600, y=5)

    window.mainloop()



def admin_panel():


    ac = Toplevel()
    ac.title("Admin Paneli")
    ac.geometry("400x400")
    ac.configure(bg="#fff")
    ac.resizable(False, False)
    ac.iconbitmap("chess.ico")






    def query():
        conn = sqlite3.connect("users.db")

        c = conn.cursor()

        c.execute("SELECT *, oid FROM users")
        records = c.fetchall()
        print(records)

        print_records = ""
        for record in records:
            print_records += str(record[0]) + "\t" + str(record[1]) + "\t " + str(record[2]) + "\n"



        query_label = Label(ac, text=print_records, bg="white", font=23)
        query_label.grid(row=8, column=0, columnspan=2)
        query_label.place(x=150, y=10)

    frame = Frame(ac, width=348, height=350, bg="white")
    frame.place(x=480, y=40)

    common_img5 = PhotoImage(width=1, height=1)
    query_button = Button(ac, text="Kullanıcı Adı, Şifre ve ID'yi Görüntüle", image=common_img5, width=250, height=20,
                          compound="c", bg="#201b17", fg="white",
                          activebackground="white", font=("Arial", 10), command=query)
    query_button.place(x=80, y=90)

    common_img7 = PhotoImage(width=1, height=1)
    account_settings_button = Button(ac, text="Yeni Hesap Ekle", image=common_img7, width=140, height=20,
                                     compound="c", bg="#201b17", fg="white",
                                     activebackground="white", font=("Arial", 10), command= admin_add_member)
    account_settings_button.place(x=120, y=250)

    ###---------------------------------------------------------------------------Hesabı Silme

    def delete():
        conn = sqlite3.connect("users.db")

        c = conn.cursor()

        c.execute("DELETE from users WHERE oid=" + delete_box.get())

        conn.commit()
        conn.close()

    common_img4 = PhotoImage(width=1, height=1)
    account_settings_button = Button(ac, text="Hesabı Sil", image=common_img4, width=140, height=20,
                                     compound="c", bg="#201b17", fg="white",
                                     activebackground="white", font=("Arial", 10), command=delete)
    account_settings_button.place(x=120, y=180)

    delete_box = Entry(ac, width=30)
    delete_box.grid(row=11, column=1)
    delete_box.place(x=160, y=130)
    delete_box_label = Label(ac, text="ID Numaranızı Girin")
    delete_box_label.place(x=30, y=130)








    ac.mainloop()

def admin_add_member():
    signup_command()




###---------------------------------------------------------------------------Hesap Ayarları

def account_settings():

    ac = Toplevel()
    ac.title("Hesap Ayarları")
    ac.geometry("400x400")
    ac.configure(bg="#fff")
    ac.resizable(False, False)
    ac.iconbitmap("chess.ico")


    user_label = Label(ac, text="Kullanıcı Adınız:")
    user_label.grid(row=9, column=0)
    user_label.place(x=80, y= 10)

    username_label = Label(ac, text=user.get(), bg="white", font = 23)
    username_label.grid(row = 9,column=5,columnspan=2)
    username_label.place(x=190, y=10)

###---------------------------------------------------------------------------Kullanıcı Adı Güncelleme Butonu

    def username_update():
            win = Toplevel()
            window_width = 350
            window_height = 350
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()
            position_top = int(screen_height / 4 - window_height / 4)
            position_right = int(screen_width / 2 - window_width / 2)
            win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
            win.title('Kullanıcı Adı Güncelleme')
            win.configure(background='#f8f8f8')
            win.resizable(0, 0)
            win.iconbitmap("chess.ico")

            user = StringVar()
            password = StringVar()
            confirmPassword = StringVar()

            user_entry2 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                                textvariable=user)
            user_entry2.place(x=40, y=30, width=256, height=34)
            user_entry2.config(highlightbackground="black", highlightcolor="black")
            user_label2 = Label(win, text='• Eski Kullanıcı Adı', fg="#89898b", bg='#f8f8f8',
                                font=("yu gothic ui", 11, 'bold'))
            user_label2.place(x=40, y=0)

            new_user_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12),
                                       highlightthickness=2,
                                       textvariable=password)
            new_user_entry.place(x=40, y=110, width=256, height=34)
            new_user_entry.config(highlightbackground="black", highlightcolor="black")
            new_user_label = Label(win, text='• Yeni Kullanıcı Adı', fg="#89898b", bg='#f8f8f8',
                                       font=("yu gothic ui", 11, 'bold'))
            new_user_label.place(x=40, y=80)

            confirm_user_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12),
                                           highlightthickness=2
                                           , textvariable=confirmPassword)
            confirm_user_entry.place(x=40, y=190, width=256, height=34)
            confirm_user_entry.config(highlightbackground="black", highlightcolor="black")
            confirm_user_label = Label(win, text='• Yeni Kullanıcı Adını Doğrula', fg="#89898b", bg='#f8f8f8',
                                           font=("yu gothic ui", 11, 'bold'))
            confirm_user_label.place(x=40, y=160)

            update_pass = Button(win, fg='#f8f8f8', text='Kullanıcı Adını Güncelle', bg='#201b17',
                                 font=("yu gothic ui bold", 14),
                                 cursor='hand2', activebackground='#201b17', command=lambda: change_username())
            update_pass.place(x=40, y=240, width=256, height=50)

            def change_username():
                if new_user_entry.get() == confirm_user_entry.get():
                    db = sqlite3.connect("users.db")
                    curs = db.cursor()

                    insert = '''update users set username=? where username=? '''
                    curs.execute(insert, [new_user_entry.get(), user_entry2.get(), ])
                    db.commit()
                    db.close()
                    messagebox.showinfo('Başarılı!', 'Kullanıcı Adınız başarıyla değiştirildi!')

                else:
                    messagebox.showerror('Hata!', "Kullanıcı Adınız eşleşmedi!")


 ###---------------------------------------------------------------------------Kullanıcı Adı Güncelleme Bitiş

###---------------------------------------------------------------------------Şifre Güncelleme


    def password_update():
        forgot_command()
        pass
###---------------------------------------------------------------------------Şifre Güncelleme Bitiş


###---------------------------------------------------------------------------Hesap Bilgileri

    def query():
        conn = sqlite3.connect("users.db")

        c = conn.cursor()

        c.execute("SELECT *, oid FROM users")
        records = c.fetchall()
        print(records)

        print_records = ""
        for record in records:
            if record[0] == user.get():

                id_number_label = Label(ac, text="ID Numaranız:")
                id_number_label.grid(row=9, column=0)
                id_number_label.place(x=80, y=35)

                id_label = Label(ac, text=str(record[2]), bg="white", font=23)
                id_label.grid(row=9, column=0)
                id_label.place(x=190, y=35)

                code_label = Label(ac, text="Şifreniz:")
                code_label.grid(row=9, column=0)
                code_label.place(x=80, y=60)

                password_label = Label(ac, text=str(record[1]), bg="white", font=23)
                password_label.grid(row=9, column=0)
                password_label.place(x=190, y=60)

        query_label = Label(ac, text=print_records, bg="white", font=23)
        query_label.grid(row=8, column=0, columnspan=2)
        query_label.place(x = 150, y= 150)


    frame = Frame(ac, width=348, height=350, bg="white")
    frame.place(x=480, y=40)

    common_img5 = PhotoImage(width=1, height=1)
    query_button = Button(ac, text="Şifre ve ID'yi Görüntüle", image=common_img5, width=140, height=20,
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 10), command=query)
    query_button.place(x=130, y=90)

###---------------------------------------------------------------------------Hesabı Silme

    def delete():
        conn = sqlite3.connect("users.db")

        c = conn.cursor()

        c.execute("DELETE from users WHERE oid=" + delete_box.get())


        conn.commit()
        conn.close()

    common_img4 = PhotoImage(width=1, height=1)
    account_settings_button = Button(ac, text="Hesabı Sil", image=common_img4, width=140, height=20,
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 10), command = delete)
    account_settings_button.place(x=120, y=180)

    delete_box = Entry(ac,width=30)
    delete_box.grid(row=11,column=1)
    delete_box.place(x=160,y=130)
    delete_box_label =Label(ac,text="ID Numaranızı Girin")
    delete_box_label.place(x=30, y=130)

    common_img6 = PhotoImage(width=1, height=1)
    account_settings_button = Button(ac, text="Şifremi Güncelle", image=common_img6, width=140, height=20,
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 10), command = password_update)
    account_settings_button.place(x=50, y=220)

    common_img7 = PhotoImage(width=1, height=1)
    account_settings_button = Button(ac, text="Kullanıcı Adımı Güncelle", image=common_img7, width=140, height=20,
                   compound="c", bg="#201b17", fg="white",
                   activebackground="white", font=("Arial", 10), command = username_update)
    account_settings_button.place(x=220, y=220)




    ac.mainloop()
###---------------------------------------------------------------------------Hesap Bilgileri Bitiş


###---------------------------------------------------------------------------Ana Ekran Bitiş

###---------------------------------------------------------------------------Giriş sayfasının ilk kısmı

root =Tk()
root.title("Giriş")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)
root.iconbitmap("chess.ico")


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
        messagebox.showinfo("Başarılı!","Başarıyla Giriş Yapıldı!")
        main_screen()
    else:
        messagebox.showinfo("Başarısız!","Giriş Başarısız Oldu!")

#########################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

###---------------------------------------------------------------------------Şifremi Unuttum Kısmı

def forgot_command():
    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.title('Şifre Güncelleme')
    win.configure(background='#f8f8f8')
    win.resizable(0, 0)
    win.iconbitmap("chess.ico")


    user = StringVar()
    password = StringVar()
    confirmPassword = StringVar()


    user_entry2 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                         textvariable=user)
    user_entry2.place(x=40, y=30, width=256, height=34)
    user_entry2.config(highlightbackground="black", highlightcolor="black")
    user_label2 = Label(win, text='• Kullanıcı Adı', fg="#89898b", bg='#f8f8f8',
                         font=("yu gothic ui", 11, 'bold'))
    user_label2.place(x=40, y=0)


    new_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
                               textvariable=password)
    new_password_entry.place(x=40, y=110, width=256, height=34)
    new_password_entry.config(highlightbackground="black", highlightcolor="black")
    new_password_label = Label(win, text='• Yeni Şifre', fg="#89898b", bg='#f8f8f8',
                               font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=80)


    confirm_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2
                                   , textvariable=confirmPassword)
    confirm_password_entry.place(x=40, y=190, width=256, height=34)
    confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
    confirm_password_label = Label(win, text='• Yeni Şifreyi Doğrula', fg="#89898b", bg='#f8f8f8',
                                   font=("yu gothic ui", 11, 'bold'))
    confirm_password_label.place(x=40, y=160)


    update_pass = Button(win, fg='#f8f8f8', text='Şifreyi Güncelle', bg='#201b17', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#201b17', command=lambda: change_password())
    update_pass.place(x=40, y=240, width=256, height=50)


    def change_password():
        if new_password_entry.get() == confirm_password_entry.get():
            db = sqlite3.connect("users.db")
            curs = db.cursor()

            insert = '''update users set Password=? where username=? '''
            curs.execute(insert, [new_password_entry.get(), user_entry2.get(), ])
            db.commit()
            db.close()
            messagebox.showinfo('Başarılı!', 'Şifreniz başarıyla değiştirildi!')

        else:
            messagebox.showerror('Hata!', "Şifreleriniz eşleşmedi!")





def signup_command():
    window=Toplevel(root)
    window.title("Kayıt")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False,False)
    window.iconbitmap("chess.ico")

###---------------------------------------------------------------------------Kullanıcı adı ve şifrenin kontrolü
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
###---------------------------------------------------------------------------Kullanıcı adı ve şifrenin kontrolü bitiş



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

code = Entry(frame,width=25,fg="#201b17",border=0,bg="white",show='•',font=("Microsoft YaHei UI Light",11 ))
code.place(x=30,y=150)
code.insert(0,"Şifre")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=173)

###############################################################################
Button(frame,width=39,pady=7,text="Giriş Yap",bg="#201b17",fg="white",border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="Hesabın yok mu?",fg ="black",bg="white",font=("Microsoft YaHei UI Light",9 ))
label.place(x=75,y=270)

label = Label(frame,text="Şifremi unuttum",fg ="black",bg="white",font=("Microsoft YaHei UI Light",9 ))
label.place(x=75,y=300)

forgot_button = Button(frame,width=10,text="Şifremi sıfırla",border=0,bg="#201b17",cursor="hand2",fg="white",command=forgot_command)
forgot_button.place(x=200,y=300)

sign_up = Button(frame,width=6,text="Kayıt Ol",border=0,bg="#201b17",cursor="hand2",fg="white",command=signup_command)
sign_up.place(x=200,y=270)


root.mainloop()