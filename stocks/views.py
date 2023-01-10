from django.shortcuts import render
import requests
import os


# Create your views here.

def index(request):
    return render(request, 'index.html')


def save_file(path, filename, data, mode):
    # ファイルを保存するためのディレクトリを作成
    os.makedirs(path, exist_ok=True)

    # ファイルパスを生成
    file_paht = os.path.join(path, filename)

    # 指定したフォルダに保存
    with open(file_paht, mode) as f:
        f.write(data.content)

def get_all_brand():
    req = requests.get("https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls")

    # 保存先ディレクトリのパス
    new_dir = "/Users/yoshikazukakehashi/PycharmProjects/kabu_django2/data"

    # 保存するファイル名
    fname = "data_all_brand.xls"

    # ファイルを保存する
    save_file(new_dir, fname, req, "wb")
