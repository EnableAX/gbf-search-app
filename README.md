
![画像](https://imgur.com/HqnzXZl.jpg)


# グランブルーファンタジー救援検索補助アプリ

python3にてtkinterを使用し作成したwindows用アプリケーションです。

python環境の入っていないパソコンでも使用できるようになっています。

win7(python環境無し)でも起動及び動作確認しました。 

開発環境=win10,python3.7.4

py2exeを使用しpython3.4.4でexe書き出しをしました

## 必要なもの

TwitterAPIキー

## 使用方法

gbf-search-app.exe が入っているフォルダごと任意の場所にコピーしgbf-search-app.exeを実行してください。


1. MenuボタンからTwitter APIキー情報の入力をしOKボタンを押す(次回以降入力の必要はありません)

2. 救援一覧から入りたい救援を選択し(1種類のみ)そのサブウィンドウ下部のOKボタンを押す

3. メインウィンドウ上部のStartボタンで救援tweetのリアルタイム更新を開始

4. 更新されメインウィンドウのテキスト欄に表示された瞬間には1番上の救援IDが
クリップボードにコピーされているのでゲーム内のIDを入力する画面にペーストする

5. 別の救援に切り替える場合や停止したい場合はStartボタン横のStopボタンを押す(停止まで時間がかかる場合があります※

6. Startボタンを押した後の終了に関しましては
Menu内Exit及びウィンドウ右上の×で消していただいてかまいません(メイン終了時に実行中スレッドを消すようになっています)

7. 通知音に関してはチェックボックスにチェックが入っているとWindows標準サウンドが救援tweet表示毎に鳴るようになります。

この機能に関してもON/OFFする際にはお手数ですが一度Stopを押し更新を止めた状態で切り替えてください。


注. 救援ツイートの流れてくる頻度の低いものに関しては終了までの時間が極端に長かったり
アプリがフリーズしてしまう可能性も有りますがその際はお手数ですがアプリの再起動をしていただけると助かります

注2. 救援tweetの流れてくる頻度が低かったりした場合の再取得が3回発生するとフリーズ及びアクセス過多による420エラー回避のため自動ストップになります


TwitterAPIキーの取得は少し調べるとたくさん出てくるので割愛します、

英文で書く必要がありますがGoogle先生の翻訳だけで申請は通りますので頑張ってください。

## その他

現状は英文の救援tweetは拾えませんがそのうち更新するかも。

参考とPython環境無しでも使用出来たらなと思ったpyスプリクトのURLも下記に記載しておきます。

https://github.com/bookii/gbf-rapid-search
