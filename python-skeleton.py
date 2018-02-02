import getopt
import sys


def usage():
    print 'Usage: xxx.py -i <STRING>'
    print
    print 'Options:'
    print '  -i, --input='
    print '  -h, --help         Show help message'
    print '  -v, --version      Show version'


def main(argv):
    input_str = None
    try:
        opts, args = getopt.getopt(argv, 'hi:v', ['help', 'input=', 'version'])
    except getopt.GetoptError, e:
        print('[ERROR] option parsing error:', str(e))
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit(1)
        elif opt in ("-v", "version"):
            print '0.0.1'
            sys.exit(1)
        elif opt in ("-i", "--input"):
            input_str = arg
        else:
            print 'Unknown parameter, (%s: %s)' % (opt, arg)

    if input_str is None:
        usage()
        sys.exit(1)

    print 'Your input string:', input_str
    print 'Finish !'


if __name__ == '__main__':
    main(sys.argv[1:])
