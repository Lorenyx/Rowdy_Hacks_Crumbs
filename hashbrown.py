#!/usr/bin/env python3
import argparse
import os

from hash_comparison import get_hash, list_algos #TODO move into modules/ 

PROG_NAME = 'HASHBROWN'
AUTHORS = ['_','Isaiah Flores 🤠','Mason Eckenrod']

if __name__ =='__main__':
    parser=argparse.ArgumentParser(
        description=f'''{PROG_NAME} is a python app that verifies current checksums with provided sum or online repository (Debian, Arch)''',
        epilog=f"""Rowdy Hacks 2022 written by {', '.join(AUTHORS)}."""
        )
    parser.add_argument('Path', type=str, default='/bin/bash', help='Path pointing to executable file or directory of executable files, or list of comma seperated files')
    parser.add_argument('--hash', type=str, default=None, help="Hash of the file used for checking. (Note. Repositories only provide md5sum for files)")
    parser.add_argument('--hash-algo', '--algo', type=str, default='md5sum', help=f"Algorithm used for provided hash to verify against. ALGOS: {', '.join(list_algos())}")
    parser.add_argument('--script-file', '-f', action="store_true", help="Flag if Path points to file storing entries. (entries should be store as PATH:ALGO:HASH)")
    parser.add_argument('--verbose', '-v', action='store_true', help="Enable verbose output")
    #TODO add verbose option to print all lines
    args=parser.parse_args()

    
    # Call hash function
    if args.script_file:
        #TODO Parse input file and call args
        pass
    else:
        cur_hash = get_hash(args.Path, args.hash_algo) #TODO return dict of file: hash
        if args.hash is None:
            exp_hash = get_hash_from_repo(args.Path, args.hash_algo)#TODO return dict of file: hash
        
        if isinstance(cur_hash, dict):
            results = {k: r == e for k, r in cur_hash for k2, e in exp_hash}

            for file_name, hash_match in results:
                if hash_match and args.verbose:
                    print(f"*** MATCH {file_name} @ {cur_hash[file_name]}")
                else:
                    print(f"""*** NOT MATCH {file_name} 
                    CURRENT  -> {cur_hash[file_name]}
                    EXPECTED -> {exp_hash[file_name]}
                    """)
        if isinstance(cur_hash, str):
            result = cur_hash[args.Path] == exp_hash[args.Path]
            if result and args.verbose:
                print(f"*** MATCH {file_name} @ {cur_hash[file_name]}")
            else:
                print(f"""*** NOT MATCH {file_name} 
                CURRENT  -> {cur_hash[file_name]}
                EXPECTED -> {exp_hash[file_name]}
                """)
            