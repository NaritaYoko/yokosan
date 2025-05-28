import requests
import json
import tkinter as tk, tkinter.ttk as ttk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("新商品TOP10")
root.minsize(500,600)

category_list={"チョコレート":2103,"スナック":2203,"キャンディ・グミ":2403,
               "アイスクリーム":2503,"チルドデザート":2603,"炭酸ドリンク":4103,
               "茶系ドリンク":4203,"ＲＴＤ":5103,"ビール類":5203,}

#canvas型を作ろう
can1 = tk.Canvas(width=500,height=600)
can1.place(x=0,y=0)
#can2 = tk.Canvas(width=100,height=90)
#can2.place(x=300,y=0)

#写真の指定
img = tk.PhotoImage(file = "try/img/itimatu_5.png")
#img2 = tk.PhotoImage(file = "try/img/food_retoruto_curry_rice.png")


#キャンバスに写真を貼り付ける
can1.create_image(0,0,image = img, anchor = tk.NW)
#can2.create_image(0,0,image = img2, anchor = tk.NW)

def clear():
    """ボックスの文字を消す"""
    box3.delete(0,tk.END)
    box4.delete(0.0,tk.END)

def get_start(event):
    clear()
    category = select.get()  # ユーザーが選んだカテゴリー


    url = f"https://ksp-api.com/api/f/newRanking/{category_list[category]}" #新商品top10
    data = requests.get(url)
    json_data = json.loads(data.text)

# ランキングの1位から10位までを表示
    for rank in json_data: 
        day = rank["nentk"]
        rank_no = rank["rank_no"]
        category = rank["cate_nm"]
        maker = rank['maker_nm']
        item = rank["item_nm"]
        
        output_str = f"  第{rank_no}位\n  メーカー：{maker}\n  商品名：{item}\n" + " " +"-" * 65 +"\n"
        box4.insert(tk.END, output_str)

    box3.insert(tk.END, day)

text1 = tk.Label(text="新商品TOP10",font=("メイリオ", 12, "bold"), background="#f8eb9c")
text1.place(y=10,x=200)

select = ttk.Combobox()
select["values"] = tuple(category_list.keys()) # 辞書のキーを選択肢とする
select.current(0) #デフォルト値の設定。無くてもOK
select.place(y=50,x=50)

btn1 = tk.Button(text="検索",font=("メイリオ", 9, "bold"),background="#f8eb9c")
btn1.bind("<1>", get_start)
btn1.place(y=48,x=220)

"""
text2 = tk.Label(text="カテゴリー",font=("メイリオ", 9, "bold"))
text2.place(y=120,x=50)
box2 = tk.Entry(width=7,font=("メイリオ", 9, "bold"))
box2.place(y=120,x=120)
"""

text3 = tk.Label(text="対象年月",font=("メイリオ", 9, "bold"), background="#f8eb9c")
text3.place(y=80,x=50)
box3 = tk.Entry(width=7,font=("メイリオ", 9, "bold"))
box3.place(y=80,x=120)

#text4 = tk.Label(text="",font=("メイリオ", 9, "bold"), bg='#040414', fg='#ffffff')
#text4.place(y=160,x=50)
box4 = tk.Text(width=50,height=20,font=("メイリオ", 9, "bold"))
box4.place(y=110,x=50)


root.mainloop()