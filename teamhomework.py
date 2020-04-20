from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *

def func_open():
    global filename
    filename = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file=filename)
    label1.configure(image=photo)
    label1.image = photo


def func_exit():
    window.quit()
    window.destroy()


def func_zoom():
    value = askinteger("확대배수", "확대할 배수를 입력하세요(2~8)", minvalue=2, maxvalue=8)
    photo = PhotoImage(file=filename)
    photo = photo.zoom(value, value)
    label1.configure(image=photo)
    label1.image = photo


def func_sub():
    value = askinteger("축소배수", "축소할 배수를 입력하세요(2~8)", minvalue=2, maxvalue=8)
    photo = PhotoImage(file=filename)
    photo = photo.subsample(value, value)
    label1.configure(image=photo)
    label1.image = photo


window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

photo = PhotoImage()
label1 = Label(window, image=photo)
label1.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

imageMenu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지효과", menu=imageMenu)
imageMenu.add_command(label="확대하기", command=func_zoom)
imageMenu.add_separator()
imageMenu.add_command(label="축소하기", command=func_sub)

window.mainloop()
