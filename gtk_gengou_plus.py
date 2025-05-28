
import tkinter as tk, tkinter.ttk as ttk, random as r 
import datetime as d
import os

root = tk.Tk()
root.title("西暦⇔和暦変換")
root.minsize(530, 300)

#canvas型を作ろう
can1 = tk.Canvas(width=530,height=300)
can1.place(x=0,y=0)

#写真の指定
#img = tk.PhotoImage(file = f"{os.getcwd()}/img/haikei2.png")
img = tk.PhotoImage(file = f"{os.getcwd()}/img/haikei3.png")
# ↑exe化したとき(gengouフォルダからファイルを開いた)
# ↓exe化した時のコマンドプロンプトの書き方(cdでgengouまで移動)
#C:\Users\NECK005\pyworks\try\gengou>pyinstaller gtk_gengou_plus.py --onefile --noconsole --distpath DIR
#img = tk.PhotoImage(file = f"{os.getcwd()}/try/gengou/img/haikei2.png")
#img = tk.PhotoImage(file = f"{os.getcwd()}/try/gengou/img/haikei3.png")
'''
base_path = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(base_path, "img", "haikei2.png")
img = tk.PhotoImage(file=img_path)
'''

#キャンバスに写真を貼り付ける
can1.create_image(0,0,image = img, anchor = tk.NW)

def reset():
     box2.delete(0, tk.END)
     box3.delete(0, tk.END)
     box4.delete(0, tk.END)

def get_change(event):
     reset()
     year = int(box1.get())
     kyou = d.date.today().year

     if year < 1868:
          wareki = ""
          ans = "明治以前です"
     elif year > kyou:
          wareki = ""
          ans = "未来は計算できません"
     elif year < 1912:
          wareki = "明治"
          nen = year-1868+1
     elif year == 1912:
          wareki = "明治"
          nen = year-1868+1
          ans = "1912年7月31日から大正元年です"
     elif year < 1926:
          wareki = "大正"
          nen = year-1912+1
     elif year == 1926:
          wareki = "大正"
          nen = year-1912+1
          ans = "1926年12月26日から昭和元年です"
     elif year < 1989:
          wareki = "昭和"
          nen = year-1926+1
     elif year == 1989:
          wareki = "昭和"
          nen = year-1926+1
          ans = "1989年1月8日から平成元年です"
     elif year < 2019:
          wareki = "平成"
          nen = year-1989+1
     elif year == 2019:
          wareki = "平成"
          nen = year-1989+1
          ans = "2019年5月1日から令和元年です"
     else:
          wareki = "令和"
          nen = year-2019+1

     if year > kyou or year < 1868:
          honbun2 = f"{ans}"
          box4.insert(tk.END, honbun2)
     elif year == 1912 or year == 1926 or year == 1912 or year == 1989 or year == 2019:
          honbun2 = f"{ans}"
          box2.insert(tk.END, wareki)
          box3.insert(tk.END, nen) 
          box4.insert(tk.END, honbun2)
     else:
          box2.insert(tk.END, wareki)
          box3.insert(tk.END, nen) 

text1 = tk.Label(text="西暦 ⇒ 和暦変換",font=("メイリオ", 9, "bold"), bg='#fbf5f1', fg='#482714')
text1.place(x=100,y=40)
#西暦用
text2 = tk.Label(text = "西暦",font=("メイリオ", 9, "bold"), bg='#fbf5f1', fg='#482714')
text2.place(x=50,y=80)
box1 = tk.Entry(width=10)
box1.place(x=90,y=80)
text3 = tk.Label(text="年",font=("メイリオ", 9, "bold"), bg='#fbf5f1', fg='#482714')
text3.place(x=160,y=80)
#和暦用
text4 = tk.Label(text="和暦",font=("メイリオ", 9, "bold"), bg='#fbf5f1', fg='#482714')
text4.place(x=50,y=180)
box2 = tk.Entry(width=8)
box2.place(x=90,y=180)
box3 = tk.Entry(width=10)
box3.place(x=150,y=180)
text5 = tk.Label(text="年",font=("メイリオ", 9, "bold"), bg='#fbf5f1', fg='#482714')
text5.place(x=220,y=180)
#コメント用
box4 = tk.Entry(width=30)
box4.place(x=50,y=230)

btn1 = tk.Button(text="変換",font=("メイリオ", 9, "bold"), bg='#b8a38b', fg='#482714')
btn1.bind("<1>", get_change)
btn1.place(x=130,y=125)


#ここから和暦⇒西暦
def reset2():
     box14.delete(0, tk.END)
     box15.delete(0, tk.END)

def get_change2(event):
     reset2()
     selected_wareki = select.get()
     year = int(box12.get())
     kyou = d.date.today().year
     reiwa_year = kyou - 2018

     ans = "" # エラーメッセージを格納する変数
     nen = "" # 変換された西暦を格納する変数

     if selected_wareki == "明治":
        if year > 45:
            ans = "明治は45年までしかありません"
        else:
            nen = 1868 + year - 1
     elif selected_wareki == "大正":
        if year > 15:
            ans = "大正は15年までしかありません"
        else:
            nen = 1912 + year - 1
     elif selected_wareki == "昭和":
        if year > 64:
            ans = "昭和は64年までしかありません"
        else:
            nen = 1926 + year - 1
     elif selected_wareki == "平成":
        if year > 31:
            ans = "平成は31年までしかありません"
        else:
            nen = 1989 + year - 1
     elif selected_wareki == "令和": # ここは`else`ではなく`elif`で明示的に"令和"をチェック
        if year > reiwa_year:
            ans = "未来はわかりません"
        else:
            nen = 2019 + year - 1

    # 結果の表示
     if ans: # ansに値が入っている場合はエラーメッセージを表示
        box15.insert(tk.END, ans)
     elif nen: # nenに値が入っている場合は西暦を表示
        box14.insert(tk.END, nen)
     else: # 想定外のケース（通常はここには来ないはず）
        box15.insert(tk.END, "エラーが発生しました")


text11 = tk.Label(text="和暦 ⇒ 西暦変換",font=("メイリオ", 9, "bold"), bg='#fbf5f1', fg='#482714')
text11.place(x=350,y=40)

#和暦用
text12 = tk.Label(text="和暦",font=("メイリオ", 9, "bold"), bg='#fbf5f1', fg='#482714')
text12.place(x=300,y=80)
select = ttk.Combobox(width=5)
select["values"] = ("明治","大正","昭和","平成","令和")
select.current(0) #デフォルト値の設定。無くてもOK
select.place(x=340,y=80)
box12 = tk.Entry(width=10)
box12.place(x=400,y=80)
text13 = tk.Label(text="年",font=("メイリオ", 9, "bold"), bg='#fbf5f1', fg='#482714')
text13.place(x=470,y=80)

#西暦用
text14 = tk.Label(text = "西暦",font=("メイリオ", 9, "bold"), bg='#fbf5f1', fg='#482714')
text14.place(x=300,y=180)
box14 = tk.Entry(width=10)
box14.place(x=340,y=180)
text15 = tk.Label(text="年",font=("メイリオ", 9, "bold"), bg='#fbf5f1', fg='#482714')
text15.place(x=410,y=180)

#コメント用
box15 = tk.Entry(width=30)
box15.place(x=300,y=230)

btn11 = tk.Button(text="変換",font=("メイリオ", 9, "bold"), bg='#b8a38b', fg='#482714')
btn11.bind("<1>", get_change2)
btn11.place(x=380,y=125)

root.mainloop()


