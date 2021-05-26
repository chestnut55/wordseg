
import re
import unicodedata


def load_test_set():
    """加载测试集
    """
    test_set = []
    with open("../icwb2-data/gold/pku_test_gold.utf8", encoding='utf-8') as f:
        for line in f:
            toks = re.split("\s+", line.rstrip())
            test_set.append(toks)

    return test_set


def load_train_set():
    train_set = []
    with open("../icwb2-data/training/pku_training.utf8", encoding='utf-8') as f:
        for line in f:
            toks = re.split("\s+", line.rstrip())
            train_set.append(toks)

    return train_set
