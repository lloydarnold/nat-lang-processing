def split_set(completeSet, testOut, trainOut, testSize):
    counter = 0
    with open(completeSet, 'r') as mainFile:
        fileOut = open(testOut, 'w'):
        for line in mainFile:
            if counter == testSize:
                fileOut.close()
                fileOut = open(trainOut, 'w')
            fileOut.write(line)
            counter += 1

        mainFile.close()
        fileOut.close()


def main():
    print("Usage: split_set( path to whole set, path to test set, path to train set, size of test set ( num of lines )")


if __name__ == '__main__':
    main()
