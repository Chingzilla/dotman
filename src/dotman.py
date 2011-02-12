#!/usr/env python2
'''
dotman - dot file manager
Useful for creating, linking and backing up varius config files
'''

import os
import sys
import argparse
import json

# Setup env constants
CONFIG_HOME_DIR = os.getenv('XDG_CONFIG_HOME')
HOME_DIR = os.getenv('HOME')

def parse_arg():
    parser = argparse.ArgumentParser(description='dotman - configuration file manager')
    
    parser.add_argument('programs_to_bk', nargs='*', type=str, default='~/.config/', required=True,
        help='List of programs to backup or recover')

    parser.add_argument('-c', '--conf',
        help='location of configuration file for dotman')
    
    parser.add_argument('-d', '--backup-dest', default='~/.config/file_backups/',
        help='location of where backup files are to be stored')

    parser.add_argument('-l', '--list', action='store_true',
        help='List the files associated with given programs')

    parser.add_argument('-v' '--verbose', action='store_true',
        help='Enables')

def init():
    
def main():
    pass

if __name__ == '__main__':
    main()
