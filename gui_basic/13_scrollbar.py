from tkinter import*

root = Tk()
root.title('GUI|Python Learn')
root.geometry("640x480+300+300") 


# 스크롤 바는 스크롤바와 스크롤바의 대상이 되는 위젯을 
# 하나의 프레임에 집어 넣도록 하는게 관리가 편하다

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

# set 이 없으면 스크롤을 내려도 다시 올라옴.
listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand= scrollbar.set)

for i in range(1, 32): # 1 ~ 31 일
    listbox.insert(END, str(i) + '일')
listbox.pack(side='left')

# 리스트박스와 매핑을 해주어야 정상적으로 동작함
scrollbar.config(command=listbox.yview)

root.mainloop()