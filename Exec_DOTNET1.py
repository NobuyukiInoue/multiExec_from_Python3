import clr
import System   # .NET Framework

clr.AddReference('System.Diagnostics.Process')

ps = System.Diagnostics.Process()
ps.Start("notepad.exe")

#processID = ps.Id
#print("ProcessID = %d is started." %processID)

#ps.WaitForExit()
