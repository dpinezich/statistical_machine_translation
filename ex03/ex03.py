#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ David Pinezich <s11729464>
# __author__ Christian Schneider <s10606002>

# main programm
def main():
    print
    print "------------------------------"
    print u"implement assignment from ex3"
    print "------------------------------"
    print

    while True:
        try:
            input = raw_input("Okay do you really want to start this? q=quit, anything else starts the program: ")
        except:
            print "Bad input, closing"
            exit(0)
        # quit
        if input == 'q':
            print u"Sad to see you going.... Bye!"
            exit(0)
        else:
            break;

if __name__ == '__main__':
    main()