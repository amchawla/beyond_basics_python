from datetime import datetime
now= datetime.now()
file_name=str(now.strftime("%Y-%m-%d-%H-%M-%S-%f")) + ".txt"
file1=open("file1.txt","r")
file2=open("file2.txt","r")
file3=open("file3.txt","r")
with open(file_name,"w") as file:
    f1=file1.read()
    file.write(f1+"\n")
    f2=file2.read()
    file.write(f2+"\n")
    f3=file3.read()
    file.write(f3)

file1.close()
file2.close()
file3.close()

