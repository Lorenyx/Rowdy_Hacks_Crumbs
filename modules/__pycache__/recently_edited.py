import os.path
import time
from datetime import date, datetime

def recently_edited(bin:str):
    "warns users if the bin has recently been updated"
    path="/usr/bin/{}".format(bin)
    if (os.path.isfile("/usr/bin/"+bin)):
        modified = date.fromtimestamp(os.path.getmtime(path))
        current = date.fromtimestamp(time.time())
        elapsed = current-modified
        if (elapsed.days < 14):
            print("Friendly reminder {} has been modified within 14 days of this program running".format(bin))
    
        
    else:
        return 1
if __name__ == "__main__":
    recently_edited("neofetch")
