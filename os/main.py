import tkinter
d = tkinter.Tk()

w = 1280
h = 720
newButton = tkinter.Button
newText = tkinter.Label

d.config(height=h,width=w,bg="black")
d.attributes('-fullscreen',True)

ce0 = newButton(d,height=64,width=64,image="PyOS/1.bmp")

ce0.place(x=40,y=40)
d.mainloop()