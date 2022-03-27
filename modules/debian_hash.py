from subprocess import run, STDOUT
from os.path import basename


def get_hash(binName: str):
    "Returns md5sum of file from apt-get repository"
    #TODO Sanitize input to prevent arbitrary execution

    # Collect md5sums to prepare for parsing, 
    exit_code = run(['apt-get', '--reinstall',
    if exit_code.stderr:
        print(f'[-] {exit_code.stderr}')
        return
    last_line = str(exit_code.stdout).split(' ')[-1]
    chksum = last_line[len('MD5Sum:') : -len(r'\\n')]
    return chksum


if __name__ == '__main__':
    retval = get_hash('neofetch')
    print(f'OUT -> {retval}')