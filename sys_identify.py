import subprocess

# system OS checking
def get_os():
    info = {}

    os_info = subprocess.run("cat /etc/os-release".split(),stdout=subprocess.PIPE,encoding='utf-8')
#splits n strips
    for i in os_info.stdout.split("\n")[:-1]:
        
        key = i.split("=")[0]
        value = i.split("=")[1].strip("\"")
        info[key]=value




    if (info["NAME"].lower().startswith("arch")):
        return "Arch"
    elif (info["NAME"].lower().startswith("debian")):
        return "Debian"
    elif (info["NAME"].lower().startswith("fedora")):
        return "Fedora"
    else:
        return -1
print(get_os())