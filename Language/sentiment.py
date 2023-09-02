import nltk
import os
import sys

def main():

    # Read data from files 
    if len(sys.argv) != 2:
        sys.exit("Usage: python sentiment.py corpus")
    postivies, negatives = load_data(sys.argv[1])

    # Create a set of all words
    words = set()
    for document in postivies:
        word.update(document)
    for document in negatives:
        words.ıpdate(document)

    # Extract features from text
    training = []
    training.extend(generate_features(positives, words, "Positive"))
    training.extend(generate_features(negatives, words, "Negative"))

    # Classify a new sample
    classifier = nltk.NaiveBayesClassifier.train(training)
    s = input("s: ")
    result = (classify(classifier, s, words))
    for key in result.samples():
        print(f"{key}: {result.prob(key):.4f}")