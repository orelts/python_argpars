import sys
import argparse
import itertools as it


parser = argparse.ArgumentParser()
# add_argument push back so when inerting to dict it happens from the bottom up
parser.add_argument("-D ", help="argument3", type=int, nargs='?', default=0, dest="D")
parser.add_argument("-C ", help="argument3",  nargs='*', default=[0], dest="C")
parser.add_argument("-B ", help="argument2",  nargs='*', default=[0], dest="B")
parser.add_argument("-A", help="argument1", nargs='*', default=[0], dest="A")
args = parser.parse_args()

d = {}
map = {}

loop_num = 0
for arg in vars(args):
    if type(getattr(args, arg)) is not list:
        continue
    attr = getattr(args, arg)
    d[arg] = getattr(args, arg)
    map[arg] = loop_num
    loop_num += 1

keys, values = zip(*d.items())
for v in it.product(*values):
    print("command A=%s B=%s C=%s D=%d" %(v[map["A"]], v[map["B"]], v[map["C"]], args.D))
    print("command close -A=%s" %(v[map["A"]]))
    print("\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

