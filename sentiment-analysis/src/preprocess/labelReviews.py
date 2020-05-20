NEG_REVIEWS_PATH = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/raw/pos_reviews_clean"
POS_REVIEWS_PATH = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/raw/pos_reviews_clean"

NEG_REVIEWS_PATH_LAB = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/processed/neg_rev_lab"
POS_REVIEWS_PATH_LAB = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/processed/pos_rev_lab"


def add_labels(filePath=None, labelledFilePath=None, label=None):
    if not(filePath and labelledFilePath and label != None):
        print("Not enough parameters passed to add labels")
        return

    outFile = open(labelledFilePath, 'a')
    for line in open(filePath, 'r'):
        line=line.strip("\n")
        line = line + (" | %d \n" %label)
        outFile.write(line)


def main():
    print("Usage: add_labels( path for file in, path for file out, label to add )")


if __name__ == "__main__":
    main()
