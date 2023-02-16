import tkinter
window = tkinter.Tk()
height = 240; width = 320
window.config(width=width, height=height, bg="black")
window.title("File Formatter")
NewButton = tkinter.Button
NewLabel = tkinter.Label
NewTextField = tkinter.Text

offseth = 2048
offseth2 = 64512

def getval():
    global a
    a = t1.get("1.0",tkinter.END+"-1c")


def format(file:str):
    from os import path
    f = open(file,"r+b")
    f.seek(0)
    f.write(b"\x04\x55\x20\x23")
    f.write(b"\x00" * (path.getsize(a) - 4))
    print(f"Format finished on file {a}!")

def writestr(file:str, offset:int,content:str | bytes):
    f = open(file,"r+b")
    f.seek(offset)
    f.write(content)

l1 = NewLabel(window,text=f"""
This little program erases EVERY BYTE in a file.
If you have important stuff in it, back them up!

Type the location into the textbox below,
then press the button.
""",bg="black",fg="white",font="system")
b1 = NewButton(window, width=20, height=2, font=("Arial",10), text="Format", command=lambda:[getval(),format(a)])
t1 = NewTextField(window, width=40,height=1, border=2, font=("Consolas",10))

l1.place(x=width/2,y=height/2-30,anchor="center")
b1.place(x=width/2, y=height-25, anchor="center")
t1.place(x=width/2, y=height/2+50, anchor="center")
# Anchor Values: "nw", "n", "ne", "w", "center", "e", "sw", "s", "se"

window.mainloop()