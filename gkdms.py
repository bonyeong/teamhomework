from tkinter import*
from tkinter.filedialog import*
from tkinter.simpledialog import*

##함수 선언 부분##
def func_open():
    global filename
    filename=askopenfilename(parent=window, filetypes=(("GIF 파일","*.gif"),("모든 파일","*.*")))
    photo=PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image=photo


def func_exit():
    window.puit()
    window.destroy()

def func_expand():
    value1=askinteger("확대배수","확대할 배수를 입력하세요(2~8)",minvalue=2,maxvalue=8)
    photo=PhotoImage(file=filename)
    photo= photo.zoom(value1,value1)
    pLabel.configure(image=photo)
    pLabel.image=photo

def func_reduce():
    value2 = askinteger("축소배수", "축소할 배수를 입력하세요(2~8)", minvalue=2, maxvalue=8)
    photo = PhotoImage(file=filename)
    photo=photo.subsample(value2,value2)
    pLabel.configure(image=photo)
    pLabel.image=photo

##메인코드부분##

window =Tk()
window.geometry("400x400")
window.title("명화 감상하기")

photo=PhotoImage()
pLabel=Label(window,image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu=Menu(window)
window.config(menu=mainMenu)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일",menu=fileMenu)
fileMenu.add_command(label="파일 열기",command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램종료",command=func_exit)

imageMenu=Menu(mainMenu)
mainMenu.add_cascade(label="이미지효과", menu=imageMenu)
imageMenu.add_command(label="확대하기",command=func_expand)
imageMenu.add_separator()
imageMenu.add_command(label="축소하기",command=func_reduce)

window.mainloop()
