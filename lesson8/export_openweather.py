import argparse
from MainController import MainController


def run(args):
    print(args.filename)
    mc = MainController()
    mc.query(args.filename, args.city)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('-city')

    parser.add_argument('--csv')
    parser.add_argument('--json')
    parser.add_argument('--html')

    args = parser.parse_args()

    run(args)
