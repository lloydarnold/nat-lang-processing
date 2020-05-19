import json
import re

WORD_MAP_PATH = ""

def build_word_map(fileIn):
    ''' Reads in file, builds word map from this and then outputs it to a JSON '''
    wordMap = {'A':0} ## Initialise dictionary -- 'A' is one of the most commonly used words, so will be present
    wordCount = 1

    for line in open(fileIn):
        tokens = tokenize(line)

def tokenize(toTokenize = ""):
    return re.split("\s", toTokenize)

def main():
    pass
    
if __name__ == '__main__':
    main()
