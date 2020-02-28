import base64
from tkinter import *
from Crypto.Cipher import AES

private_key='HESAAZIXCLIY137A'

def encryption(privateInfo):
    BLOCK_SIZE=16
    PADDING='{'
    pad=lambda s: s+(BLOCK_SIZE - len(s)%BLOCK_SIZE)*PADDING
    EncodeAES=lambda c,s: base64.b64encode(c.encrypt(pad(s)))
    secret=private_key
    cipher=AES.new(secret)
    encoded=EncodeAES(cipher,privateInfo)
    l.config(text='Encrypted message: %s'%encoded)
    print(encoded)

def decryption(encryptedString):
    PADDING='{'
    DecodeAES=lambda c, e: c.decrypt(base64.b64decode(e)).decode('utf-8').rstrip(PADDING)
    key=private_key
    cipher=AES.new(key)
    decoded=DecodeAES(cipher, encryptedString)
    print('Decoded:',decoded)

def _copyright():
    win=Toplevel()
    message="No rights reserved."
    Label(win,text=message).pack(fill="both",padx=50,pady=50)

def what_is():
    win=Toplevel()
    message=("Encrypt-Decrypt messages using python 3.x and AES and PyCrypto using "+private_key+" as private key .")
    Label(win,text=message).pack(fill="both",padx=100,pady=70)

#GUI
root=Tk()
root.geometry("700x300")
root.title("Encrypt-Decrypt Messages")
l0=Label(root,text="Type a message to be encrypted or decrypted in their respective boxes: ")
l0.grid(row=0,column=0,columnspan=30)
l=Label(root)
l.grid(row=5,column=0,columnspan=3000)

e1=Entry(root)
e1.grid(row=1,column=1)
l1=Label(root,text="Message to be encrypted.")
l1.grid(row=1,column=0)
e2=Entry(root)
e2.grid(row=2,column=1)
l2=Label(root,text="Message to be decrypted.")
l2.grid(row=2,column=0)

b=Button(root,text="Result of encryption",command=lambda: encryption(e1.get()))
b.grid(row=1,column=2)

b1=Button(root,text="Result of decryption",command=lambda: decryption(e2.get()))
b1.grid(row=2,column=2)

menubar=Menu(root)
root.config(menu=menubar)
aboutmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="About",menu=aboutmenu)
aboutmenu.add_command(label="What is...",command=what_is)
aboutmenu.add_command(label="Copyright",command=_copyright)

mainloop()
