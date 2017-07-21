# test_argparse.py
# coding: utf-8
"""Naval Fate.
 
Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
  naval_fate.py (-h | --help)
  naval_fate.py --version
 
Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
 
"""
'''
1. Overview
argparse是python用于解析命令行参数和选项的标准模块，
用于代替已经过时的optparse模块。argparse模块的作用是用于解析命令行参数，
例如python parseTest.py input.txt output.txt --user=name --port=8080。



'''
from docopt import docopt
 
if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    print(arguments)