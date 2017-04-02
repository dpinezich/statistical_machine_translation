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

    number_of_words = 2

    save_line = []
    text_to_line = {}

    # open the corpus and store all phrases with the length expected
    with open("align/corpus.es-en", "r") as corpus:
        for index, c in enumerate(corpus):
            splitted_line = c.split("|||")

            count_es = len(splitted_line[0].split())
            count_en = len(splitted_line[1].split())

            if (count_es <= number_of_words and count_en <= number_of_words):
                text_to_line[index] = ["index", str(splitted_line[0]).strip().split(), str(splitted_line[1]).strip().split()]
                # save all relevant lines for a faster gdfa searching
                save_line.append(index)

    corpus.close()
    print u"corpus is ready"

    with open("align/alignments.gdfa", "r") as alignment:
        for index, a in enumerate(alignment):
            if (index in save_line):
                text_to_line[index][0] = a.strip()

    alignment.close()
    print u"alignment is ready"

    for i in text_to_line:
        print i

if __name__ == '__main__':
    main()