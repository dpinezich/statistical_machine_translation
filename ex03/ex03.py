#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ David Pinezich <s11729464>
# __author__ Christian Schneider <s10606002>

# Hello intruder, we heard you like github: https://github.com/dpinezich/statistical_machine_translation :)

# Class struct for all the joys of sorting and stuff
class Calculated:
    def __init__(self, word, foreign, ratio):
        self.word = word
        self.foreign = foreign
        self.ratio = ratio

    def __repr__(self):
        return repr((self.word, self.foreign, self.ratio))


# main programm
def main():

    import sys

    print
    print "------------------------------"
    print u"implement assignment from ex3"
    print "------------------------------"
    print

    speed = False
    number_of_words = 2
    file_uri_list = sys.argv;

    while True:
        try:
            input = raw_input("Would you like to work with the quick version (only using the first few items from the lists)? s=short, q=quit: ")
        except:
            print "Bad input, closing"
            exit(0)
        # quit
        if input == 'q':
            print u"Sad to see you going.... Bye!"
            exit(0)
        elif input == 's':
            print u"Quick version selected: "
            print ""
            speed = True
            break;
        else:
            print u"Normal version selected: "
            print ""
            break;

    save_line = []
    text_to_line = {}

    with open(file_uri_list[1], "r") as corpus:
        for index, c in enumerate(corpus):
            splitted_line = c.split("|||")

            # check length without removing any char, even . is legit
            count_es = len(splitted_line[0].split())
            count_en = len(splitted_line[1].split())

            if (count_es <= number_of_words and count_en <= number_of_words):
                tokens_en = splitted_line[0].split()
                tokens_es = splitted_line[1].split()
                text_to_line[index] = [tokens_en, tokens_es]
                save_line.append(index)

            # speed version
            if (len(text_to_line) > 10000 and speed):
                break
    print u"Corpus is ready"
    corpus.close()

    # create corpus entries
    corpus_entries_and_alignments = []
    with open(file_uri_list[2], "r") as alignment:
        for index, a in enumerate(alignment):
            if (index in save_line):
                line = a[0:len(a) - 1]
                splitted_line = line.split(" ")
                alignments = []

                for s_line in splitted_line:
                    splitted_alignment = s_line.split("-")
                    alignments.append([splitted_alignment[0], splitted_alignment[1]])

                corpus_entry_and_alignment = []
                corpus_entry = text_to_line[index]
                corpus_entry_and_alignment.append(corpus_entry)
                corpus_entry_and_alignment.append(alignments)
                corpus_entries_and_alignments.append(corpus_entry_and_alignment)

            # speed version
            if (len(corpus_entries_and_alignments) > 10000 and speed):
                break
    print u"Alignment is ready"
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
        current_alignments = ca[1];
        current_corpus_entry = ca[0];
        for a in current_alignments:
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
    print u"Extraction is done"


    # calculate and print probabilities
    calculated_triples = []
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
        calculated_triples.append(Calculated(e[0], e[1], str(ratio)))

    print u"Calculation is done"
    print u"*******************"
    print

    sorted_calculated_triples = sorted(calculated_triples, key=lambda calculated: calculated.word)

    out_list = []
    for out in sorted_calculated_triples:
        if(out.word not in out_list):
            out_list.append(out.word)
            print out.word + " ||| " + out.foreign + " ||| " + out.ratio
    print
    print u"*******************"

if __name__ == '__main__':
    main()