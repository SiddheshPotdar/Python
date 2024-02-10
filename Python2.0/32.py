# copyfile(): copies contents of the file
# copy(): copyfile() + permission mode + destianation can be directory
# copy2(): copy() + copyise metadata

import shutil

shutil.copyfile("copy\\first.txt", "copy\\second.txt") # (src, dir)

shutil.copy('copy\\first.txt', "copy\\third.txt")

shutil.copy2("copy\\first.txt", "copy\\fourth.txt")


#* copyfile() vs copy()
shutil.copyfile("copy\\original.txt", "copy\\copyfile.txt")
shutil.copy("copy\\original.txt", "copy\\copy.txt")
