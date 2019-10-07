from tkinter import *

# 다이얼 로그를 이용한 파일 열기
from tkinter import filedialog, messagebox


def open():
    file = filedialog.askopenfile(parent=win, mode="r")

    if file != None:
        txt.delete('1.0', END)  # 기존 내용 지우기

        lines = file.read()

        txt.insert('1.0', lines)

        file.close()


# 다이얼 로그를 이용한 파일 저장하기

def save():
    file = filedialog.askopenfile(parent=win, mode="w")

    if file != None:
        lines = txt.get('1.0', END + '-1c')  # 맨 마지막 한 문자 제거후 저장

        file.write(lines)

        file.close()


# 프로그램 종료하기

def exit():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
        win.destroy()


def about():
    label = messagebox.showinfo("About", "메모장 프로그램")


win = Tk()

txt = Text(win, height=30, width=80)  # Text 위젯 사용

txt.pack()

# 메뉴 추가

menu = Menu(win)

win.config(menu=menu)

# 파일 메뉴 추가

filemenu = Menu(menu)

menu.add_cascade(label="파일", menu=filemenu)

filemenu.add_command(label="열기", command=open)

filemenu.add_command(label="저장하기", command=save)

filemenu.add_command(label="종료", command=exit)

# 도움말 메뉴 추가

helpMenu = Menu(menu)

menu.add_cascade(label="도움말", menu=helpMenu)

helpMenu.add_command(label="프로그램 정보", command=about)

win.mainloop()