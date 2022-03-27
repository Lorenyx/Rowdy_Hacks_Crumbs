


import subprocess

def get_hash(bin:str):
    "Retrieves the hash for a program using arch"
    z
    hash_check = subprocess.run("paccheck {}".format(bin).split(),stdout=subprocess.PIPE,encoding='utf-8')
    info = {}
    print(hash_check.returncode)
    output = hash_check.stdout.split("\n")[:-1]
    
    
      
        

    

if __name__ == "__main__":
    get_hash("htop")