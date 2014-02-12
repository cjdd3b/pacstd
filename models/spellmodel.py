import re, collections

class SpellingModel(object):
    def __init__(self):
        self.model = collections.defaultdict(lambda: 1) # And-one smoothing

    def train(self, features):
        '''
        Basically counts words.
        '''
        for f in features:
            self.model[f] += 1
        return


    #P(c) = The number of times each variant appears in either the unstandardized or standardized field
    #P(w|c) = 1 if there is a standardized name match; metric distance to closest match otherwise? Test that.

    # Edit distance isn't going to work here because of massive variations in company spelling. "AT&T vs. TECHNICIAN/ATT"
    # Need to use something like a metric tree instead to find candidate matches. Further, need something like
    # a VP-tree to do continuous value search with Jaccard.

    # Use a substring or ngram error model? What's the probability that they mean "Covington Burling" if the input
    # string contains "Covington" and so forth.

    # Aggregate four models: Straight-up match + Norvig spellcheck based on prob. models + ngram/substr probs + acronym model
    # One at a time. If not X certain after all those, hit up Yahoo.