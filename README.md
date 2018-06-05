コマンド並列実行マクロ  『multiExec_from_Python3 on Windows』  
==
Windows版のPython3からコマンドをマルチプロセスで並列実行するサンプルプログラムです。   
  

## システム要件
*Windows XP/Vista/7/8/10 or Windows Server 2008/2012/2016  
*Python 3.6以降

## ダウンロードおよび実行方法

コマンド プロンプト（またはPowerShell）を開き、git でダウンロードします。  
```
>git clone https://github.com/gx3n-inue/multiExec_from_Python3
```

## 実行方法
  
1.任意のテキストファイル(cmdList.txt)に実行したいコマンド列を列挙しておきます。１行１コマンドで記入してください。

2.下記の書式でPythonスクリプトを実行します。
```
>python multiExec.py cmdListFileName <maxProcessCount> <interval> <retryCount> <waitExit>
```
  
実行例１（最大プロセス数 = 4, プロセス一覧取得間隔 = 4[s], プロセス一覧再取得回数  = 4, 起動したプロセスの終了を待たない）  
```
>python multiExec.py cmdList.txt
```

実行例２（最大プロセス数 = 4, プロセス一覧取得間隔 = 4[s], プロセス一覧再取得回数  = 4, 起動したプロセスの終了を待つ）  
>python multiExec.py cmdList.txt 4 4 4 1


## ライセンス
  
コマンド並列実行マクロ『multiExec_from_Python3』 ver1.00  
This project is licensed under the terms of the MIT license, see LICENSE.  
