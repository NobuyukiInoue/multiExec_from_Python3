import sys
import win32com.client
from time import sleep

shell = win32com.client.Dispatch("WScript.Shell")

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

ex = shell.Exec(argv[1])

ProcessID  = ex.ProcessID
print("ProcessID = %d is started." %ProcessID)

if (exitWait == 1):
  while (ex.status == 0):
    sleep(0.1)
  print("ProcessID = %d is done." %ProcessID)
