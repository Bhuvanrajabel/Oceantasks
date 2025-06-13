# File handling
import os
f = open("file.txt", "x")
print("File created")
with open("file.txt", "a") as f:
    f.write("Now the file is content!")
    f.write("Python file handling")
print("File is written")
with open("file.txt") as f:
    print(f.read())
print("File is readed")
os.remove("file.txt")
print("File deleted")
