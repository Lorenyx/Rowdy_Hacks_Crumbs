import os

from subprocess import run, STDOUT

def get_hash(binName: str, hashType: str):
    "Takes filename and hash and returns the computed hash of that file"
    #TODO Sanitize input to prevent arbitrary execution

    # Collect md5sums to prepare for parsing, 
    exit_code = run(['sudo', 'apt-get', '--print-uris', 'install', binName], capture_output=True)
    return exit_code


if __name__ == '__main__':
    retval = get_hash('neofetch', 'SHA1')
    print(f'STDOUT -> {retval.stdout}')
    print(f'STDOUT -> {retval.stderr}')