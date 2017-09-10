import csv
from feature_extraction import calculate_features

"""
    TASK: Prepare data-set from raw text
    DATA-SET-FORMAT: CSV
    INPUT: Raw lines from dataset
    OUTPUT: CSV containing features extracted from dataset
"""


def dataset_preparation(dump_filename, dataset_filename):
    # first read the text

    # for each paragraph, calculate sentence length, sentence count, word length, word count
    # avg syllable per word, total syllable, time to read
    # @TODO: Add number of punctuation, text classification, positive words count

    # write each line in a csv format

    data = [[part.strip() for part in line.split('___', 4)] for line in open(dataset_filename).readlines()]

    with open(dump_filename, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(["id", "text", "avg word length", "word count", "syllable per word", "total syllables", "avg sentence length", "sentence count", "reading time"])
        for line in data:
            arr = calculate_features(line[3].strip())
            writer.writerow([int(line[0]), line[3].strip()] + arr + [float(line[1])])
            print [int(line[0]), line[3].strip()] + arr + [float(line[1])]


if __name__ == '__main__':
    dataset_preparation('../dataset/dataset.csv', '../dataset/reading-dataset.txt')
