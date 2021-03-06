#!/usr/bin/python
from sys import argv
import zbar

def read_one_qrcode():
    # create a Processor
    proc = zbar.Processor()

    # configure the Processor
    proc.parse_config('enable')

    # initialize the Processor
    device = '/dev/video0'
    if len(argv) > 1:
        device = argv[1]
    proc.init(device)

    # enable the preview window
    proc.visible = True

    # read at least one barcode (or until window closed)
    proc.process_one()

    # hide the preview window
    proc.visible = False

    # extract results
    for symbol in proc.results:
        # do something useful with results
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

def main():
    read_one_qrcode()

if __name__ == '__main__':
    main()
