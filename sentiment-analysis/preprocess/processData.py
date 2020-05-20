import cleanWords
import buildWordMap
import labelReviews
import shuffle

DATA_DIR = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data"

RAW_POS = DATA_DIR + "raw/pos_reviews"
RAW_NEG = DATA_DIR + "raw/neg_reviews"
CLEAN_POS = DATA_DIR + "processed/pos_clean"
CLEAN_NEG = DATA_DIR + "processed/neg_clean"
LAB_POS = DATA_DIR + "processed/pos_rev_lab"
LAB_NEG = DATA_DIR + "processed/neg_rev_lab"
PROCESSED_SET = DATA_DIR + "processed/all_reviews"

TEST_SET = DATA_DIR + "processed/test"
TRAIN_SET = DATA_DIR + "processed/train"

WORD_MAP_PATH = DATA_DIR + "/processed/wordMap.json"

def main():
    pass


if __name__ == '__main__':
    main()
