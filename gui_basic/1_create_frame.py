from tkinter import*

root = Tk()
root.title('GUI|Python Learn')
# root.geometry("640x480") # 가로 * 세로
root.geometry("640x480+300+300") # 가로 * 세로 + x 좌표 + y 좌표

# root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창크기변경 x)


# 창이 닫히지 않도록 이벤트루프를 돌린다.
root.mainloop()