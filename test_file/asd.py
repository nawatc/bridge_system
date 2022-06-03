import argparse

def listad():
    print("asdasd")

parser = argparse.ArgumentParser(description='Example list of options', add_help=True)
parser.add_argument('-d', '--delete', dest='command', action='store_const', const='delete', help='Delete ID')
parser.add_argument('-s', '--search', dest='command', action='store_const', const='search', help='Search ID')
parser.add_argument('-l', '--list'  , dest='command', action='store_const', const='list', help='List all ID')
args = parser.parse_args()

if      args.command == 'delete':
    print('Run delete')
elif    args.command == 'search':
    print('Run search')
else:
    print('Run list')