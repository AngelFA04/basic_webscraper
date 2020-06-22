import os

from functions import parse_home

ROOT = 'Notices/'


def run():
    """ Main program function  """
    print("Finding news...")
    parse_home()


if __name__ == "__main__":
    if not os.path.isdir(ROOT):                
        os.mkdir(ROOT)
    run()