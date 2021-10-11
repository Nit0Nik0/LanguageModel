from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict
first_sentence = reuters.sents()[0]
print(first_sentence)


model = defaultdict(lambda: defaultdict(lambda: 0))
bi = bigrams(first_sentence, pad_left=True, pad_right=True)

for w1, w2, w3 in trigrams(first_sentence, pad_right=True, pad_left=True):
    model[(w1, w2)][w3] += 1
    print(f"{w1} {w2} {w3}")

print(bi)

# w1        w2
#       w1
#[(None, 'ASIAN'), ('ASIAN', 'EXPORTERS'), ('EXPORTERS', 'FEAR'), ('FEAR', 'DAMAGE'), ('DAMAGE', 'FROM'), ('FROM', 'U'), ('U', '.'), ('.', 'S'), ('S', '.-'), ('.-', 'JAPAN'), ('JAPAN', 'RIFT'), ('RIFT', 'Mounting'), ('Mounting', 'trade'), ('trade', 'friction'), ('friction', 'between'), ('between', 'the'), ('the', 'U'), ('U', '.'), ('.', 'S'), ('S', '.'), ('.', 'And'), ('And', 'Japan'), ('Japan', 'has'), ('has', 'raised'), ('raised', 'fears'), ('fears', 'among'), ('among', 'many'), ('many', 'of'), ('of', 'Asia'), ('Asia', "'"), ("'", 's'), ('s', 'exporting'), ('exporting', 'nations'), ('nations', 'that'), ('that', 'the'), ('the', 'row'), ('row', 'could'), ('could', 'inflict'), ('inflict', 'far'), ('far', '-'), ('-', 'reaching'), ('reaching', 'economic'), ('economic', 'damage'), ('damage', ','), (',', 'businessmen'), ('businessmen', 'and'), ('and', 'officials'), ('officials', 'said'), ('said', '.'), ('.', None)]

# w1    w2      w3
#[(None, None, 'ASIAN'), (None, 'ASIAN', 'EXPORTERS'), ('ASIAN', 'EXPORTERS', 'FEAR'), ('EXPORTERS', 'FEAR', 'DAMAGE'), ('FEAR', 'DAMAGE', 'FROM'), ('DAMAGE', 'FROM', 'U'), ('FROM', 'U', '.'), ('U', '.', 'S'), ('.', 'S', '.-'), ('S', '.-', 'JAPAN'), ('.-', 'JAPAN', 'RIFT'), ('JAPAN', 'RIFT', 'Mounting'), ('RIFT', 'Mounting', 'trade'), ('Mounting', 'trade', 'friction'), ('trade', 'friction', 'between'), ('friction', 'between', 'the'), ('between', 'the', 'U'), ('the', 'U', '.'), ('U', '.', 'S'), ('.', 'S', '.'), ('S', '.', 'And'), ('.', 'And', 'Japan'), ('And', 'Japan', 'has'), ('Japan', 'has', 'raised'), ('has', 'raised', 'fears'), ('raised', 'fears', 'among'), ('fears', 'among', 'many'), ('among', 'many', 'of'), ('many', 'of', 'Asia'), ('of', 'Asia', "'"), ('Asia', "'", 's'), ("'", 's', 'exporting'), ('s', 'exporting', 'nations'), ('exporting', 'nations', 'that'), ('nations', 'that', 'the'), ('that', 'the', 'row'), ('the', 'row', 'could'), ('row', 'could', 'inflict'), ('could', 'inflict', 'far'), ('inflict', 'far', '-'), ('far', '-', 'reaching'), ('-', 'reaching', 'economic'), ('reaching', 'economic', 'damage'), ('economic', 'damage', ','), ('damage', ',', 'businessmen'), (',', 'businessmen', 'and'), ('businessmen', 'and', 'officials'), ('and', 'officials', 'said'), ('officials', 'said', '.'), ('said', '.', None), ('.', None, None)]

#
