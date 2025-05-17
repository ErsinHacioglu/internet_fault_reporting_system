import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import re
import tc_dogrulama

def email_dogru_mu(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

form = tk.Tk()
form.geometry('400x400')
form.config(bg='black')
form.title('Arıza Bildirim Uygulaması')

lbl_baslik = tk.Label(form, text='Arıza Bildirim Uygulaması', bg='black', fg='white', font='Times 17 bold')
lbl_baslik.pack()

kullanici_adi = tk.StringVar()
sifre = tk.StringVar()

lbl_ad = tk.Label(form, text='Kullanıcı Adı:', bg='black', fg='white', font='Times 13 bold')
lbl_ad.place(x=20, y=90)

lbl_sifre = tk.Label(form, text='Şifre:', bg='black', fg='white', font='Times 13 bold')
lbl_sifre.place(x=20, y=130)

entry_ad = tk.Entry(form, textvariable=kullanici_adi)
entry_sifre = tk.Entry(form, show='*', textvariable=sifre)
entry_ad.place(x=120, y=90)
entry_sifre.place(x=120, y=130)

def giris():
    if kullanici_adi.get() == 'ersin' and sifre.get() == '1234':
        msg = messagebox.showinfo('Tebrikler ', message='Giriş Başarılı')
        if msg == 'ok':
            basvuru_formu = tk.Toplevel()
            basvuru_formu.geometry('350x350')
            basvuru_formu.title('Arıza Bildirim Formu')
            basvuru_formu.config(bg='yellow')

            tk.Label(basvuru_formu, text='Arıza Bildirim Formu', bg='yellow', fg='red', font='Times 20 bold').pack()
            tk.Label(basvuru_formu, text='Ad Soyad:', font='consoles 15 italic', bg='yellow', fg='black').place(x=40, y=50)
            tk.Label(basvuru_formu, text='TC No:', font='consoles 15 italic', bg='yellow', fg='black').place(x=40, y=80)
            tk.Label(basvuru_formu, text='Modem Tipi:', font='consoles 15 italic', bg='yellow', fg='black').place(x=40, y=110)
            tk.Label(basvuru_formu, text='Arıza Tipi:', font='consoles 15 italic', bg='yellow', fg='black').place(x=40, y=140)
            tk.Label(basvuru_formu, text='Adres:', font='consoles 15 italic', bg='yellow', fg='black').place(x=40, y=170)
            tk.Label(basvuru_formu, text='Mail:', font='consoles 15 italic', bg='yellow', fg='black').place(x=40, y=200)

            entry_ad_soyad = tk.Entry(basvuru_formu)
            entry_ad_soyad.place(x=140, y=50)

            entry_tc = tk.Entry(basvuru_formu)
            entry_tc.place(x=140, y=80)

            modem_liste = ['Tmp', 'KMNR', '2TMYS', 'MTPL', 'NYPM', 'PNDS']
            combo_modem = Combobox(basvuru_formu, values=modem_liste)
            combo_modem.place(x=140, y=110)

            ariza_liste = ['arıza1', 'arıza2', 'arıza3', 'arıza4', 'arıza5']
            combo_ariza = Combobox(basvuru_formu, values=ariza_liste)
            combo_ariza.place(x=140, y=140)

            entry_adres = tk.Entry(basvuru_formu)
            entry_adres.place(x=140, y=170)

            entry_mail = tk.Entry(basvuru_formu)
            entry_mail.place(x=140, y=200)

            def olustur():
                tc_kosul = tc_dogrulama.Tc(entry_tc.get())
                email_kosul = email_dogru_mu(entry_mail.get())

                if not tc_kosul:
                    messagebox.askretrycancel('Başarısız', 'TC kimlik numaranızı doğru girdiğinize emin olunuz!')
                elif not email_kosul:
                    messagebox.askretrycancel('Başarısız', 'Lütfen geçerli bir e-posta adresi giriniz!')
                else:
                    messagebox.showinfo('Başarıyla oluştu', 'Arıza bildiriminiz alınmıştır.')

            tk.Button(basvuru_formu, text='oluştur', command=olustur).place(x=140, y=240)

def iptal():
    form.destroy()

btn_giris = tk.Button(form, text='   Giriş     ', activebackground='green', command=giris)
btn_iptal = tk.Button(form, text='   İptal     ', activebackground='red', command=iptal)
btn_giris.place(x=120, y=180)
btn_iptal.place(x=220, y=180)

form.mainloop()
