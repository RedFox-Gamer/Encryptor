#pip install onetimepad
import onetimepad
from tkinter import *

#Name of the app and Window Size
root = Tk()
root.title("Encrypt / Decrypt by Adam Stark")
root.geometry("1920x1080")

def encryptMessage():
    pt = e1.get()
    ct = onetimepad.encrypt(pt, 'random')
    e2.insert(0, ct)

def decryptMessage():
    ct1 = e3.get()
    pt1 = onetimepad.decrypt(ct1, 'random')
    e4.insert(0, pt1)

#Creating Label
label1 = Label(root, text='Base Text')
label1.grid(row=10, column=1)
label2 = Label(root, text='Encrypted Text')
label2.grid(row=11, column=1)
label3 = Label(root, text='Encrypted Text') 
label3.grid(row=10, column=11)
label4 = Label(root, text='Decrypted Text')
label4.grid(row=11, column=11)

#Creating entires
e1 = Entry(root)
e1.grid(row=10, column=2)
e2 = Entry(root)
e2.grid(row=11, column=2)
e3 = Entry(root)
e3.grid(row=10, column=12)
e4 = Entry(root)
e4.grid(row=11, column=12)

#Creating the buttons
#Encrypt:
ent = Button(root, text='Encrypt', bg="red", fg="white", command=encryptMessage)
ent.grid(row=12, column=2)

#Decrypt:
b2 = Button(root, text='Decrypt', bg="green", fg="white", command=decryptMessage)
b2.grid(row=12, column=12)

root.mainloop()