from tkinter import*

root = Tk()
root.title('GUI|Python Learn')
root.geometry("640x480+300+300") 



def btncmd():
    pass

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()