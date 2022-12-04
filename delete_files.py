#!/usr/bin/python3

'''
Delete files that are older than 30 days old
'''

from datetime import datetime
from pathlib import Path


def main():
    """ function main """
    today = datetime.today()
    print(f'The following files will be deleted...')

    for i in Path('/home').rglob('*'):
        mtime = datetime.fromtimestamp(i.stat().st_mtime)
        filetime = mtime - today
        if filetime.days <= 30:
            print(f'{i.name:<20}: {abs(filetime.days)} days old')
            i.unlink()

if __name__ == "__main__":
    main()