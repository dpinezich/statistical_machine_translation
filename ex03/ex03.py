#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ David Pinezich <s11729464>
# __author__ Christian Schneider <s10606002>

import re

# main programm
def main():

    import sys, getopt

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

    file_uri_list = sys.argv;




    save_line = []
    text_to_line = {}
    with open(file_uri_list[1], "r") as corpus:
        for index, c in enumerate(corpus):
            splitted_line = c.split("|||")

            count_es = len(splitted_line[0].split())
            count_en = len(splitted_line[1].split())

            if (count_es < 3 and count_en < 3):
                text_to_line[index] = str(splitted_line[0]) + "|||" + str(splitted_line[1])
                save_line.append(index)
    corpus.close()


    with open(file_uri_list[2], "r") as alignment:
        for index, a in enumerate(alignment):
            if (index in save_line):
                print str(index) + ": " + str(a) + text_to_line[index]

    alignment.close()

if __name__ == '__main__':
    main()