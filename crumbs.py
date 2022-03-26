#!/usr/bin/env python3
import argparse
import os

import sys_identify

if __name__ =='__main__':
    parser=argparse.ArgumentParser(
        description='''CRUMBS is a python app that verifies current checksums with provided sum or online repository (Debian, Arch)''',
        epilog="""All is well that ends well."""
        )
    parser.add_argument('Path', type=str, default='/bin/bash', help='Path pointing to executable file or directory of executable files, or list of comma seperated files')
    parser.add_argument('--Hash', type=str, default='md5sum', help="Hash of the file used for checking. MUST MATCH system repository sum provided. (Debian = MD5Sum, Arch = MD5Sum")
    args=parser.parse_args()

    #TODO remove testing
    print(args.Path)
    print(args.Hash)
    #TODO end of testing

    # provided Path is a file
    if os.path.isfile(args.Path):
        # Comparse Hash to provided one
        
        # get_file_Hash(args.Path, args.Hash.lower())
        print(f'Decoding {args.Path} into {args.Hash}')
    if os.path.isdir(args.Path):
        # call get_all_file_Hash

        # get_dir_Hashes(args.Path, args.Hash)
        print(f'Decoding files in {args.Path} to {args.Hash}')