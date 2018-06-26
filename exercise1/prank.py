import os
arr = os.listdir("prank")
print(arr)
os.chdir("prank")
for filename in arr:
    newfile = ''.join(i for i in filename if not i.isdigit())
    os.rename(filename, newfile)