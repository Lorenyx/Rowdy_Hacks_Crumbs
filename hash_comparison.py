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
def get_hash(path, hash_algo):
    # provided Path is a file
    if os.path.isfile(path):
        # Comparse Hash to provided one
        print(f'*** Decoding file {path} into {hash_algo}')
        get_hash_from_file(path, hash_algo)

    if os.path.isdir(path):
        # call get_all_file_Hash
        print(f'*** Decoding dir {path} into {hash_algo}')
        get_hash_from_dir(path, hash_algo)



def get_hash_from_dir(dir_path, hash_algo):
    """Returns list of hashes for all files in directory"""
    if not os.path.isdir(dir_path):
        print(f"[-] Cannot find directory at {dir_path}")
        return

    hashes = []
    for file in os.listdir(dir_path):
        hashes.append(get_hash_from_file(os.path.join(dir_path, file), hash_algo))
    return hashes


def get_hash_from_file(file_path, hash_algo):
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