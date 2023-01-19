import sys
from waitress import serve

from config.config import app, cfg

def usage(prog_name):
    print("Usage: python3 " + prog_name + " <config file path>")

if __name__=='__main__':
    if len(sys.argv) < 2:
        usage(sys.argv[0])
        exit(-1)

    serve(app=app, host=cfg["app"]["host"], port=cfg["app"]["port"])
