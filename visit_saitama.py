import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("CSV_4_2_1_.csv",
                 usecols=["Country","Item1","Year","Overnight Stays"])

#欠損有無確認 １個前の値で埋めた
#print(df.isnull().sum())
df = df.fillna(method = "ffill") 

#t_data["Overnight Stays"]が文字列みたいになっている（グラフのｙ軸がヘンテコ）
# 数値に変換する（リスト内包の出番）
#Python の int() は 「5,670」 のようなカンマを含む文字列を整数に変換できない。
#カンマを削除してから整数に変換
# 数値に変換して新しい列として追加
#まず、df["Overnight Stays"] のすべての値を 文字列 (str) に変換 してから
# .replace() を実行するとエラーを防ぐことがでる
df["stays"] = [int(str(val).replace(",", "")) for val in df["Overnight Stays"]]

country_name = [val for val in df["Country"]]
country_name = list(set(country_name))
country_name = sorted(country_name)
country_name = country_name[3:7]
#print(country_name)

#バーの幅
width = 0.15
# 各国のデータを取得し、棒グラフを作成
for i, val in enumerate(country_name):
    country = df.query(f'Country == "{val}" and Item1 == "Saitama"') 
    plt.bar(country["Year"] + i * width, country["stays"], width, label=val)  

# 凡例とタイトル
plt.legend(loc=2)
plt.title("埼玉県の外国人訪問(宿泊)件数")
plt.xlabel("Year")
plt.ylabel("Overnight Stays")

plt.show()
