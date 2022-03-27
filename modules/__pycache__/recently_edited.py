import os.path
import time

def recently_edited(bin:str):
    "warns users if the bin has recently been updated"
    path="/usr/bin/{}".format(bin)
    if (os.path.isfile("/usr/bin/"+bin)):
        modified = time.ctime(os.path.getmtime(path))
    else:
        return -1
if __name__ == "__main__":
    recently_edited("neofetch")
