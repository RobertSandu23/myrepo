import os
import time


class LinuxCommands:
    def __init__(self):
        pass
 
    def pwd(self):
        path = os.getcwd()
        return os.system(f'pwd')
    
    def ls(self):
        pwd = os.getcwd()
        ls = f"ls {pwd}"
        return os.system(ls)
    
    def ps(self):
        os.system('ps -la')
    
    def mkdir_touch_rm(self):
        pwd = os.getcwd()
        cd = 'cd TestDir'
        os.system(f'cd {pwd}')
        os.system("mkdir TestDir")
        time.sleep(1)
        os.system(f"{cd} && touch hi.txt && echo 'Hello I am here for 10 seconds only' >> hi.txt")
        time.sleep(10)
        os.system(f"{cd} && echo 'Closed. File was removed' >> hi.txt")
        time.sleep(1)
        os.system(f"rm -r TestDir")
    

linux = LinuxCommands()
print("===results===")
print("\n===pwd===")
pwd = linux.pwd()
print("\n===ls===")
ls = linux.ls()
print("\n===ps===")
ps = linux.ps()
print("\n===dir_manager===\ncheck your current working directory, search for TestDir and open hi.txt")
dir = linux.mkdir_touch_rm()