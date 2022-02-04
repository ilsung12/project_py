# pip install keyboard
import keyboard
import time
from PIL import ImageGrab


def screenshot():
    # 2022년 1월 1일 10시 20분 30초 -> _20220101_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save('image{}.png'.format(curr_time)) # ex) image_20220101_102030.png

keyboard.add_hotkey('F9', screenshot) # 사용자가 F9 키를 누르면 스크린샷 저장
#keyboard.add_hotkey('crtl+shift+s', screenshot) 

keyboard.wait('esc') # 사용자가 ESC 를 누를때까지 프로그램 수행