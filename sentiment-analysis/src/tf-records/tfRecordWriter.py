import tensorflow as tf
import re
import numpy as np
import json

WORD_MAP_PATH = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data" \
                "/processed/wordMap.json"

TEST_SET_PATH = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data" \
                "/processed/test"
TRAIN_SET_PATH = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data" \
                 "/processed/train"

TEST_RECORD_PATH = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/tf" \
                   "-records/test_set.tfrecord"
TRAIN_RECORD_PATH = "/home/lloyd/Documents/programming/imperative/python/natlangprocessing/sentiment-analysis/data/tf" \
                    "-records/train_set.tfrecord"


def int64_feature(value):
    if not isinstance(value, list):
        value = [value]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))


def bytes_feature(value):
    if not isinstance(value, list):
        value = [value]
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))


def add_line_to_tf_records(line, tfWriter, wordMap):
    split_line = line.split('|')
    line = split_line[0]
    label = int(split_line[1].rstrip('\n'))

    if label == 1:
        label = 'positive'
        label_encoded = [0, 1]
    elif label == 0:
        label = 'negative'
        label_encoded = [1, 0]

    map_sequence = []
    tokens = tokenize(line)

    for token in tokens:
        try:
            idx = wordMap[token]
        except KeyError:
            print('token: %s could not be found in the dictionary.' % token)
            continue

        map_sequence.append(idx)

    map_sequence = np.array(map_sequence)
    seq_length = len(map_sequence)
    map_sequence = map_sequence.tostring()

    nextLine = tf.train.Example(features=tf.train.Features(feature={'text_line/encoded': bytes_feature(map_sequence),
                                                                    'text_line/seq_length': int64_feature(seq_length),
                                                                    'label/label': bytes_feature(
                                                                        tf.compat.as_bytes(label)),
                                                                    'label/encoded': int64_feature(label_encoded)
                                                                    }))

    tfWriter.write(nextLine.SerializeToString())

def tokenize(toTokenize=""):
    return re.split("\s", toTokenize)


def create_record(dataPath, outPath, wordMapPath=WORD_MAP_PATH):
    jsonFile = open(wordMapPath)
    wordMap = json.load(jsonFile)

    with tf.python_io.TFRecordWriter(outPath) as tf_writer:
        for line in open(dataPath):
            add_line_to_tf_records(line, tf_writer, wordMap)
    print("It... worked ?? ")


def main():
    create_record(TRAIN_SET_PATH, TRAIN_RECORD_PATH)
    create_record(TEST_SET_PATH, TEST_RECORD_PATH)


if __name__ == "__main__":
    main()
