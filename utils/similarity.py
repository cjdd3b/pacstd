import re, string

PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))

def shingle(word, n):
    '''
    More on shingling here: http://blog.mafr.de/2011/01/06/near-duplicate-detection/
    '''
    return set([word[i:i + n] for i in range(len(word) - n + 1)])

def jaccard(a, b):
    '''
    Jaccard similarity between two sets.

    Explanation here: http://en.wikipedia.org/wiki/Jaccard_index
    '''
    x = shingle(a, 3)
    y = shingle(b, 3)
    return 1.0 - (float(len(x & y) + 1) / float(len(x | y) + 1)) # Smoothing

def fingerprint(word, n=7):
    return '%s' % ''.join(sorted(set(
        list(PUNCTUATION.sub('', word.strip()).lower())[:n])
    ))
