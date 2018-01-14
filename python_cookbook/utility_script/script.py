# encoding:UTF-8

# import argparse
#
# parser = argparse.ArgumentParser(description="search some files")
#
# parser.add_argument(dest="filenames",metavar ='filename',nargs='*')
# parser.add_argument('-p','--pat',metavar='pattern',required=True,dest='pattern',action='append',help='verbose mode')
# parser.add_argument('-v', dest='verbose', action='store_true',
#                     help='verbose mode')
#
# parser.add_argument('-o', dest='outfile', action='store',
#                     help='output file')
#
# parser.add_argument('--speed', dest='speed', action='store',
#                     choices={'slow','fast'}, default='slow',
#                     help='search speed')
#
# args = parser.parse_args()
#
#
#
# # Output the collected arguments
# print(args.filenames)
# print(args.patterns)
# print(args.verbose)
# print(args.outfile)
# print(args.speed)


import argparse

parser = argparse.ArgumentParser(description="to show how to use the python argParse package")
parser.add_argument(dest='filenames', metavar='filename', nargs='*')
parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
parser.add_argument('-o', dest='outfile', action='store', help='output file')
parser.add_argument('-speed', dest='speed', action='store',
                    choices={'slow', 'fast'}, default='slow',
                    help='search speed')

args = parser.parse_args()
print("解析输入的文件名是:\t", args.filenames)
print("verbose:\t\t", args.verbose)
print("outfiles", args.outfile)
print("speed: \t\t", args.speed)

#
# parser.add_argument('-p', '--pat', metavar='pattern',
#                     required=True, dest='patterns',
#                     action='append', help='text pattern to search')
