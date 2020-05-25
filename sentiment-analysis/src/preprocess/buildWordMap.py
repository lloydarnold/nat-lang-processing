import json
import re

WORD_MAP_PATH = "wordMap.json"


def build_word_map(filesIn=(), mapPath=WORD_MAP_PATH):
    """ Reads in file, builds word map from this and then outputs it to a JSON """
    wordMap = {'a': 0}  # Initialise dictionary -- 'A' is one of the most commonly used words, so will be present
    wordCount = 1

    for file in filesIn:
        for line in open(file):
            tokens = tokenize(line)
            for token in tokens:
                if token not in wordMap:
                    wordMap[token] = wordCount
                    wordCount += 1

    with open(mapPath, "w") as outfile:
        json.dump(wordMap, outfile)


def tokenize(toTokenize=""):
    return re.split("\s", toTokenize)


def main():
    print("Usage: build_word_map( [paths for files to include], path for file out (leave blank to make file in cwd) )")


if __name__ == '__main__':
    main()
