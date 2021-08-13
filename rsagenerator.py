#Nyarlko Simple RSA Key Generator
import rsa;from tkinter.ttk import *;from tkinter import *;
w=Tk();w.title('Nyarlko RSA Key Generator');w.configure(background='black')
def newKey():
    global prve,pbe,keylene
    prve.delete(0,END);pbe.delete(0,END);
    key_lenght=int(keylene.get())
    publicKey,privateKey=rsa.newkeys(int(key_lenght))
    prve.insert(0, privateKey);pbe.insert(0, publicKey)
#Keylen
keylen=Label (w, text="Lenght:" ,bg="black",fg="white",font="none 12 bold");keylen.grid(row=0,column=0,sticky=W)
keylene=Entry(w,width=40,bg="white");keylene.grid(row=0,column=1,sticky=W)
keylene.insert(0, "1024")
#PublicKey Label
pb=Label (w, text="Public:" ,bg="black",fg="white",font="none 12 bold");pb.grid(row=2,column=0,sticky=W)
pbe=Entry(w,width=40,bg="white");pbe.grid(row=2,column=1,sticky=W)
#PrivateKey Label
prv=Label (w, text="Private:" ,bg="black",fg="white",font="none 12 bold");prv.grid(row=3,column=0,sticky=W)
prve=Entry(w,width=40,bg="white");prve.grid(row=3,column=1,sticky=W)
#info
info=Label (w, text="Copy: CTRL+C" ,bg="black",fg="white",font="none 12 bold");info.grid(row=4,column=0,sticky=W)
info2=Label (w, text="Paste: CTRL+V" ,bg="black",fg="white",font="none 12 bold");info2.grid(row=4,column=1,sticky=W)
#GenerateNewKey Button
newKeyButton=Button(w,text="Generate New",width=12,font="none 12 bold",command=newKey)
newKeyButton.grid(row=5,column=1,sticky=W)
w.mainloop()
sys.exit(0)
