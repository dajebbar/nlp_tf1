import os
from datetime import datetime

"""
+ os.getcwd() => get current working directory

+ os.chdir(<path>) => change directory 

+ os.listdir() => list directory

+ os.mkdir(<dirname>) => create a directory

+ os.makedirs(<dirname>) => make directories recursively

+ os.rmdir(<dirname>) => remove directory

+ os.removedirs(<dirname>) => remove directory recursively

+ os.rename(<from>, <to>) => rename file

+ os.stat(<filename>)  => print all info of a file

+ os.walk(<path>) => traverse directory recursively

+ os.environ => get environment variables

+ os.path.join(<path>, <file>) => join path without worrying about /

+ os.path.basename(<filename>) => get basename

+ os.path.dirname(<filename>) => get dirname

+ os.path.exists(<path-to-file>) => check if the path exists or not

+ os.path.splitext(<path-to-file>) => split path and file extension

+ dir(os) => check what methods exists
"""

print(f"The current directory is : {os.getcwd()}")

print(f"It contains: {os.listdir()}")

print("changing directory...")

os.chdir("/home/ehp/Documents/NLP_Labs/nlp_tf1/text_preprocessing")

print(f"The current directory now is : {os.getcwd()}")

print(f"It contains: {os.listdir()}")

# create os-demo directory
print("Creating os-demo directory...")
os.makedirs("os-demo", exist_ok=True)
print(f"It contains: {os.listdir()}")

# rename test.txt
print("renaming file...")
os.rename("test.txt", "demo.txt")

# getting info from demo.txt
print("getting infos...")
print(os.stat("demo.txt"))

modification_time = os.stat('demo.txt').st_mtime
print("get modification time")
print(datetime.fromtimestamp(modification_time))
print()
print("*-*" * 15)

fpath = "/home/ehp/Documents/NLP_Labs"

print("Get files tree...")
for dirpaths, dirnames, filenames in os.walk(fpath):
    print(f"Current path: {dirpaths}")
    print(f"Directories: {dirnames}")
    print(f"Files: {filenames}")
    print()

fp = os.getcwd()
op = os.path.join(fp, "demo.txt")
print(op)
print(os.path.exists(op))