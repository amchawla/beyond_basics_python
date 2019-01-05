import glob2
from datetime import datetime
now= datetime.now()
file_name="output/"+ str(now.strftime("%Y-%m-%d-%H-%M-%S-%f")) + ".txt"
files=glob2.glob("*.txt")
with open(file_name,"w") as file:
    for filename in files:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")

