import tkinter.ttk as ttk # ttk 안에 콤보박스 있음
from tkinter import* 

root = Tk()
root.title('GUI|Python Learn')
root.geometry("640x480+300+300") 

values = [str(i) + '일' for i in range(1,32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set('카드 결제일') # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state='readonly')
readonly_combobox.current(0) # 0번쨰 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get()) # 선택된 값 표시

btn = Button(root, text='선택', command=btncmd)
btn.pack()

root.mainloop()