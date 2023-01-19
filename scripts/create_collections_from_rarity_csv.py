import sys
from utils.Collection import Collection

def usage(prog_name: str):
    print("<path to python3> " + prog_name + " <path to Rarity generated csv file>")

def main(argc: int, argv):
    td = Collection()
    td.create()

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        usage(sys.argv[0])
        exit(1)
    
    main(len(sys.argv), sys.argv[1])
