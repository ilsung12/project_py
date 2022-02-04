import tkinter.messagebox as msgbox
from tkinter import*

root = Tk()
root.title('GUI|Python Learn')
root.geometry("640x480+300+300") 

# 기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo('알림', '정상적으로 예매 완료되었습니다.')

def warn():
    msgbox.showwarning('경고', '해당 좌석은 매진되었습니다.')

def error():
    msgbox.showerror('에러', '결제 오류가 발생했습니다.')

def okcancel():
    msgbox.askokcancel('예매', '해당 좌석은 유아동반석입니다. 예매하시겠습니까?')

def retrycancel():
    res = msgbox.askretrycancel('예매', '일시적인 오류입니다. 다시 시도하시겠습니까?')
    print('응답: ', res) # True, False, None => 예 1, 아니오 0, 그 외
    if res == 1: # 재시도
        print('재시도')
    elif res == 0: # 취소, 
        print('취소')
    

def yesno():
    msgbox.askyesno('예 / 아니오', '해당 좌석은 역방향입니다. 예매하시겠습니까?')

def yesnocancel():
    res = msgbox.askyesnocancel(title=None, message='예매 내역이 저장되지 않았습니다. \n 저장 후 종료하시겠습니까?')
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재화면에서 계속 작업 )
    print('응답: ', res) # True, False, None => 예 1, 아니오 0, 그 외
    if res == 1: # 네, OK
        print('예')
    elif res == 0:
        print('아니오')
    else:
        print('취소')


Button(root, command=info, text='알림').pack()
Button(root, command=warn, text='경고').pack()
Button(root, command=error, text='에러').pack()
Button(root, command=okcancel, text='예매').pack()
Button(root, command=retrycancel, text='예매').pack()
Button(root, command=yesno, text='예 아니오').pack()
Button(root, command=yesnocancel, text='예 아니오 취소').pack()



root.mainloop()