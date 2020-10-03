from Utility import Utility

print("checking all the necessary dir exist or not")
dirs = Utility.getAllDir()
for dir in dirs:
    Utility.ensureDir(dirs[dir])

