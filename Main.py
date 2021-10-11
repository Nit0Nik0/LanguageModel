# Matthew Poindexter
from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict

# Create a placeholder for model
model = defaultdict(lambda: defaultdict(lambda: 0))

# Count frequency of co-occurance
for sentence in reuters.sents():
    #rueters.sents() returns
    for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
        model[w1][w2]+=1;

# Let's transform the counts to probabilities
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w in model[w1_w2]:
        model[w1_w2][w] /= total_count

# predict the next word
print(dict(model["the"]))