import cleanWords as cw
import buildWordMap as bm
import labelReviews as lr
import shuffle as sh
import splitSet as ss

DATA_DIR = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data"

RAW_POS = DATA_DIR + "/raw/pos_reviews"
RAW_NEG = DATA_DIR + "/raw/neg_reviews"
CLEAN_POS = DATA_DIR + "/processed/pos_clean"
CLEAN_NEG = DATA_DIR + "/processed/neg_clean"
LAB_POS = DATA_DIR + "/processed/pos_rev_lab"
LAB_NEG = DATA_DIR + "/processed/neg_rev_lab"
PROCESSED_SET = DATA_DIR + "/processed/all_reviews"

TEST_SET = DATA_DIR + "/processed/test"
TRAIN_SET = DATA_DIR + "/processed/train"

WORD_MAP_PATH = DATA_DIR + "/processed/wordMap.json"


def clean():
    cw.clean_data(RAW_POS, CLEAN_POS)
    cw.clean_data(RAW_NEG, CLEAN_NEG)


def label():
    lr.add_labels(CLEAN_NEG, LAB_NEG, 0)
    lr.add_labels(CLEAN_POS, LAB_NEG, 1)


def main():
    clean()
    bm.build_word_map([CLEAN_POS, CLEAN_NEG], WORD_MAP_PATH)
    label()
    sh.shuffle([LAB_POS, LAB_NEG], PROCESSED_SET)
    ss.split_set(PROCESSED_SET, TEST_SET, TRAIN_SET, 200)


if __name__ == '__main__':
    main()
