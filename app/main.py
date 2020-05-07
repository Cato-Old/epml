import sys

no_argument_warning = 'No required argument!'


def main():
    try:
        print(sys.argv[1])
    except IndexError:
        print(no_argument_warning)
