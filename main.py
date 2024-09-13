import tkinter
import random
import time
import _thread
import sys
import math
# 画面作成
version = tkinter.Tcl().eval('info patchlevel')
root = tkinter.Tk()
canvas = tkinter.Canvas(width=1920, height=1080, bg="white")
canvas.pack()
root.title("Matibari")
key = ""
count1 = 0
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""
def byouga():
    global oval_size, key, hari, before_key, deg, lv
    try:
        canvas.delete("hari", "oval", "texts")
        canvas.create_oval(640 - oval_size, 100, 640 + oval_size, oval_size * 2 + 100, fill="white", tag="oval")
        deg -= 0.05
        top_x = 640
        top_y = 100 + oval_size
        for i in range(len(haris)):
            canvas.create_line(top_x + math.sin(haris[i] + deg * -1) * oval_size, top_y + math.cos(haris[i] + deg * -1) * oval_size, top_x + math.sin(haris[i] + deg * -1) * (oval_size + 200), top_y + math.cos(haris[i] + deg * -1) * (oval_size + 200), tag="hari", width=10)
            canvas.create_text(top_x, top_y + 30, text="Lv:" + str(lv), tag="texts")
            canvas.create_text(top_x, top_y - 30, text="Remain:" + str(sasuhari + 1), tag="texts")
        canvas.update()
        before_key == key
    except:
        print("Finish!")
        sys.exit()
before_key = ""
oval_size = 150
game_over = 0
deg = 0
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
hari = 10
haris = []
canvas.create_line(640, 850, 640, 650, tag="taiki_hari", width=10)
root.after(20, byouga())
lv = 0
if_click = 0
def click():
    global if_click
    if_click = 1
button = tkinter.Button(root, text="Push!", command=click)
button.place(x=700, y=700, width=100, height=50)
while True:
    lv += 1
    syote_hari = random.randint(5, (5 + lv))
    sasuhari = 10 + lv - syote_hari
    for i in range(syote_hari):
        haris.append((6.28 / syote_hari) * i)
    while True:
        root.after(20, byouga())
        if if_click == 1:
            if_click = 0
            hari -= 1
            break_ = 0
            for i in range(6):
                canvas.create_line(640, 800 - (600 - oval_size * 2 - 100) / 5 * i, 640, 600 - (600 - oval_size * 2 - 100) / 5 * i, tag="sasu_hari", width=10)
                root.after(20, byouga())
                canvas.delete("sasu_hari")
                for k in range(len(haris)):
                    if deg % 6.28 - 0.03 < ((haris[k]) % 6.28) and deg % 6.28 + 0.03 > ((haris[k]) % 6.28):
                        lv -= 1
                        break_ = 1
                        time.sleep(1)
                        break
                if break_ == 1:
                    break
            if break_ == 1:
                break
            haris.append(deg)
            if sasuhari == 0:
                time.sleep(1)
                break
            for i in range(6):
                root.after(20, byouga())
            sasuhari -= 1
    haris.clear()
        
print("game over")