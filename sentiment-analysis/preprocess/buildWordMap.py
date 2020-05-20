import json
import re

WORD_MAP_PATH = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/test/wordMap.json"

def build_word_map(fileIn, mapPath = WORD_MAP_PATH):
    ''' Reads in file, builds word map from this and then outputs it to a JSON '''
    wordMap = {'A':0} ## Initialise dictionary -- 'A' is one of the most commonly used words, so will be present
    wordCount = 1

    for line in open(fileIn):
        tokens = tokenize(line)
        for token in tokens:
            if token not in wordMap:
                wordMap[token] = wordCount
                wordCount += 1

    with open(mapPath, "w") as outfile:
        json.dump(wordMap, outfile)


def tokenize(toTokenize = ""):
    return re.split("\s", toTokenize)


def main():
    fileIn = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/test/testRaw1_clean"
    build_word_map(fileIn)


if __name__ == '__main__':
    main()
