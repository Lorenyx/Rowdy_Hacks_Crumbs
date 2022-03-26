#python project to store the checksums for comparison
import os 
from os.path import isfile, join

file_path = input("Enter file path: ")

#base_path = r"C:\users\josea\Documents\miscellanus"
base_path = file_path
file_ls = [f for f in os.listdir(base_path) if isfile(join(base_path, f))]

for f in file_ls:
    print(f)




