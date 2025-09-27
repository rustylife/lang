#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-only

from os import system
from random import randint
import sys

def main():
    system('clear')
    count = 0
    score = 0
    dic = input('dic file: ')
    if not dic:
        dic = '/home/rusty/code/lang/deu'
    print()

    dfile = open(dic, 'r')
    fcontent = dfile.readlines()
    for idx, line in enumerate(fcontent):
        if 'VOCAB' in line or 'WORTSCHATZ' in line or 'SŁOWNIK' in line:
            fcontent = fcontent[idx:]
            break
    dfile.close()

    while fcontent:
        wordnum = randint(0, len(fcontent)-1)
        word = fcontent.pop(wordnum).split(' - ', 1)
        if len(word)<2:
            continue
        print('*', word[1].strip())
        input('')
        print(word[0].strip())
        print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(0)
