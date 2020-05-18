import os
import re

FILE_PATH = ""
CLEAN_FILE_PATH = FILE_PATH + "_clean"

def clean_data():
    '''Remove all non-alphabetic characters. .'''

    with open(CLEAN_FILE_PATH, 'w') as writer:
        for line in open(FILE_PATH):
            line=line.rstrip()  # Remove whitespace
            if line:
                line=re.sub('[^A-Za-z\d]+', '', line)     #Match all non alphanumeric characters and get rid of them
                line=line.lower()                         # Set line to lowercase
                if len(line)>1:
                    writer.write(line+'\n')

def main():
    FILE_PATH = input("Please enter path of file to clean ")

    clean_data()

if __name__ == "__main__":
    main()
