#!/usr/bin/env python3
import argparse
import os

from hash_comparison import get_hash, get_hash_from_repo, list_algos #TODO move into modules/ 

PROG_NAME = 'HASHBROWN'
AUTHORS = ['_','Isaiah Flores 🤠','Mason Eckenrod']

if __name__ =='__main__':
    parser=argparse.ArgumentParser(
        description=f'''{PROG_NAME} is a python app that verifies current checksums with provided sum or online repository (Debian, Arch)''',
        epilog=f"""Rowdy Hacks 2022 written by {', '.join(AUTHORS)}."""
        )
    parser.add_argument('Path', type=str, default='/bin/bash', help='Path pointing to executable file or directory of executable files, or list of comma seperated files')
    parser.add_argument('--hash', '-x', type=str, default=None, help="Hash of the file used for checking. (Note. Repositories only provide md5sum for files)")
    parser.add_argument('--hash-algo', '--algo', '-a', type=str, default='md5', help=f"Algorithm used for provided hash to verify against. ALGOS: {', '.join(list_algos())}")
    parser.add_argument('--only-hash', '-O', action='store_true', help='Whether to only store the hashes of the files and not compare them, (Output in PATH:ALGO:HASH)')
    parser.add_argument('--script-file', '-f', action="store_true", help="Flag if Path points to file storing entries. (entries should be store as PATH:ALGO:HASH)")
    parser.add_argument('--quiet', '-q', action='store_false', help="Enable verbose output")
    
    args=parser.parse_args()

    # handle ONLY HASH
    if args.only_hash:
        cur_hash = get_hash(args.Path, args.hash_algo, False)
        if isinstance(cur_hash, dict):
            for k in cur_hash:
                print(f"{k}:{args.hash_algo}:{cur_hash[k]}")
                exit(0)
        if isinstance(cur_hash, str):
            print(f"{args.Path}:{args.hash_algo}:{cur_hash}")
            exit(0)
    
    # handle SCRIPT FILE
    if args.script_file:
        #TODO Parse input file and call args
        pass
    # handle BASE CASE
    else:
        cur_hash = get_hash(args.Path, args.hash_algo) 

        if args.hash:
            exp_hash = args.hash
        else:
            #TODO handle mismatch algo
            exp_hash = get_hash_from_repo(args.Path, args.hash_algo)
            # print('[-] Missing hash value or file of hashes to compare against')
            # exit(-2)

        if isinstance(cur_hash, dict):
            # handle dictionary of hashes
            for key in zip(cur_hash.keys(), exp_hash.keys()):
                is_match = cur_hash[key] == exp_hash[key]
                print(cur_hash[key])
                print(exp_hash[key])
                print(key)
                if not is_match:
                    print(f"""*** NOT MATCH @ {key} 
    CURRENT  -> {cur_hash[key]}
    EXPECTED -> {exp_hash[key]}""")

                elif args.quiet:
                    print(f"*** MATCH {key} @ {cur_hash[key]}")
                
        if isinstance(cur_hash, str):
            # Handle single hash to exp hash
            is_match = cur_hash == exp_hash

            if exp_hash.strip() == "":
                print(f"[-] Could not find expected hash for {args.Path}")
                exit(1)

            if not is_match:
                print(f"""*** NOT MATCH @ {args.Path} 
    CURRENT  -> {cur_hash}
    EXPECTED -> {exp_hash}""")

            elif args.quiet:
                print(f"*** MATCH {args.Path} @ {cur_hash}")
