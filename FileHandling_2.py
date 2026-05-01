#4. Read from a File
#We used open in read mode and file.read to read and print to display

f=open("E:/python_tutorial/data.txt")
contents=f.read()
print(contents)
f.close()