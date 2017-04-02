#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ David Pinezich <s11729464>
# __author__ Christian Schneider <s10606002>


# main programm
def main():

    import sys, getopt

    print
    print "------------------------------"
    print u"implement assignment from ex3"
    print "------------------------------"
    print

    '''
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
    '''

    # asking about whether to run the quick version
    s = False
    try:
        input = raw_input("Would you like to work with the quick version (only using the first few items from the lists)? s=short, extracts everything: ")
    except:
        print "Bad input, closing"
        exit(0)
    # quit
    if input == 's':
        s = True




    number_of_words = 2
    file_uri_list = sys.argv;




    save_line = []
    text_to_line = {}

    with open(file_uri_list[1], "r") as corpus:
        for index, c in enumerate(corpus):
            splitted_line = c.split("|||")

            count_es = len(splitted_line[0].split())
            count_en = len(splitted_line[1].split())

            if (count_es < 3 and count_en < 3):
                # text_to_line[index] = str(splitted_line[0]) + "|||" + str(splitted_line[1])
                tokens_en = splitted_line[0].split()
                tokens_es = splitted_line[1].split()
                text_to_line[index] = [tokens_en, tokens_es]
                save_line.append(index)

            if (len(text_to_line) > 200 and s):
                break

    corpus.close()

    corpus_entries_and_alignments = []

    with open(file_uri_list[2], "r") as alignment:
        for index, a in enumerate(alignment):
            if (index in save_line):
                line = a[0:len(a) - 1]
                splitted_line = line.split(" ")
                alignments = []
                for b in splitted_line:
                    splitted_alignment = b.split("-")
                    alignments.append([splitted_alignment[0], splitted_alignment[1]])
                corpus_entry_and_alignment = []
                corpus_entry = text_to_line[index]
                corpus_entry_and_alignment.append(corpus_entry)
                corpus_entry_and_alignment.append(alignments)
                corpus_entries_and_alignments.append(corpus_entry_and_alignment)
                # print str(index) + ": " + str(alignments) + ": " + str(text_to_line[index])
            if (len(corpus_entries_and_alignments) > 500 and s):
                break
    alignment.close()

    '''
        # just for testing
        for i in corpus_entries_and_alignments:
            corpus_item = i[0]
            es_iten = corpus_item[1]
            first_es_token = es_iten[0]
            print first_es_token
    '''

    # extract translations
    extracted_translations = []
    for ca in corpus_entries_and_alignments:
        previous_e_index = -1
        next_e_index = -1
        current_alignments = ca[1];
        current_corpus_entry = ca[0];
        for a in current_alignments:
            e_phrase = ""
            f_phrase = ""
            next_e_index = int(a[0]);

            current_e_phrase_from_corpus = current_corpus_entry[0]
            current_f_phrase_from_corpus = current_corpus_entry[1]

            if (next_e_index == previous_e_index and previous_e_index != -1):
                previous_extracted_translation = extracted_translations[len(extracted_translations[0]) - 1]
                e_phrase = previous_extracted_translation[0]
                f_phrase = previous_extracted_translation[1]
                f_phrase += current_f_phrase_from_corpus[int(a[1])]
            else:
                e_phrase = current_e_phrase_from_corpus[int(a[0])]
                f_phrase = current_f_phrase_from_corpus[int(a[1])]
                previous_e_index = next_e_index
            extracted_translations.append([e_phrase, f_phrase])

    # testing
    '''
    for e in extracted_translations:
    print str(e)

    '''

    # calculate and print probabilities
    for e in extracted_translations:
        count_e_and_f = 0
        count_f = 0
        for cea in corpus_entries_and_alignments:
            ce = cea[0]
            e_phrase_in_corpus = ""
            f_phrase_in_corpus = ""
            for cie in ce[0]:
                e_phrase_in_corpus += cie + " "
            e_phrase_in_corpus = e_phrase_in_corpus[0:len(e_phrase_in_corpus) - 1]

            for cif in ce[1]:
                f_phrase_in_corpus += cif + " "
            f_phrase_in_corpus = f_phrase_in_corpus[0:len(f_phrase_in_corpus) - 1]

            if (e[1] == f_phrase_in_corpus):
                count_f += 1
            if (e[0] == e_phrase_in_corpus and e[1] == f_phrase_in_corpus):
                count_e_and_f += 1
        ratio = 0
        if count_f > 0:
            ratio = float(count_e_and_f) / float(count_f)
        print e[0] + " ||| " + e[1] + " ||| " + str(ratio)


if __name__ == '__main__':
    main()