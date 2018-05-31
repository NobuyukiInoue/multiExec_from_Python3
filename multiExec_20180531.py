#!python.exe

import sys
import os
import win32com.client
import traceback
#import time
from time import sleep

##-----------------------------------------------------------------##
## wait_enableExec function
##-----------------------------------------------------------------##
def wait_enableExec(maxProcessCount, interval, retryCount, pid_list):
  loopCount = 0

  while 1:
    # プロセス一覧から対象プロセスのPIDを検索する
    pCount = 0
        
    for i in range(0, len(pid_list)):
      if IsExist_targetProcesses(pid_list[i]):
        # 見つかった場合はカウントする
        pCount = pCount + 1
            
      else:
        # 見つからなかった場合は終了したと判断し、PIDを初期化する
        pid_list[i] = 0
    if pCount < maxProcessCount:
      # マクロ同時起動上限数を下回っている場合は、次の処理へ
      return 0
        
    loopCount += 1
                        
    if (loopCount >= retryCount):
      # 一定時間待ってもプロセス数の上限を下回らなかった場合
      print("Process Count is MAX!!")
      firstKey = ''
      while (firstKey != 'C' and firstKey != 'Q'):
        keyRet = input("Force Quit(Q) or Wait Continue(C)?")
        firstKey = keyRet[0].upper()
      if (firstKey == 'Q'):
        print("QUIT...")
        sys.exit()
      print("Continue...")
      loopCount = 0
    else:
      sleep(interval)

##-----------------------------------------------------------------##
## IsExist_targetProcesses function
##-----------------------------------------------------------------##
def IsExist_targetProcesses(target_pid):
  if (target_pid == 0):
    return 0
  # WMI Win32_Process classのオブジェクトからPIDを検索する
  locator = win32com.client.Dispatch("WbemScripting.SWbemLocator")
  server = locator.ConnectServer()
  objSet = server.ExecQuery("Select * From Win32_Process")

  for obj in objSet:
    if (obj.ProcessID == target_pid):
      return 1

  return 0

##-----------------------------------------------------------------##
## Main
##-----------------------------------------------------------------##
shell = win32com.client.Dispatch("WScript.Shell")

argv = sys.argv
argc = len(argv)

if (argc < 2):
	#引数の個数チェック
	print('Usage: python %s cmdListFileName <maxProcessCount> <interval> <retryCount> <nowait>' %argv[0] )
	quit()

if (argc >= 3):
    maxProcessCount = int(argv[2])
else:
    maxProcessCount = 4

if (argc >= 4):
  interval = int(argv[3])
else:
  interval = 4

if (argc >= 5):
  retryCount = int(argv[4])
else:
  retryCount = 4

if (argc >= 6):
  nowait = 0
else:
  nowait = 1

# ファイルをオープンする
cmdLstFile = open(argv[1], "r")

# 行ごとにすべて読み込んでリストデータにする
lines = cmdLstFile.readlines()

# ファイルをクローズする
cmdLstFile.close()

# PID保存用配列
pid_list = [0]
for i in range(1, maxProcessCount):
  pid_list.append(0)

i = 0
# 一行ずつ表示する
while i < len(lines):
  wait_enableExec(maxProcessCount, interval, retryCount, pid_list)
  p = 0
  while p < maxProcessCount:
    if (pid_list[p] == 0):
      while (lines[i][0] == '#'):
        i += 1
      if (i < len(lines)):
        lines[i] = lines[i].rstrip()
        if (lines[i][0:2] == ".\\"):
          lines[i] = lines[i][2:]
        print("%d : %s" %(i, lines[i]))
        try:
          ex = shell.Exec(lines[i])
          if (ex is not None):
            pid_list[p] = ex.ProcessID
        except Exception:
          print('%s execute Error...' %(lines[i]) )
          traceback.print_exc()
        i += 1
    if (i >= len(lines)):
      break
    p += 1
print("multiExec done...")
