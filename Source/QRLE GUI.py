from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import webbrowser
import qrcode


def clicked():
    url = QR.get()
    name = "QR.png"
    png = qrcode.make(url)
    png.save(name)
    question = mb.askyesno(title="Dialog window", message="Open a ready-made QR code?")
    if question:
        png.show()
    else:
        mb.showinfo("INFO", "Your QR code is ready!")


def clicked2():
    answer = mb.askyesno(title="Redirecting", message="Open author feedback?")
    if answer:
        webbrowser.open("https://t.me/qrle_bot", new=2)
    else:
        pass


root = Tk()
root.configure(background="#b3b3b3")
root.title("QRLE GUI")
root.iconbitmap("icon.ico")
root.geometry("300x300")

img = Image.open("logo.jpg")
image = ImageTk.PhotoImage(img)

initil = Label(root, image=image)
initil.grid(padx=0, pady=0)

text = Label(root, text="Provide link/text", bg="#b3b3b3", fg="#ffffff", font="Arial 13")
text.grid(padx=0, pady=0)

QR = Entry(root, width=20, bg="#dedede")
QR.grid(padx=0, pady=0)

button = Button(root, text="     Build     ", command=clicked, background="#000000", fg="#ffffff", height=2)
button.grid(padx=6, pady=6)

help = Button(root, text="     Help     ", command=clicked2, background="#000000", fg="#ffffff", height=1)
help.grid(padx=6, pady=8)

root.mainloop()
