from tkinter import *
from tkinter import messagebox
import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def saveandencryptnotes():
    title = entrytitle.get()
    mesaj = textinput.get("1.0",END)
    mastersecret = mastersecretinput.get()

    if len(title) == 0 or len(mesaj) == 0 or len(mastersecret) == 0:
        messagebox.showinfo(title="Error!",message="Please Enter All Info")

    else:
        message_encrypted = encode(mastersecret,mesaj)
        try:
            with open("mysecret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            entrytitle.delete(0,END)
            mastersecretinput.delete(0,END)
            textinput.delete("1.0",END)

def dekripnot():
    message_encrpyted = textinput.get("1.0",END)
    mastersecret = mastersecretinput.get()

    if len(message_encrpyted) == 0 or len(mastersecret) == 0:
        messagebox.showinfo(title="Error!",message="Please Enter All Info")

    else:
        try:
            decryptedmessage = decode(mastersecret,message_encrpyted)
            textinput.delete("1.0",END)
            textinput.insert("1.0",decryptedmessage)
        except:
            messagebox.showinfo(title="Error!",message="Please Enter Encrypted Text")


window = Tk()

window.title("Secret Notes")
punto = ("Verdana",20,"normal")
window.config(padx=30,pady=30,bg="light blue")



photo = PhotoImage(file="shit.png")
photolabel = Label(image=photo,bg="light blue")
photolabel.pack()

titleinfolabel = Label(text="Enter Your Title",font=punto,bg="light blue")
titleinfolabel.pack()

entrytitle = Entry(width=30)
entrytitle.pack()

inputinfolabel = Label(text="Enter Your Secret",bg="light blue",font=punto)
inputinfolabel.pack()

textinput = Text(width=50,height=25)
textinput.pack()

mastersecretlabel = Label(text="Enter Master Key",font=punto,bg="light blue")
mastersecretlabel.pack()

mastersecretinput = Entry(width=30)
mastersecretinput.pack()

savebutton = Button(text="Save and Encrypt",command=saveandencryptnotes)
savebutton.pack()

decripbutton = Button(text="Decrypt",command=dekripnot)
decripbutton.pack()



window.mainloop()
