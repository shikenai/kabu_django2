from django.shortcuts import render
import requests
import os
import pandas as pd


def index(request):
    return render(request, 'index.html')


# 東証から銘柄一覧を取得して、dataフォルダに格納する一連の関数
def save_file(path, filename, data, mode):
    # ファイルを保存するためのディレクトリを作成
    os.makedirs(path, exist_ok=True)

    # ファイルパスを生成
    file_path = os.path.join(path, filename)

    # 指定したフォルダに保存
    with open(file_path, mode) as f:
        f.write(data.content)


def brand_xls2csv():
    read_file = pd.read_excel("/Users/yoshikazukakehashi/PycharmProjects/kabu_django2/data/data_all_brand.xls")
    read_file.to_csv("/Users/yoshikazukakehashi/PycharmProjects/kabu_django2/data/data_all_brand.csv", index=True,
                     header=True)


def get_all_brand():
    req = requests.get("https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls")

    # 保存先ディレクトリのパス
    new_dir = "/Users/yoshikazukakehashi/PycharmProjects/kabu_django2/data"

    # 保存するファイル名
    fname = "data_all_brand.xls"

    # ファイルを保存する
    save_file(new_dir, fname, req, "wb")

    brand_xls2csv()
