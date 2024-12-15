# 動画をフレーム単位で切り取るツール
Pythonを使って簡単な操作で動画を切り取るツールです。主に超音波画像の動画を必要な部分だけ切り取って使うために作成しました。 

- OSはWindowsでのみ動作確認をしております。

## 使い方手順
### 1. プログラムのダウンロード
- [こちら](https://github.com/PT-Araisan/frame_cutter_app/blob/main/frame_cutter.py)のプログラムが保存されているページに移動します。
- 赤丸をクリックしてファイルをダウンロードします。
![demo3](https://github.com/PT-Araisan/frame_cutter_app/blob/main/assets/3.png)

- もしサンプルの動画も必要であれば[こちら](https://github.com/PT-Araisan/frame_cutter_app/blob/main/sample.mp4)から同じようにダウンロードしてください。
ダウンロードしたファイルは、フォルダを作成してその中に入れておいて下さい。切り取りたい動画も同じフォルダに入れてください。


### 2. コマンドプロンプトの起動とフォルダの移動
- コマンドプロンプトは、コマンドを使ってプログラムを操作するためのツールです。Windowsでは、次の手順でコマンドプロンプトを起動できます。
- 検索窓でコマンドプロンプトを検索してクリックします。
![demo1](https://github.com/PT-Araisan/frame_cutter_app/blob/main/assets/1.png)

※Macの場合はターミナルを使用。

- コマンドプロンプトに「cd」と半角スペースを入れて、先ほど作ったフォルダをドラッグ＆ドロップして下さい。

![demo4](https://github.com/PT-Araisan/frame_cutter_app/blob/main/assets/4.png)

※cdはプログラムを実行するフォルダを変更するコマンド。


### 3. Pythonのインストール:
-  Web上にインストール方法を説明するサイトが沢山ありますので、例えば[こちら](https://udemy.benesse.co.jp/development/python-work/python-install.html)を参考にしながらインストールを行います。


### 4. 仮想環境の作成
- 仮想環境は、プロジェクトに必要なライブラリ（必要な機能を提供するコードやツール）や依存関係を他のプロジェクトやシステム全体から隔離して管理するために使用します。
   
⓵まずコマンドプロンプトに以下を入力・実行して仮想環境を作ります（ここでは「venv」という名前で仮想環境を作ります）。

※コピペでOK。少し時間がかかります。

```bash
python -m venv venv
```

⓶仮想環境を実行します。PCやコマンドプロンプトを再起動した場合には毎回この実行が必要です。

```bash
venv\Scripts\activate
```
仮想環境が立ち上がれば、以下のように変わります。
![demo5](https://github.com/PT-Araisan/frame_cutter_app/blob/main/assets/5.png)

※Macの場合は
```bash
source venv/bin/activate
```


### 5. 必要なライブラリのインストール

- `pip`という、ライブラリをインストールするためのツール最新の状態にします。
コマンドプロンプトに以下を入力して実行します。
```bash
python -m pip install --upgrade pip
```

- ライブラリをインストールします。
```bash
pip install opencv-python 
```


### 6. プログラムの起動:
- 動画切り取りのプログラムを起動して実行します。

```bash
python frame_cutter.py
```


### 7. プログラムの使用方法
- プログラムを実行すると、「動画ファイルのパスを入力してください」と出ますのでファイル名を書いて実行します。
※サポートしている拡張子は.mp4, .avi, .mov, .mkvです。

すると、以下のようなウインドウが立ち上がります。
![demo6](https://github.com/PT-Araisan/frame_cutter_app/blob/main/assets/6.png)

ウインドウの大きさは解像度に応じて自動で決められますが、もっと大きくしたい場合にはマウスを使って広げられます。
※その際には広げた後にコマンドプロンプト上で「Ctrl + C」で一旦プログラムを終了し、再度プログラムを起動してください。

- <操作方法>

  ⓵ ウインドウを一度クリックして下さい。それによりキー入力を受け付けられるようになります。  

  ⓶ スペースを押すと自動で進みます。もう一度押すと一時停止します。  

  ⓷ 「d」キーで１フレーム進みます。「a」キーで１フレーム戻ります。  

  ⓸ speedをマウスでドラッグすると速さが変わります。  

  ⓹ 動画が最後まで進むと、コマンドプロンプトの方に「動画の範囲を切り取って保存しますか？ (yes / no)」と出力されます。  

  ⓺ yesを入力すると、切り取りを行う開始フレーム番号と終了フレーム番号を聞かれるので、任意の数値を入力します。  

  ⓻ 入力した範囲のフレームが切り取られ、動画として「clipped_video.mp4」という名前でフォルダ内に保存されます。  

うまくいくと、コマンドプロンプトはこのような表示になっているはずです。
![demo7](https://github.com/PT-Araisan/frame_cutter_app/blob/main/assets/7.png)


### 8. プログラムを次に使う場合の注意点
- コマンドプロンプトの起動、cdコマンドを使ってのフォルダ移動、仮想環境の実行（作成は必要ありません）は毎回必要です。

## お問い合わせ

何か質問や要望があれば、[Twitter の DM](https://x.com/Pt96442837Pt) からお気軽にお知らせください。

