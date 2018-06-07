##------------------------------------------------------------------##
## pythonnet を利用する場合、まず最初に clr をインポートする
##------------------------------------------------------------------##
import clr

##------------------------------------------------------------------##
## 名前空間の指定
##------------------------------------------------------------------##
clr.AddReference('System.Diagnostics.Process')

##------------------------------------------------------------------##
## インポート宣言
##------------------------------------------------------------------##
import sys
from time import sleep

import System   # .NET Framework

##------------------------------------------------------------------##
## メイン処理
##------------------------------------------------------------------##
argv = sys.argv
argc = len(argv)

if (argc < 2):
	#引数の個数チェック
	print('Usage: python %s ExecCommand <exitWait>' %argv[0] )
	quit()

if (argc >= 3):
  if (int(argv[2]) > 0):
    exitWait = 1
  else:
    exitWait = 0
else:
  exitWait = 0

ps = System.Diagnostics.Process()
ps.Start(argv[1])

#processID = ps.Id
#print("ProcessID = %d is started." %processID)

if (exitWait == 1):
  ps.WaitForExit()
  #print("ProcessID = %d is done." %processID)
