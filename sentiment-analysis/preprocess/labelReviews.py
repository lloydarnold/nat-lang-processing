NEG_REVIEWS_PATH = ""
POS_REVIEWS_PATH = ""

NEG_REVIEWS_PATH_LAB = ""
POS_REVIEWS_PATH_LAB = ""


def add_labels(filePath=Null,labelledFilePath=Null, label=Null):
    if not(filePath and labelledFilePath and label):
        print("Not enough parameters passed to add labels")
        return

    outFile = open(labelledFilePath, 'a')
    for line in open(filePath, 'r'):
        line=line.strip("\n")
        line = line + (" | %d \n" %label)


def main():
    pass


if __name__ == "__main__":
    main()
