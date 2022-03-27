#python project to store the checksums for comparison
import os 
from os.path import isfile, join
import hashlib


BLOCK_SIZE = 65536

# file_path = input("Enter file path: ")

# base_path = file_path
# file_ls = [f for f in os.listdir(base_path) if isfile(join(base_path, f))]

# for f in file_ls:
#     print(f)


def get_file_hash(file_path, hash_algo):
    """Returns hash of file at filePath at hashAlgo"""
    if not os.path.isfile(file_path):
        print(f"[-] Cannot open file at {file_path}")
        return

    if hash_algo in hashlib.algorithms_available:
        file_hash = hashlib.new(hash_algo) # Create the hash object, can use something other than `.sha256()` if you wish
    else:
        print(f'[-] Hash algo "{hash_algo}" does not exist')
        return

    with open(file_path, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file

    return file_hash.hexdigest() # Get the hexadecimal digest of the hash


def list_algos():
    return hashlib.algorithms_available