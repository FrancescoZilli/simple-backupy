# Simple-backuPY
A simple terminal backup program made with Python.

# Usage
Wanna backup files and folders without having to deal with a lot of different GUIs? Bored of selecting files via mouse? Got you covered!
To execute a backup it's easy:you need to specify the files and folders absolute addresses in the , under the 
  - create a "backup_y.ini" file (if not present, otherwise a standard one will be created)
  - specify the absolute path of files and folders you want to backup
  - create and specify in the previously cited ".ini" file the folder(s) where you want your backup to be
  - execute "python py_backup.py"

# backup_y.ini example
[BACK UP] <br />
Z:\Users\<username>\<ancient pr0n path>\Favourites <br />
C:\Users\<username>\Desktop\passwords.txt (please don't do this) <br />
<br />
[DESTINATION] <br />
C:\Users\<username>\MY_BACKUP1 <br />
E:\Users\<username>\<incredibly dense path>\MY_BACKUP2 <br />


Written for Python 2.7.10+ 
