from collections import namedtuple

""" Named tuple implementation to hold bigram probabilities read from file """
BigramTuple = namedtuple('BigramCount', ['count', 'mle', 'laplace_bigram', 'interpolated', 'discounted'])


class DefaultDictionary(dict):
    """ Dictionary extension that returns 0 for missing keys instead of None """
    def __missing__(self, key):
        return 0


class ModelFromDicts:
    """ Constructs a model from dictionaries that were built from bigram and unigram files. Assumes that the
    bigram dictionary map tuples of bigrams to BigramTuple objects. """
    def __init__(self, unigrams, bigrams, number_tokens):
        self.number_tokens = number_tokens
        self.unigram_counts = unigrams
        self.bigram_counts = bigrams

    def vocab_size(self):
        return len(self.unigram_counts)

    def bigram_count(self, x, y):
        val = self.bigram_counts[(x, y)]
        if val == 0:
            return 0
        return val.count

    def unigram_count(self, x):
        return self.unigram_counts[x]

    def num_tokens(self):
        return self.number_tokens


class Model:
    """ Holds bigram and unigram data for a model """
    def __init__(self, sentences, tokens):
        self.sentences = sentences
        self.tokens = tokens
        self.bigram_counts = DefaultDictionary()
        self.unigram_counts = DefaultDictionary()
        self.bfile_prob = None  # bigram probabilities from file
        self.ufile_prob = None  # unigram probabilities from file
        self.build_models()

    def build_models(self):
        for i in range(len(self.tokens) - 1):
            x = self.tokens[i]
            y = self.tokens[i + 1]
            self.unigram_counts[x] += 1
            self.bigram_counts[(x, y)] += 1
        self.unigram_counts[self.tokens[len(self.tokens) - 1]] += 1

    def vocab_size(self):
        return len(self.unigram_counts)

    def bigram_count(self, x, y):
        return self.bigram_counts[(x, y)]

    def unigram_count(self, x):
        return self.unigram_counts[x]

    def num_tokens(self):
        return len(self.tokens)
