import json
import os
import urllib3
import sys
import time
import re
import subprocess
import queue
import threading
import winsound as ws
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import requests
from requests_oauthlib import OAuth1Session
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

FILTER_URL = 'https://stream.twitter.com/1.1/statuses/filter.json'

token = {}
new_token = {"CK": "", "CS": "", "AT": "", "AS": ""}
token_list = os.path.join(os.path.dirname(sys.argv[0]), "token_list.json")
token_check = os.path.isfile(token_list)

sub_win = None
sub_win2 = None
help_win = None

enemy_n = os.path.join(os.path.dirname(sys.argv[0]), "enemy_name.ini")
enemy_n_check = os.path.isfile(enemy_n)
Enemy = "0\n名前"

#jsonファイルの有無(有れば何もしない、無ければ新規作成)
def token_list_check():
    if None or not token_check:
        with open(token_list, "w") as fn:
            json.dump(new_token, fn, indent=4)
#敵ネームファイルの有無
def enemy_name_check():
    if None or not enemy_n_check:
        with open(enemy_n, mode="w") as f:
            f.write(Enemy)

def maguna():
    global sub_win, Enemy
    if sub_win is None or not sub_win.winfo_exists(): #ウィンドウを無ければ新規作成
        sub_win = tk.Toplevel()
        sub_win.title("マグナ")
        frame1 = ttk.Frame(sub_win,padding=10)
        frame1.grid()
        #敵情報を入れる変数の定義
        enemy_s = StringVar()
        #OKボタン用コマンド
        def enemy_set():
            Enemy = enemy_s.get()
            with open(enemy_n, mode="w") as f:
                f.write(Enemy)
            sub_win.destroy()            
        #キャンセルボタン用コマンド
        def sub_close():
            sub_win.destroy()
        #ここから敵情報のラジオボタン
        tiamat50 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv50 ティアマト・マグナ',
            value=("50\nティアマト・マグナ"),
            variable=enemy_s)
        tiamat50.grid(row=0, sticky=W)

        tiamat60 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv60 ティアマト・マグナ',
            value=("60\nティアマト・マグナ"),
            variable=enemy_s)
        tiamat60.grid(row=1, sticky=W)

        colossus70 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv70 コロッサス・マグナ',
            value=("70\nコロッサス・マグナ"),
            variable=enemy_s)
        colossus70.grid(row=2, sticky=W)

        colossus80 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv80 コロッサス・マグナ',
            value=("80\nコロッサス・マグナ"),
            variable=enemy_s)
        colossus80.grid(row=3, sticky=W)

        leviathan60 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv60 リヴァイアサン・マグナ',
            value=("60\nリヴァイアサン・マグナ"),
            variable=enemy_s)
        leviathan60.grid(row=4, sticky=W)

        leviathan70 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv70 リヴァイアサン・マグナ',
            value=("70\nリヴァイアサン・マグナ"),
            variable=enemy_s)
        leviathan70.grid(row=5, sticky=W)

        yggdrasil60 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv60 ユグドラシル・マグナ',
            value=("60\nユグドラシル・マグナ"),
            variable=enemy_s)
        yggdrasil60.grid(row=6, sticky=W)

        yggdrasil70 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv70 ユグドラシル・マグナ',
            value=("70\nユグドラシル・マグナ"),
            variable=enemy_s)
        yggdrasil70.grid(row=7, sticky=W)

        luminiera75 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv75 シュヴァリエ・マグナ',
            value=("75\nシュヴァリエ・マグナ"),
            variable=enemy_s)
        luminiera75.grid(row=8, sticky=W)

        luminiera85 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv85 シュヴァリエ・マグナ',
            value=("85\nシュヴァリエ・マグナ"),
            variable=enemy_s)
        luminiera85.grid(row=9, sticky=W)

        celeste75 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv75 セレスト・マグナ',
            value=("75\nセレスト・マグナ"),
            variable=enemy_s)
        celeste75.grid(row=10, sticky=W)

        celeste85 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv85 セレスト・マグナ',
            value=("85\nセレスト・マグナ"),
            variable=enemy_s)
        celeste85.grid(row=11, sticky=W)

        tiamat100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 ティアマト・マグナ＝エア(HL)',
            value=("100\nティアマト・マグナ＝エア"),
            variable=enemy_s)
        tiamat100.grid(row=12, sticky=W)

        colossus100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 コロッサス・マグナ(HL)',
            value=("100\nコロッサス・マグナ"),
            variable=enemy_s)
        colossus100.grid(row=13, sticky=W)

        leviathan100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 リヴァイアサン・マグナ(HL)',
            value=("100\nリヴァイアサン・マグナ"),
            variable=enemy_s)
        leviathan100.grid(row=14, sticky=W)

        yggdrasil100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 ユグドラシル・マグナ(HL)',
            value=("100\nユグドラシル・マグナ"),
            variable=enemy_s)
        yggdrasil100.grid(row=15, sticky=W)

        luminiera100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 シュヴァリエ・マグナ(HL)',
            value=("100\nシュヴァリエ・マグナ"),
            variable=enemy_s)
        luminiera100.grid(row=16, sticky=W)

        celeste100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 セレスト・マグナ(HL)',
            value=("100\nセレスト・マグナ"),
            variable=enemy_s)
        celeste100.grid(row=17, sticky=W)

        #ボタンUIの位置及びコマンド設定
        button1 = ttk.Button(frame1, text='OK', padding=5, command=enemy_set)
        button1.grid(row=18, sticky=E)

        button2 = ttk.Button(frame1, text='cancel', padding=5, command=sub_close)
        button2.grid(row=18, column=2)

def old_ishi():
    global sub_win, Enemy
    if sub_win is None or not sub_win.winfo_exists(): #ウィンドウを無ければ新規作成
        sub_win = tk.Toplevel()
        sub_win.title("旧石")
        frame1 = ttk.Frame(sub_win,padding=10)
        frame1.grid()
        #敵情報を入れる変数の定義
        enemy_s = StringVar()
        #OKボタン用コマンド
        def enemy_set():
            Enemy = enemy_s.get()
            with open(enemy_n, mode="w") as f:
                f.write(Enemy)
            sub_win.destroy()            
        #キャンセルボタン用コマンド
        def sub_close():
            sub_win.destroy()
        #ここから敵情報のラジオボタン
        nezha100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 ナタク',
            value=("100\nナタク"),
            variable=enemy_s)
        nezha100.grid(row=0, sticky=W)

        twin100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 フラム＝グラス',
            value=("100\nフラム＝グラス"),
            variable=enemy_s)
        twin100.grid(row=1, sticky=W)

        macula100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 マキュラ・マリウス',
            value=("100\nマキュラ・マリウス"),
            variable=enemy_s)
        macula100.grid(row=2, sticky=W)

        medusa100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 メドゥーサ',
            value=("100\nメドゥーサ"),
            variable=enemy_s)
        medusa100.grid(row=3, sticky=W)

        apollo100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 アポロン',
            value=("100\nアポロン"),
            variable=enemy_s)
        apollo100.grid(row=4, sticky=W)

        olivia100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 Dエンジェル・オリヴィエ',
            value=("100\nDエンジェル・オリヴィエ"),
            variable=enemy_s)
        olivia100.grid(row=5, sticky=W)

        nezha120 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 ナタク(HL)',
            value=("120\nナタク"),
            variable=enemy_s)
        nezha120.grid(row=6, sticky=W)

        twin120 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 フラム＝グラス(HL)',
            value=("120\nフラム＝グラス"),
            variable=enemy_s)
        twin120.grid(row=7, sticky=W)

        macula120 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 マキュラ・マリウス(HL)',
            value=("120\nマキュラ・マリウス"),
            variable=enemy_s)
        macula120.grid(row=8, sticky=W)

        medusa120 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 メドゥーサ(HL)',
            value=("120\nメドゥーサ"),
            variable=enemy_s)
        medusa120.grid(row=9, sticky=W)

        apollo120 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 アポロン(HL)',
            value=("120\nアポロン"),
            variable=enemy_s)
        apollo120.grid(row=10, sticky=W)

        olivia120 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 Dエンジェル・オリヴィエ(HL)',
            value=("120\nDエンジェル・オリヴィエ"),
            variable=enemy_s)
        olivia120.grid(row=11, sticky=W)

        #ボタンUIの位置及びコマンド設定
        button1 = ttk.Button(frame1, text='OK', padding=5, command=enemy_set)
        button1.grid(row=12, sticky=E)

        button2 = ttk.Button(frame1, text='cancel', padding=5, command=sub_close)
        button2.grid(row=12, column=2)

def new_ishi():
    global sub_win, Enemy
    if sub_win is None or not sub_win.winfo_exists(): #ウィンドウを無ければ新規作成
        sub_win = tk.Toplevel()
        sub_win.title("新石")
        frame1 = ttk.Frame(sub_win,padding=10)
        frame1.grid()
        #敵情報を入れる変数の定義
        enemy_s = StringVar()
        #OKボタン用コマンド
        def enemy_set():
            Enemy = enemy_s.get()
            with open(enemy_n, mode="w") as f:
                f.write(Enemy)
            sub_win.destroy()            
        #キャンセルボタン用コマンド
        def sub_close():
            sub_win.destroy()
        #ここから敵情報のラジオボタン
        garuda = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 ガルーダ',
            value=("100\nガルーダ"),
            variable=enemy_s)
        garuda.grid(row=0, sticky=W)

        athena = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 アテナ',
            value=("100\nアテナ"),
            variable=enemy_s)
        athena.grid(row=1, sticky=W)

        grani = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 グラニ',
            value=("100\nグラニ"),
            variable=enemy_s)
        grani.grid(row=2, sticky=W)

        baal = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 バアル',
            value=("100\nバアル"),
            variable=enemy_s)
        baal.grid(row=3, sticky=W)

        odin = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 オーディン',
            value=("100\nオーディン"),
            variable=enemy_s)
        odin.grid(row=4, sticky=W)

        lich = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 リッチ',
            value=("100\nリッチ"),
            variable=enemy_s)
        lich.grid(row=5, sticky=W)

        #ボタンUIの位置及びコマンド設定
        button1 = ttk.Button(frame1, text='OK', padding=5, command=enemy_set)
        button1.grid(row=6, sticky=E)

        button2 = ttk.Button(frame1, text='cancel', padding=5, command=sub_close)
        button2.grid(row=6, column=2)

def caban():
    global sub_win, Enemy
    if sub_win is None or not sub_win.winfo_exists(): #ウィンドウを無ければ新規作成
        sub_win = tk.Toplevel()
        sub_win.title("高級鞄")
        frame1 = ttk.Frame(sub_win,padding=10)
        frame1.grid()
        #敵情報を入れる変数の定義
        enemy_s = StringVar()
        #OKボタン用コマンド
        def enemy_set():
            Enemy = enemy_s.get()
            with open(enemy_n, mode="w") as f:
                f.write(Enemy)
            sub_win.destroy()            
        #キャンセルボタン用コマンド
        def sub_close():
            sub_win.destroy()
        #ここから敵情報のラジオボタン
        morrigna = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 バイヴカハ',
            value=("120\nバイヴカハ"),
            variable=enemy_s)
        morrigna.grid(row=0, sticky=W)

        prometheus = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 プロメテウス',
            value=("120\nプロメテウス"),
            variable=enemy_s)
        prometheus.grid(row=1, sticky=W)

        caong = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 カー・オン',
            value=("120\nカー・オン"),
            variable=enemy_s)
        caong.grid(row=2, sticky=W)

        gilgamesh = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 ギルガメッシュ',
            value=("120\nギルガメッシュ"),
            variable=enemy_s)
        gilgamesh.grid(row=3, sticky=W)

        hector = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 ヘクトル',
            value=("120\nヘクトル"),
            variable=enemy_s)
        hector.grid(row=4, sticky=W)

        anubis = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 アヌビス',
            value=("120\nアヌビス"),
            variable=enemy_s)
        anubis.grid(row=5, sticky=W)

        #ボタンUIの位置及びコマンド設定
        button1 = ttk.Button(frame1, text='OK', padding=5, command=enemy_set)
        button1.grid(row=6, sticky=E)

        button2 = ttk.Button(frame1, text='cancel', padding=5, command=sub_close)
        button2.grid(row=6, column=2)

def tenshi():
    global sub_win, Enemy
    if sub_win is None or not sub_win.winfo_exists(): #ウィンドウを無ければ新規作成
        sub_win = tk.Toplevel()
        sub_win.title("四大天司")
        frame1 = ttk.Frame(sub_win,padding=10)
        frame1.grid()
        #敵情報を入れる変数の定義
        enemy_s = StringVar()
        #OKボタン用コマンド
        def enemy_set():
            Enemy = enemy_s.get()
            with open(enemy_n, mode="w") as f:
                f.write(Enemy)
            sub_win.destroy()            
        #キャンセルボタン用コマンド
        def sub_close():
            sub_win.destroy()
        #ここから敵情報のラジオボタン
        raphael = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 ラファエル',
            value=("100\nラファエル"),
            variable=enemy_s)
        raphael.grid(row=0, sticky=W)

        michael = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 ミカエル',
            value=("100\nミカエル"),
            variable=enemy_s)
        michael.grid(row=1, sticky=W)

        gabriel = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 ガブリエル',
            value=("100\nガブリエル"),
            variable=enemy_s)
        gabriel.grid(row=2, sticky=W)

        uriel = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 ウリエル',
            value=("100\nウリエル"),
            variable=enemy_s)
        uriel.grid(row=3, sticky=W)

        primarchs = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv??? 四大天司ＨＬ',
            value=("???\n四大天司ＨＬ"),
            variable=enemy_s)
        primarchs.grid(row=4, sticky=W)

        #ボタンUIの位置及びコマンド設定
        button1 = ttk.Button(frame1, text='OK', padding=5, command=enemy_set)
        button1.grid(row=5, sticky=E)

        button2 = ttk.Button(frame1, text='cancel', padding=5, command=sub_close)
        button2.grid(row=5, column=2)

def maguna2():
    global sub_win, Enemy
    if sub_win is None or not sub_win.winfo_exists(): #ウィンドウを無ければ新規作成
        sub_win = tk.Toplevel()
        sub_win.title("マグナ2")
        frame1 = ttk.Frame(sub_win,padding=10)
        frame1.grid()
        #敵情報を入れる変数の定義
        enemy_s = StringVar()
        #OKボタン用コマンド
        def enemy_set():
            Enemy = enemy_s.get()
            with open(enemy_n, mode="w") as f:
                f.write(Enemy)
            sub_win.destroy()            
        #キャンセルボタン用コマンド
        def sub_close():
            sub_win.destroy()
        #ここから敵情報のラジオボタン
        grimnir = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 グリームニル',
            value=("120\nグリームニル"),
            variable=enemy_s)
        grimnir.grid(row=0, sticky=W)

        shiva = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 シヴァ',
            value=("120\nシヴァ"),
            variable=enemy_s)
        shiva.grid(row=1, sticky=W)

        europa = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 エウロペ',
            value=("120\nエウロペ"),
            variable=enemy_s)
        europa.grid(row=2, sticky=W)

        goburo = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 ゴッドガード・ブローディア',
            value=("120\nゴッドガード・ブローディア"),
            variable=enemy_s)
        goburo.grid(row=3, sticky=W)

        metatron = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 メタトロン',
            value=("120\nメタトロン"),
            variable=enemy_s)
        metatron.grid(row=4, sticky=W)

        avatar = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv120 アバター',
            value=("120\nアバター"),
            variable=enemy_s)
        avatar.grid(row=5, sticky=W)

        #ボタンUIの位置及びコマンド設定
        button1 = ttk.Button(frame1, text='OK', padding=5, command=enemy_set)
        button1.grid(row=6, sticky=E)

        button2 = ttk.Button(frame1, text='cancel', padding=5, command=sub_close)
        button2.grid(row=6, column=2)

def etc():
    global sub_win, Enemy
    if sub_win is None or not sub_win.winfo_exists(): #ウィンドウを無ければ新規作成
        sub_win = tk.Toplevel()
        sub_win.title("マグナ2")
        frame1 = ttk.Frame(sub_win,padding=10)
        frame1.grid()
        #敵情報を入れる変数の定義
        enemy_s = StringVar()
        #OKボタン用コマンド
        def enemy_set():
            Enemy = enemy_s.get()
            with open(enemy_n, mode="w") as f:
                f.write(Enemy)
            sub_win.destroy()            
        #キャンセルボタン用コマンド
        def sub_close():
            sub_win.destroy()
        #ここから敵情報のラジオボタン
        proto100 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 プロトバハムート',
            value=("100\nプロトバハムート"),
            variable=enemy_s)
        proto100.grid(row=0, sticky=W)

        proto150 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv150 プロトバハムート(HL)',
            value=("150\nプロトバハムート"),
            variable=enemy_s)
        proto150.grid(row=1, sticky=W)

        ultimate150 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv150 アルティメットバハムート',
            value=("150\nアルティメットバハムート"),
            variable=enemy_s)
        ultimate150.grid(row=2, sticky=W)

        grand = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 ジ・オーダー・グランデ',
            value=("100\nジ・オーダー・グランデ"),
            variable=enemy_s)
        grand.grid(row=3, sticky=W)

        rose = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv110 ローズクイーン',
            value=("110\nローズクイーン"),
            variable=enemy_s)
        rose.grid(row=4, sticky=W)

        huanglong = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 黄龍',
            value=("100\n黄龍"),
            variable=enemy_s)
        huanglong.grid(row=5, sticky=W)

        qilin = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv100 黒麒麟',
            value=("100\n黒麒麟"),
            variable=enemy_s)
        qilin.grid(row=6, sticky=W)

        impossible = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv??? 黄龍・黒麒麟HL',
            value=("???\n黄龍・黒麒麟HL"),
            variable=enemy_s)
        impossible.grid(row=7, sticky=W)

        malice = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv150 ティアマト・マリス',
            value=("150\nティアマト・マリス"),
            variable=enemy_s)
        malice.grid(row=8, sticky=W)

        akasha = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv200 アーカーシャ',
            value=("200\nアーカーシャ"),
            variable=enemy_s)
        akasha.grid(row=9, sticky=W)

        lucilius = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv150 ルシファー',
            value=("150\nルシファー"),
            variable=enemy_s)
        lucilius.grid(row=10, sticky=W)

        ultimate200 = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv200 アルティメットバハムート(HL)',
            value=("200\nアルティメットバハムート"),
            variable=enemy_s)
        ultimate200.grid(row=11, sticky=W)

        #ボタンUIの位置及びコマンド設定
        button1 = ttk.Button(frame1, text='OK', padding=5, command=enemy_set)
        button1.grid(row=12, sticky=E)

        button2 = ttk.Button(frame1, text='cancel', padding=5, command=sub_close)
        button2.grid(row=12, column=2)

def sisyo():
    global sub_win, Enemy
    if sub_win is None or not sub_win.winfo_exists(): #ウィンドウを無ければ新規作成
        sub_win = tk.Toplevel()
        sub_win.title("四象降臨")
        frame1 = ttk.Frame(sub_win,padding=10)
        frame1.grid()
        #敵情報を入れる変数の定義
        enemy_s = StringVar()
        #OKボタン用コマンド
        def enemy_set():
            Enemy = enemy_s.get()
            with open(enemy_n, mode="w") as f:
                f.write(Enemy)
            sub_win.destroy()            
        #キャンセルボタン用コマンド
        def sub_close():
            sub_win.destroy()
        #ここから敵情報のラジオボタン
        zephyrus = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv90  ゼピュロス',
            value=("90\nゼピュロス"),
            variable=enemy_s)
        zephyrus.grid(row=0, sticky=W)

        agni = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv90 アグニス',
            value=("90\nアグニス"),
            variable=enemy_s)
        agni.grid(row=1, sticky=W)

        neptune = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv90 ネプチューン',
            value=("90\nネプチューン"),
            variable=enemy_s)
        neptune.grid(row=2, sticky=W)

        titan = ttk.Radiobutton(
            frame1,
            padding=5,
            text='Lv90 ティターン',
            value=("90\nティターン"),
            variable=enemy_s)
        titan.grid(row=3, sticky=W)

        #ボタンUIの位置及びコマンド設定
        button1 = ttk.Button(frame1, text='OK', padding=5, command=enemy_set)
        button1.grid(row=4, sticky=E)

        button2 = ttk.Button(frame1, text='cancel', padding=5, command=sub_close)
        button2.grid(row=4, column=2)

def syudou():
    global sub_win, Enemy
    if sub_win is None or not sub_win.winfo_exists(): #ウィンドウを無ければ新規作成
        sub_win = tk.Toplevel()
        sub_win.title("手動入力")
        frame1 = ttk.Frame(sub_win,padding=10)
        frame1.grid()
        #敵情報を入れる変数の定義
        enemy_s = StringVar()
        #OKボタン用コマンド
        def enemy_set():
            Enemy = Lv.get() + "\n" + name.get()
            with open(enemy_n, mode="w") as f:
                f.write(Enemy)
            sub_win.destroy()            
        #キャンセルボタン用コマンド
        def sub_close():
            sub_win.destroy()

        label1 = ttk.Label(frame1, text='Lv', padding=(5,2))
        label1.grid(row=0,column=0,sticky=E)
    
        label2 = ttk.Label(frame1, text='正式名称', padding=(5,2))
        label2.grid(row=1,column=0,sticky=E)
        
        Lv = StringVar()
        Lv_set = ttk.Entry(
            frame1,
            textvariable=Lv,
            width=20 )
        Lv_set.grid(row=0,column=1, sticky=W)

        name = StringVar()
        name_set = ttk.Entry(
            frame1,
            textvariable=name,
            width=50 )
        name_set.grid(row=1,column=1, sticky=W)
        
        #ボタンUIの位置及びコマンド設定
        button1 = ttk.Button(frame1, text='OK', padding=5, command=enemy_set)
        button1.grid(row=3, column=1, sticky=E)

        button2 = ttk.Button(frame1, text='cancel', padding=5, command=sub_close)
        button2.grid(row=3, column=2, sticky=W)

#使い方説明
def help():
    global help_win, Enemy
    if help_win is None or not help_win.winfo_exists(): #ウィンドウを無ければ新規作成
        help_win = tk.Toplevel()
        help_win.title("Help")
        frame1 = ttk.Frame(help_win,padding=10)
        frame1.grid()
        #OKボタン用コマンド
        def help_close():
            help_win.destroy()

        label1 = ttk.Label(frame1, text='1. MenuボタンからTwitter APIキー情報の入力をしOKボタンを押す(次回以降入力の必要はありません)', padding=(5,2))
        label1.grid(row=0,column=0,sticky=W)
        label2 = ttk.Label(frame1, text='2. 救援一覧から入りたい救援を選択し(1種類のみ)そのサブウィンドウ下部のOKボタンを押す', padding=(5,2))
        label2.grid(row=1,column=0,sticky=W)
        label3 = ttk.Label(frame1, text='3. メインウィンドウ上部のStartボタンで救援tweetのリアルタイム更新を開始', padding=(5,2))
        label3.grid(row=3,column=0,sticky=W)
        label4 = ttk.Label(frame1, text='4. 更新されメインウィンドウのテキスト欄に表示された瞬間には1番上の救援IDが\nクリップボードにコピーされているのでゲーム内のIDを入力する画面にペーストする', padding=(5,2))
        label4.grid(row=4,column=0,sticky=W)
        label5 = ttk.Label(frame1, text='5. 別の救援に切り替える場合や停止したい場合はStartボタン横のStopボタンを押す\n(停止まで時間がかかる場合があります※)', padding=(5,2))
        label5.grid(row=5,column=0,sticky=W)
        label6 = ttk.Label(frame1, text='6. Startボタンを押した後の終了に関しましては\nMenu内Exit及びウィンドウ右上の×で消していただいてかまいません(メイン終了時に実行中スレッドを消すようになっています)', padding=(5,2))
        label6.grid(row=6,column=0,sticky=W)
        label7 = ttk.Label(frame1, text='7. 通知音に関してはチェックボックスにチェックが入っているとWindows標準サウンドが救援tweet表示毎に鳴るようになります。\nこの機能に関してもON/OFFする際にはお手数ですが一度Stopを押し更新を止めた状態で切り替えてください。', padding=(5,2))
        label7.grid(row=7,column=0,sticky=W)
        label8 = ttk.Label(frame1, text='※. 救援ツイートの流れてくる頻度の低いものに関しては終了までの時間が極端に長かったり\nアプリがフリーズしてしまう可能性も有りますがその際はお手数ですがアプリの再起動をしていただけると助かります', padding=(5,2))
        label8.grid(row=8,column=0,sticky=W)
        label9 = ttk.Label(frame1, text='※2. 救援tweetの流れてくる頻度が低かったりした場合の再取得が3回発生するとフリーズ及びアクセス過多による420エラー回避のため自動ストップになります', padding=(5,2))
        label9.grid(row=9,column=0,sticky=W)
        
        #ボタンUIの位置及びコマンド設定
        button1 = ttk.Button(frame1, text='OK', padding=5, command=help_close)
        button1.grid(row=10, column=1, sticky=E)
def ver_help():
    global help_win, Enemy
    if help_win is None or not help_win.winfo_exists(): #ウィンドウを無ければ新規作成
        help_win = tk.Toplevel()
        help_win.title("etc")
        frame1 = ttk.Frame(help_win,padding=10)
        frame1.grid()
        #OKボタン用コマンド
        def help_close():
            help_win.destroy()

        label1 = ttk.Label(frame1, text='GBF救援ID検索補助ツール Ver 1.0', padding=(5,2))
        label1.grid(row=0,column=0,sticky=W)
        label2 = ttk.Label(frame1, text='バグ等のお問い合わせ先は\nTwitter ID=@Enable_ERO へお願いします。', padding=(5,2))
        label2.grid(row=1,column=0,sticky=W)
        
        #ボタンUIの位置及びコマンド設定
        button1 = ttk.Button(frame1, text='OK', padding=5, command=help_close)
        button1.grid(row=10, column=1, sticky=E)

def OAuths():
    global sub_win2, token
    if sub_win2 is None or not sub_win2.winfo_exists(): #ウィンドウを無ければ新規作成
        sub_win2 = tk.Toplevel()
        sub_win2.title('APIキー情報設定')
        sub_win2.resizable(False, False)
        frame1 = ttk.Frame(sub_win2, padding=10)
        frame1.grid()
        #jsonファイルを開きAPIキー取得
        with open(token_list) as f:
            jsn = json.load(f)

        label1 = ttk.Label(frame1, text='consumer key', padding=(5,2))
        label1.grid(row=0,column=0,sticky=E)
    
        label2 = ttk.Label(frame1, text='consumer key secret', padding=(5,2))
        label2.grid(row=1,column=0,sticky=E)
    
        label3 = ttk.Label(frame1, text='access token', padding=(5,2))
        label3.grid(row=2,column=0,sticky=E)

        label4 = ttk.Label(frame1, text='access token secret', padding=(5,2))
        label4.grid(row=3,column=0,sticky=E)

        consumer_key = StringVar()
        consumer_key = ttk.Entry(
            frame1,
            textvariable=consumer_key,
            width=60 )
        consumer_key.grid(row=0,column=1)
        consumer_key.insert(tkinter.END, jsn["CK"])

        consumer_key_secret = StringVar()
        consumer_key_secret = ttk.Entry(
            frame1,
            textvariable=consumer_key_secret,
            width=60 )
        consumer_key_secret.grid(row=1,column=1)
        consumer_key_secret.insert(tkinter.END, jsn["CS"])

        access_token = StringVar()
        access_token = ttk.Entry(
            frame1,
            textvariable=access_token,
            width=60 )
        access_token.grid(row=2,column=1)
        access_token.insert(tkinter.END, jsn["AT"])

        access_token_secret = StringVar()
        access_token_secret = ttk.Entry(
            frame1,
            textvariable=access_token_secret,
            width=60 )
        access_token_secret.grid(row=3,column=1)
        access_token_secret.insert(tkinter.END, jsn["AS"])

        #入力した内容を反映して保存するコマンド
        def ok_info():
            token["CK"] = consumer_key.get()
            token["CS"] = consumer_key_secret.get()
            token["AT"] = access_token.get()
            token["AS"] = access_token_secret.get()
            with open(token_list, "w") as f:
                json.dump(token, f, indent=4)
            messagebox.showinfo("OK", "保存しました")
            sub_win2.destroy()
        #キャンセルボタン用コマンド
        def sub2_close():
            sub_win2.destroy()

        frame2 = ttk.Frame(frame1, padding=(0,5))
        frame2.grid(row=4,column=1,sticky=W)

        button1 = ttk.Button(frame2, text="OK", command=ok_info)
        button1.pack(side=LEFT)
        
        button2 = ttk.Button(frame2, text="Cancel",command=sub2_close)
        button2.pack(side=LEFT)

# 文字列から参戦IDを抽出
def parse(string):
    pattern = r'[0-9A-F]{8}\s:参戦ID'
    matchOB = re.findall(pattern, string)   # 一致する文字列を全て取得
    if matchOB:
        return matchOB[-1][0:8]     # 一致する文字列のうち最後のものをreturnすることによってダミーのIDを回避
    else:
        return None
# stringをクリップボードにコピー
def set_clipboard(string, os_name):
    if os_name == 'win32':
        process = subprocess.Popen('clip', stdin = subprocess.PIPE, shell=True)
    process.communicate(string.encode("utf-8")) # str型をbyte型に変換
#メインフレーム終了コマンド
def Exit():
    root.quit()

if __name__ == "__main__":
    
    root = Tk()
    #Twitter APIキーファイル確認
    token_list_check()
    #敵ネームファイル確認
    enemy_name_check()
    
    os_name = sys.platform

    menubar = Menu(root)

    # File Menu
    filemenu = Menu(menubar, tearoff=0)
    enemy_type = Menu(menubar, tearoff=0)

    filemenu.add_cascade(label="救援一覧", menu=enemy_type)
    filemenu.add_command(label="APIキー情報設定", command=OAuths)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=Exit)
    # Help
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="使い方", command=help)
    helpmenu.add_command(label="バージョン情報etc", command=ver_help)
    # Add
    menubar.add_cascade(label="Menu", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)

    for List in ("マグナ+HL", "旧石", "新石", "高級鞄", "四大天使", "マグナ2", "その他", "四象降臨", "手動入力"):
        if ("マグナ+HL") in List:
            enemy_type.add_command(label="マグナ", command=maguna)
        if ("旧石") in List:
            enemy_type.add_command(label="旧石", command=old_ishi)
        if ("新石") in List:
            enemy_type.add_command(label="新石", command=new_ishi)
        if ("高級鞄") in List:
            enemy_type.add_command(label="高級鞄", command=caban)
        if ("四大天使") in List:
            enemy_type.add_command(label="四大天使", command=tenshi)
        if ("マグナ2") in List:
            enemy_type.add_command(label="マグナ2", command=maguna2)
        if ("その他") in List:
            enemy_type.add_command(label="その他", command=etc)
        if ("四象降臨") in List:
            enemy_type.add_command(label="四象降臨", command=sisyo)
        if ("手動入力") in List:
            enemy_type.add_command(label="手動入力", command=syudou)

    root.config(menu=menubar)

    root.title("GBF救援ID検索補助ツール")
    root.minsize(500, 200)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.grid()
    
    frame1 = ttk.Frame(root)
    frame1.rowconfigure(0, weight=1)
    frame1.columnconfigure(0, weight=1)
    frame1.grid(sticky=W)

    #通知音チェックボックスの表示
    sound_chk = BooleanVar()
    sound_chk_box = tkinter.Checkbutton(variable=sound_chk, text=u"通知音ON/OFF")
    sound_chk_box.grid(row=0, column=0, sticky=E)
    
    #テキストウィジェットの表示
    text_widget = tk.Text(root)
    text_widget.grid(column=0, row=2, sticky=(tk.N, tk.S, tk.E, tk.W))

    stop_flag= False
    thread= None
    error = 0

    def start():
        global stop_flag, thread, error
        while not stop_flag:
            try:
                #敵情報読み込み
                with open(enemy_n) as fe:
                    Enemy = [s.strip() for s in fe.readlines()]
                #APIキー読み込み+定義
                with open(token_list) as f:
                    jsn = json.load(f)
                CK = jsn["CK"]
                CS = jsn["CS"]
                AT = jsn["AT"]
                AS = jsn["AS"]
                #OAuth
                oauth_session = OAuth1Session(CK, CS, AT, AS)
                params = {'track': 'Lv%s %s' % (Enemy[0], Enemy[1])}
                req = oauth_session.post(FILTER_URL, params=params, stream=True, verify = False)
                #tweet表示
                for line in req.iter_lines():
                    tweet = json.loads(line.decode("utf-8"))
                    # Stopボタンを押した後 ↓ でループを抜けthreadをKill
                    if stop_flag == True:
                        break
                        thread.join()
                    # pass tweets via the game page
                    if tweet.get('source') == '<a href="http://granbluefantasy.jp/" rel="nofollow">グランブルー ファンタジー</a>':
                        raid_id = parse(tweet.get('text'))
                        if raid_id:
                            set_clipboard(raid_id, os_name)
                        text_widget.insert("1.0",tweet.get("text")+ "\n")
                        if sound_chk.get() == True:
                            ws.PlaySound('SystemAsterisk', ws.SND_ALIAS)

            except json.JSONDecodeError as e:
                text_widget.insert("1.0",'再取得\n')
                error += 1
                if error >= 3:
                    text_widget.insert("1.0",'読み込みエラー 再度実行してください\n')
                    button1.configure(state=tk.NORMAL)
                    error = 0
                    thread=None
                    break
                    thread.join()
                pass

    def start_btn():
        global stop_flag, thread
        button1.configure(state=tk.DISABLED)
        # スレッドが無いなら生成してstart()する
        if not thread:
            thread = threading.Thread(target=start)
            stop_flag=False
            thread.start()

    def stop_btn():
        global stop_flag, thread
        button1.configure(state=tk.NORMAL)
        # スレッドがある場合停止してjoin()する
        if thread:
            stop_flag=True
            thread.join()
            thread=None
        
    frame2 = ttk.Frame(root, padding=(0,5))
    frame2.grid(row=0, column=0, sticky=W+N)

    button1 = ttk.Button(frame2, text="Start", command=start_btn)
    button1.pack(side=LEFT)

    button2 = ttk.Button(frame2, text="Stop",command=stop_btn)
    button2.pack(side=LEFT)

    root.mainloop()
    # 終了時にスレッドを停止する処理
    if thread:
        stop_flag=True
        thread.join()