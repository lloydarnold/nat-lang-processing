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
    print("Usage: shuffle( [paths for files to be shuffled together], output file path ) ")

if __name__ == '__main__':
    main()
