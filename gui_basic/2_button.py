from tkinter import*
from tkinter import messagebox

root = Tk()
root.title('GUI|Python Learn')

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text='버튼2')
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text='버튼3')
btn3.pack()

# w,h => margin, padding 값 없이 만들어짐 (text가 늘어나도 반응 x)
btn4 = Button(root, width=10, height=3, text='버튼4')
btn4.pack()

btn5 = Button(root, fg='red', bg='yellow', text='버튼5')
btn5.pack()

photo = PhotoImage(file='gui_basic/img.png')
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print('버튼이 클릭되었어요')

btn7 = Button(root, text='동작하는 버튼', command=btncmd)
btn7.pack()


root.mainloop()