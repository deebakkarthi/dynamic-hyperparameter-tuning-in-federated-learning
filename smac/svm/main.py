#!/usr/bin/env python
import os
import pickle

import numpy as np

DATA_DIR = "./data/"


def load_cifar_10_train():
    num_samples = 50000
    image_size = 3072
    batch_size = 10000
    X = np.empty((num_samples, image_size), dtype=np.uint8)
    y = np.empty(num_samples, dtype=np.uint8)
    index = 0
    for file_name in os.listdir(DATA_DIR):
        if file_name.startswith("data_batch_"):
            file_path = os.path.join(DATA_DIR, file_name)
            with open(file_path, "rb") as file:
                batch_data = pickle.load(file, encoding="bytes")
                X[index : index + batch_size] = batch_data[b"data"]
                y[index : index + batch_size] = batch_data[b"labels"]
                index += batch_size
    return X, y


def load_cifar_10_test():
    file_path = os.path.join(DATA_DIR, "test_batch")
    with open(file_path, "rb") as file:
        batch_data = pickle.load(file, encoding="bytes")
        X = np.array(batch_data[b"data"])
        y = np.array(batch_data[b"labels"])
    return X, y
