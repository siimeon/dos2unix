#!/usr/bin/python

import argparse

"""
dos2unix.py dos to unix or unix to dos file converter
"""


def dos2unix(name):
    data = open(name, 'r').read()
    open(name, 'w').write(data.replace('\r\n', '\n'))


def unix2dos(name):
    data = open(name, 'r').read()
    open(name, 'w').write(data.replace('\n', '\r\n'))


def cli_controller():
    parser = argparse.ArgumentParser(description='Dos to Unix file converter')
    parser.add_argument('file',
                        help="Path to file to be converted")
    parser.add_argument('-d',
                        '--unix2dos',
                        action='store_true',
                        help='Unix to Dos convection')
    arguments = parser.parse_args()
    if arguments.unix2dos:
        unix2dos(arguments.file)
    else:
        dos2unix(arguments.file)


if __name__ == '__main__':
    cli_controller()
