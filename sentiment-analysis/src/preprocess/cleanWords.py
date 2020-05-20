import os
import re
from pathlib import Path

FILE_PATH = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/raw/pos_reviews"
CLEAN_FILE_PATH = FILE_PATH + "_clean"

def clean_data(filePath = FILE_PATH, cleanFilePath = CLEAN_FILE_PATH):
    '''Remove all non-alphabetic characters.'''

    with open(cleanFilePath, 'w+') as writer:
        writer = open(cleanFilePath, 'w+')
        for line in open(filePath):
            line=line.rstrip()  # Remove whitespace
            if line:
                line=re.sub('[^A-Za-z\d]+', ' ', line)     #Match all non alphanumeric characters and get rid of them
                line=line.lower()                         # Set line to lowercase
                if len(line)>1:
                    writer.write(line+'\n')

def main():
    print("Usage: clean_data( path for file in, path for file out )")


if __name__ == "__main__":
    main()
