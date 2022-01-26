from tkinter import*
from turtle import width

root = Tk()
root.title('GUI|Python Learn')
root.geometry("640x480+300+300") 

# 여러줄
txt = Text(root, width=30, height=5)
txt.pack()
# 기본값 제공
txt.insert(END, "글자를 입력하세요.")


# 한줄
e = Entry(root, width=30)
e.pack()
e.insert(0, '한 줄만 입력하세요')


def btncmd():
    # 내용 출력
    # 1: 첫번째 라인부터 가져와라 
    # 0: 0번짜 컬럼 위치부터 가져와라
    # END: 기본값
    print(txt.get("1.0", END)) 
    print(e.get())

    # 내용 삭제
    txt.delete('1.0', END)
    e.delete(0, END)
    

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()