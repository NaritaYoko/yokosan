import json
import requests
import datetime as d
import tkinter as tk, tkinter.ttk as ttk

root = tk.Tk()
root.title("今日の運勢")
root.minsize(500,510)

#canvas型を作ろう
can1 = tk.Canvas(width=500,height=510)
can1.place(x=0,y=0)

# 星座と画像ファイルの対応
sign_to_image = {
    "初期画像":"try/img/bg.png",
    "牡羊座": "try/img/mark01_ohitsuji.png",
    "牡牛座": "try/img/mark02_ouishi.png",
    "双子座": "try/img/mark03-illust5.png",
    "蟹座": "try/img/mark04_kani.png",
    "獅子座": "try/img/mark05_shishi.png",
    "乙女座": "try/img/mark06_otome.png",
    "天秤座": "try/img/mark07_tenbin.png",
    "蠍座": "try/img/mark08_sasori.png",
    "射手座": "try/img/mark09_ite.png",
    "山羊座": "try/img/mark10_yagi.png",
    "水瓶座": "try/img/mark11_mizugame.png",
    "魚座": "try/img/mark12_uo.png",
}

# 初期画像の指定とキャンバスへの配置（タグ "horoscope_image" を追加）
initial_sign = "初期画像" # 初期表示する星座
img = tk.PhotoImage(file = sign_to_image[initial_sign])
image_on_canvas = can1.create_image(0,0,image = img, anchor = tk.NW, tags="horoscope_image")

def clear():
    """ボックスの文字を消す"""
    box2.delete(0,tk.END)
    box3.delete(0.0,tk.END)
    box4.delete(0,tk.END)
    box5.delete(0,tk.END)
    box6.delete(0,tk.END)
    box7.delete(0,tk.END)
    box8.delete(0,tk.END)
    box9.delete(0,tk.END)

def get_start(event):
    clear()
    selected_sign = select.get()  # ユーザーが選んだ星座名

    # 選択された星座に対応する画像ファイルを取得
    if selected_sign in sign_to_image:
        new_image_path = sign_to_image[selected_sign]
        new_img = tk.PhotoImage(file=new_image_path)

        # キャンバス上の画像を更新
        can1.itemconfig(image_on_canvas, image=new_img)
        can1.image = new_img # PhotoImageオブジェクトを保持

    kyou = d.date.today()
    nen = kyou.year
    tsuki = kyou.month
    hi = kyou.day

    url = f"http://api.jugemkey.jp/api/horoscope/free/{nen}/{tsuki:02}/{hi:02}"
    data = requests.get(url)
    json_data = json.loads(data.text)

    h_data = json_data["horoscope"]

    hor = h_data[f"{nen}/{tsuki:02}/{hi:02}"]

    for k in hor:
        if k["sign"] == selected_sign:
            rank = (f"第 {k["rank"]} 位")
            box2.insert(tk.END, rank)
            content = ( k["content"])
            box3.insert(tk.END, content)
            total = (f"{'★ ' * k['total']}")
            box4.insert(tk.END, total)
            money = (f"{'★ ' * k['money']}")
            box5.insert(tk.END, money)
            job = (f" {'★ ' * k['job']}")
            box6.insert(tk.END, job)
            love = (f"{'★ ' * k['love']}")
            box7.insert(tk.END, love)
            item = (k["item"])
            box8.insert(tk.END, item)
            color = (k["color"])
            box9.insert(tk.END, color)


text1 = tk.Label(text="今日の運勢",font=("メイリオ", 12, "bold"), bg='#000000', fg='#ffffff')
text1.place(y=10,x=200)

select_font = ("メイリオ", 10,"bold")  # フォントの種類とサイズ
select = ttk.Combobox(font=select_font,width=10)
#select["values"] = tuple(sign_to_image.keys()) # 辞書のキーを星座の選択肢とする

select["values"] = ("牡羊座", "牡牛座", "双子座", "蟹座","獅子座","乙女座","天秤座","蠍座",
                    "射手座","山羊座","水瓶座","魚座") 

select.current(0) #デフォルト値の設定。無くてもOK
select.place(y=70,x=50)

btn1 = tk.Button(text="占う",font=("メイリオ", 9, "bold"), bg="#e0e474")
btn1.bind("<1>", get_start)
btn1.place(y=70,x=200)

kyou = d.date.today()
text10 = tk.Label(text=f"{kyou}",font=("メイリオ", 9, "bold"),bg='#000000', fg='#ffffff')
text10.place(y=10,x=370)

text2 = tk.Label(text="ランキング",font=("メイリオ", 9, "bold"), bg='#000000', fg='#ffffff')
text2.place(y=120,x=50)
box2 = tk.Entry(width=7,font=("メイリオ", 9, "bold"))
box2.place(y=120,x=120)

text3 = tk.Label(text="総評",font=("メイリオ", 9, "bold"), bg='#01121b', fg='#ffffff')
text3.place(y=160,x=50)
box3 = tk.Text(width=39,height=3,font=("メイリオ", 9, "bold"))
box3.place(y=160,x=120)

text4 = tk.Label(text="総合運",font=("メイリオ", 9, "bold"), bg='#032232', fg='#ffffff')
text4.place(y=240,x=50)
box4 = tk.Entry(width=13)
box4.place(y=240,x=120)

text5 = tk.Label(text="金運",font=("メイリオ", 9, "bold"), bg='#032232', fg='#ffffff')
text5.place(y=240,x=250)
box5 = tk.Entry(width=13)
box5.place(y=240,x=310)

text6 = tk.Label(text="仕事運",font=("メイリオ", 9, "bold"), bg='#042333', fg='#ffffff')
text6.place(y=280,x=50)
box6 = tk.Entry(width=13)
box6.place(y=280,x=120)

text7 = tk.Label(text="恋愛運",font=("メイリオ", 9, "bold"), bg='#042333', fg='#ffffff')
text7.place(y=280,x=250)
box7 = tk.Entry(width=13)
box7.place(y=280,x=310)

text8 = tk.Label(text="ラッキーアイテム",font=("メイリオ", 9, "bold"), bg='#08233c', fg='#ffffff')
text8.place(y=320,x=50)
box8 = tk.Entry(width=18,font=("メイリオ", 9, "bold"))
box8.place(y=320,x=160)

text9 = tk.Label(text="ラッキーカラー",font=("メイリオ", 9, "bold"), bg='#08233c', fg='#ffffff')
text9.place(y=360,x=50)
box9 = tk.Entry(width=18,font=("メイリオ", 9, "bold"))
box9.place(y=360,x=160)

root.mainloop()