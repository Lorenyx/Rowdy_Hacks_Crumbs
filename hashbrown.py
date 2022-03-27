#!/usr/bin/env python3
import argparse
import os

import modules.sys_identify as sys_identify
from hash_comparison import get_file_hash, list_algos #TODO move into modules/ 

PROG_NAME = 'HASHBROWN'
AUTHORS = ['_','_','Mason Eckenrod']

if __name__ =='__main__':
    parser=argparse.ArgumentParser(
        description=f'''{PROG_NAME} is a python app that verifies current checksums with provided sum or online repository (Debian, Arch)''',
        epilog=f"""Rowdy Hacks 2022 written by {', '.join(AUTHORS)}."""
        )
    parser.add_argument('Path', type=str, default='/bin/bash', help='Path pointing to executable file or directory of executable files, or list of comma seperated files')
    parser.add_argument('--hash', type=str, default=None, help="Hash of the file used for checking. (Note. Repositories only provide md5sum for files)")
    parser.add_argument('--hash-algo', '--algo', type=str, default='md5sum', help=f"Algorithm used for provided hash to verify against. ALGOS:{', '.join(list_algos())}")
    args=parser.parse_args()

    # provided Path is a file
    if os.path.isfile(args.Path):
        # Comparse Hash to provided one
        
        result = get_file_hash(args.Path, args.hash_algo.lower())
        print(f'Decoding {args.Path} into {args.hash_algo}')

    if os.path.isdir(args.Path):
        # call get_all_file_Hash
        
        # get_dir_Hashes(args.Path, args.hash)
        print(f'Decoding files in {args.Path} to {args.hash}')