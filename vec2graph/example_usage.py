#!/usr/bin/env python

from gensim import models
import logging
import argparse
import zipfile
from vec2graph import visualize
import json


def load_embeddings(embeddings_file):
    # Detect the model format by its extension:
    # Binary word2vec format:
    if embeddings_file.endswith('.bin.gz') or embeddings_file.endswith('.bin'):
        emb_model = models.KeyedVectors.load_word2vec_format(embeddings_file, binary=True,
                                                             unicode_errors='replace')
    # Text word2vec format:
    elif embeddings_file.endswith('.txt.gz') or embeddings_file.endswith('.txt') \
            or embeddings_file.endswith('.vec.gz') or embeddings_file.endswith('.vec'):
        emb_model = models.KeyedVectors.load_word2vec_format(
            embeddings_file, binary=False, unicode_errors='replace')
    # ZIP archive from the NLPL vector repository:
    elif embeddings_file.endswith('.zip'):
        with zipfile.ZipFile(embeddings_file, "r") as archive:
            # Loading and showing the metadata of the model:
            metafile = archive.open('meta.json')
            metadata = json.loads(metafile.read())
            for key in metadata:
                print(key, metadata[key])
            print('============')
            # Loading the model itself:
            stream = archive.open("model.bin")  # or model.txt, if you want to look at the model
            emb_model = models.KeyedVectors.load_word2vec_format(
                stream, binary=True, unicode_errors='replace')
    else:
        # Native Gensim format?
        emb_model = models.KeyedVectors.load(embeddings_file)
        # If you intend to train further: emb_model = models.Word2Vec.load(embeddings_file)

    emb_model.init_sims(replace=True)  # Unit-normalizing the vectors (if they aren't already)
    return emb_model


logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "-w",
    "--word",
    help="word to look for in the model. If omitted, random word is used",
    default="",
)
parser.add_argument(
    "-n",
    "--nbr",
    help="amount of neighbors to show.",
    default=10,
    type=int,
)
parser.add_argument(
    "-e",
    "--edge",
    help="width of an edge (link) between nodes.",
    default=1,
    type=int,
)
parser.add_argument(
    "-d",
    "--depth",
    help="recursion depth to build graphs also of neighbors of target word."
         " Default is 0 (no neighbors)",
    default=0,
    type=int,
)
parser.add_argument(
    "-l",
    "--lim",
    help="limit (threshold) of cosine similarity which should be surpassed by"
         " neighbors to be rendered as connected. Scale is either more "
         "than 0 and less than 1 (as real range for similarities), or"
         " from 1 to 100 as percents. Default is 0 (all edges are preserved)",
    default=0,
    type=float,
)
parser.add_argument(
    "-m",
    "--model",
    help="path to vector model file. If omitted, first model with the extension "
         "bin.gz (as binary) or .vec.gz (as non-binary) in working directory"
         " is loaded",
    default="",
)
parser.add_argument(
    "-o",
    "--output",
    help="path to the output directory where to store visualization files."
         " If omitted, a new directory will be made in the current one, with the name"
         " based on the timestamp",
    default="",
)

parser.add_argument(
    "-s",
    "--sep",
    help="if this parameter is used, the words are split by a separator"
         "(underscore), and only the first part is shown in visualization (E.g. "
         "it is useful when PoS is attached to a word). By now, this "
         "parameter accepts no value",
    action="store_true",
)

parser.add_argument(
    "-js",
    "--javascript",
    help="path to D3.js library, can be 'web' (link to version at the D3.js "
         "site) or 'local' (file in the directory with generated HTML, if not"
         " present, it is downloaded from web). Default is 'web'",
    choices=("web", "local"),
    default="web",
)
args = parser.parse_args()

model = load_embeddings(args.model)

word = args.word

visualize(
    args.output,
    model,
    word,
    depth=args.depth,
    topn=args.nbr,
    threshold=args.lim,
    edge=args.edge,
    sep=args.sep,
    library=args.javascript,
)
