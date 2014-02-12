import cPickle as pickle
from utils.inverted import InvertedIndex
from vptest import VPTree, jaccard, fingerprint
from flask import Flask, request

app = Flask(__name__)
app.debug = True

########## LOAD DATA STRUCTURES ##########

inverted = pickle.load(open("../data/org-inverted.pk", "rb" ))
searchtree = pickle.load(open("../data/org-vptree.pk", "rb" ))

########## ROUTES ##########

@app.route("/")
def index():
    qs = str(request.args.get('qs'))
    return str(inverted.search(qs))
    #return str(searchtree.search(fingerprint(qs), 0.25))

########## MAIN ##########

if __name__ == "__main__":
    app.run()