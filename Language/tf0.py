import math
import nltk 
import os
import sys


def main():
    """Calculate top term frequencies for a corpus of documents."""

    if len(sys.argv) != 2:
        sys.exit("Usage: python tfidf.py corpus")
    print("Loading data...")
    corpus = load_data(sys.argv[1])

    # Get all words in corpus
    print("Extracting words from corpus...")
    words = set()
    for filename in corpus:
        words.update(corpus[filename])

    # Calcuşate TF-IDFs
    print("Calculting term frequencies...")
    tfidfs = dict()
    for filename in corpus:
        tfidfs[filename] = []
        for word in corpus[filename]:
            tf = corpus[filename] [word]
            tfidfs[filename].append((word, tf))

    # Sort and get top 5 term frequencies for each file
    print("Computing top terms...")
    for filename in corpus:
        tfidfs[filename].sort(key=lambda tfidf[1], reverse=True)
        tfidfs[filename] = tfidfs[filename] [:5]