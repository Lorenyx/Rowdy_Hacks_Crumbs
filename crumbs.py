#!/usr/bin/env python3
import argparse
import os

import sys_identify

if __name__ =='__main__':
    parser=argparse.ArgumentParser(
        description='''CRUMBS is a python app that verifies current checksums with provided sum or online repository (Debian, Arch)''',
        epilog="""All is well that ends well."""
        )
    parser.add_argument('Path', type=str, default='/bin/bash', help='Path pointing to executable file or directory of executable files')
    parser.add_argument('--hash', type=str, help="Hash of the file used for checking. MUST MATCH system repository sum provided. (Debian = MD5Sum, Arch = MD5Sum")
    parser.add_argument('-d', '--directory', type=str, help='Directory of files to verify')
    args=parser.parse_args()

    #TODO remove testing
    print(args.Path)
    print(args.Hash)
    #TODO end of testing

    # provided Path is a file
    if os.path.isfile(args.Path):
        # Comparse hash to provided one
        if not args.Hash:
            args.Hash = 'md5sum'
        # get_file_hash(args.Path, args.Hash.lower())
        print(f'Decoding {args.Path} into {args.Hash}')