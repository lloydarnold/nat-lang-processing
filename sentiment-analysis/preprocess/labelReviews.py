NEG_REVIEWS_PATH = ""
POS_REVIEWS_PATH = ""

NEG_REVIEWS_PATH_LAB = ""
POS_REVIEWS_PATH_LAB = ""


def add_labels(filePath=None, labelledFilePath=None, label=None):
    if not(filePath and labelledFilePath and label):
        print("Not enough parameters passed to add labels")
        return

    outFile = open(labelledFilePath, 'a')
    for line in open(filePath, 'r'):
        line=line.strip("\n")
        line = line + (" | %d \n" %label)
        outFile.write(line)


def main():
    testPath1 = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/test/testRaw1_clean"
    testPath2 = testPath1 + "_lab"
    add_labels(testPath1, testPath2, 1)


if __name__ == "__main__":
    main()
