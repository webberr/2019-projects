#! python3
import os

myFiles = ['index.ejs', 'README.md', 'package.json']
# os.chdir('C:\Users\ryan_\src')

# print(os.getcwd())

# for filename in myFiles:
#         print(os.path.join('C:\\Users\\ryan_\\src', filename))

installDir = 'C:\\InstallDir\\'
totalSize = 0
# if(not os.path.exists(installDir)):
#     os.makedirs(installDir)

# os.path.getsize('C:\\Windows\\System32\\calc.exe')
# os.listdir('C:\\Windows\\System32')

# print(os.path.realpath(installDir))
for filename in os.listdir('C:\\Windows\\System32'):
      totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(totalSize)