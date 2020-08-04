# -*- coding: utf-8 -*- 
import pyautogui as pg
import tkinter as tk
from tkinter import messagebox as msg
import time

import inko

def to_Eng(s):
    i=inko.Inko()
    return i.ko2en(s)

def main():
    t=text.get("1.0","end")
    t=to_Eng(t)
    msg.showinfo("Typewriter v.1.0", "입력을 원하는 곳을 클릭하고 3초 정도 기다리십시오.\n독후감의 길이에 따라 일정 시간이 소요될 수 있습니다.\n창을 끄지 말고 기다려주세요.")

    time.sleep(3)
    pg.typewrite(t)

global a

w=tk.Tk()
w.title("Typewriter v.1.0")
w.geometry("700x700")
w.resizable(False, False)

text=tk.Text(w,width=100,height=45)

b1=tk.Button(w,width=350,height=10,text="붙여넣기",command=main)

l=tk.Label(w,width=100,height=3,anchor="e",justify="right",bg="white",
           text="독서교육종합지원시스템 복사/붙여넣기 스크립트 \ncredit: 19191 최종엽, 19159 전서준 ")
l.pack()
text.pack()
b1.pack()


w.mainloop()
