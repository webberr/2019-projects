#! python3
import os

myFiles = ['index.ejs', 'README.md', 'package.json']
# os.chdir('C:\Users\ryan_\src')

# print(os.getcwd())

# for filename in myFiles:
#         print(os.path.join('C:\\Users\\ryan_\\src', filename))

installDir = 'C:\\InstallDir\\'
if(not os.path.exists(installDir)):
    os.makedirs(installDir)

print(os.path.realpath(installDir))