import sys

def main(opener):
    f = opener.open(sys.argv[1], mode='wt', encoding="utf8" )
    f.write(' '.join(sys.argv[2:]))
    f.close()