#4. Read from a File
#We used open in read mode and file.read to read and print to display

file=open("E:/python_tutorial/data.txt")
contents=file.read()
print(contents)
file.close()