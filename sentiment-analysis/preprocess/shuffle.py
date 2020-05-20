import random

def shuffle(filesIn = [], fileOut=None):
    ''' Will read in multiple files and shuffle them together, assuming they're small enough
    to fit in ram. If they're not, need to re-implement '''

    allData = []
    for file in filesIn:
        tempF = open(file, 'r')
        allData += tempF.readlines()
        tempF.close()

    for i in range(0, len(allData)):
        j = random.randint(0, len(allData) -1)
        allData[i], allData[j] = allData[j], allData[i]

    out = open(fileOut, 'w')
    for line in allData:
        out.write(line)

    out.close()


def main():
    path1 = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/test/testRaw1_clean"
    path2 = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/test/testRaw2_clean"
    path3 = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/test/finalTest"
    shuffle([path1, path2], path3)


if __name__ == '__main__':
    main()
