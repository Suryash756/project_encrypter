from tkinter import*

root = Tk()
root.title("encyrpter converter")
root.geometry("600x400")

root.configure(background = "lightblue")

head = Label(root,text="Ascii_and_encryption_converter",bg="darkblue",fg="white")
head.place(relx=0.5,rely=0.1,anchor=CENTER)


val = Entry(root)
val.place(relx = 0.5,rely= 0.5,anchor=CENTER)
label_ascii = Label(root,text="name in ascii : ",bg="snow",fg="black")
label_enc = Label(root,text="name in encryption : ",bg="snow",fg="black")

def conversion():
    data = str(val.get())
    for letter in data :
        ascii = int(ord(letter))
        label_ascii["text"] += str(ascii)
        enc = ascii + 1
        label_enc["text"] += str(chr(enc))
        
        
btn = Button(root,text="see the name in encryption and ascii code",command=conversion,bg="silver",fg="black")
btn.place(relx = 0.5,rely= 0.6,anchor=CENTER)
label_ascii.place(relx = 0.5,rely= 0.7,anchor=CENTER)
label_enc.place(relx = 0.5,rely= 0.8,anchor=CENTER)


root.mainloop()