import win32com.client
from time import sleep

shell = win32com.client.Dispatch("WScript.Shell")
ex = shell.Exec("notepad.exe")

ProcessID  = ex.ProcessID
print("ProcessID = %d is started." %ProcessID)

while (ex.status == 0):
  sleep(0.1)

print("ProcessID = %d is done." %ProcessID)
