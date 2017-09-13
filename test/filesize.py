import os

def func(file_name):
    file_size = os.stat(file_name).st_size

name = input("Enter file name: ")
f_extns = name.split(".")

print("Size of File is",func(file_size),'& type is',repr(f_extns[-1]))
    
