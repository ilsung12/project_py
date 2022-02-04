import os
import tkinter as tk
from tkinter import *

# main frame
root = tk.Tk()
root.title('제목 없음 - Window 메모장')
root.geometry("640x480+300+300") 

filename = 'mynote.txt'

def openFile():
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf8') as file:
            txt.delete('1.0', END)
            txt.insert(END, file.read())

def saveFile():
    with open(filename, 'w', encoding='utf8') as file:
        file.write(txt.get('1.0', END)) # 모든내용을 가져와서 저장

# menu
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='열기', command=openFile)
menu_file.add_command(label='저장', command=saveFile)
menu_file.add_separator()
menu_file.add_command(label='끝내기', command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집", menu=menu_file)
menu.add_cascade(label="서식", menu=menu_file)
menu.add_cascade(label="보기", menu=menu_file)
menu.add_cascade(label="도움말", menu=menu_file)

# scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')

# text
txt = tk.Text(root, yscrollcommand=scrollbar.set)
txt.pack(side='left', fill='both', expand=True)



scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()