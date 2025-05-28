import requests
from bs4 import BeautifulSoup
import tkinter as tk, tkinter.ttk as ttk

root = tk.Tk()
root.title("今日は何の日？")
root.minsize(500,500)

#canvas型を作ろう
can2 = tk.Canvas(width=500,height=500)
can2.place(x=0,y=0)
#can1 = tk.Canvas(width=100,height=93)
#can1 = tk.Canvas(width=100, height=93, background="#f9f8f2")
#can1.place(x=370,y=10)



#写真の指定
#img = tk.PhotoImage(file = "try/img/calender2.png")
img2 = tk.PhotoImage(file = "try/img/haikei_calender.png")

#キャンバスに写真を貼り付ける
can2.create_image(0,0,image = img2, anchor = tk.NW)
#can1.create_image(0,0,image = img, anchor = tk.NW)


def clear():
    """ボックスの文字を消す"""
    box4.delete(0.0,tk.END)

def get_start(event):
     clear()
     month = box2.get()
     day = box3.get()

     url = f"https://www.php.co.jp/fun/today/{int(month):02}-{int(day):02}.php/" 
     res = requests.get(url)
     kekka = BeautifulSoup(res.text, "html.parser") #kekkaはBeautifulSoup型になった
     
     topics = kekka.find_all("div",class_="topics clearfix")
     output_topics=topics[0].get_text().strip()
     box4.insert(tk.END, output_topics)


text1 = tk.Label(text="今日は何の日？",font=("メイリオ", 12, "bold"), background="#f9f8f2")
text1.place(y=10,x=200)

text2 = tk.Label(text="月",font=("メイリオ", 9, "bold"))
text2.place(y=50,x=170)
box2 = tk.Entry(width=7,font=("メイリオ", 9, "bold"))
box2.place(y=50,x=100)

text3 = tk.Label(text="日",font=("メイリオ", 9, "bold"))
text3.place(y=50,x=270)
box3 = tk.Entry(width=7,font=("メイリオ", 9, "bold"))
box3.place(y=50,x=200)

btn1 = tk.Button(text="検索",font=("メイリオ", 9, "bold"))
btn1.bind("<1>", get_start)
btn1.place(y=50,x=320)

text4 = tk.Label(text="今日は・・・",font=("メイリオ", 10, "bold"), background="#f9f8f2")
text4.place(y=97,x=50)
box4 = tk.Text(width=50,height=20,font=("メイリオ", 9, "bold"))
box4.place(y=120,x=50)


root.mainloop()