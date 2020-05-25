import tensorflow as tf
import re
import numpy as np


def int64_feature(value):
    if not isinstance(value, list):
        value = [value]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))


def bytes_feature(value):
    if not isinstance(value, list):
        value = [value]
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))


def _add_to_tf_records(line, tf_writer, word2idx):
    split_line = line.split('|')
    line = split_line[0]
    label = int(split_line[1].rstrip('\n'))

    if label == 1:
        label = 'positive'
        label_encoded = [0, 1]
    elif label == 0:
        label = 'negative'
        label_encoded = [1, 0]

    idx_sequence = []
    tokens = tokenize(line)

    for token in tokens:
        try:
            idx = word2idx[token]
        except KeyError:
            print('token: %s could not be found in the dictionary.' % token)
            continue

        idx_sequence.append(idx)

    idx_sequence = np.array(idx_sequence)
    seq_length = len(idx_sequence)
    idx_sequence = idx_sequence.tostring()

    example = tf.train.Example(features=tf.train.Features(feature={'text_line/encoded': bytes_feature(idx_sequence),
                                                                   'text_line/seq_length': int64_feature(seq_length),
                                                                   'label/label': bytes_feature(
                                                                       tf.compat.as_bytes(label)),
                                                                   'label/encoded': int64_feature(label_encoded)
                                                                   }))

    tf_writer.write(example.SerializeToString())


def tokenize(toTokenize=""):
    return re.split("\s", toTokenize)
