


import subprocess

def get_hash(bin:str):
    "Retrieves the hash for a program using arch"
    
    hash_check = subprocess.run("md5sum {}".format(bin).split(),stdout=subprocess.PIPE,encoding='utf-8')
    info = {}
    output = hash_check.stdout.split("\n")[:-1]
    return output[0].split(" ")[0]
    
    
      
        

    

if __name__ == "__main__":
    get_hash("/usr/bin/htop")