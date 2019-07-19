#!/usr/bin/env python

import argparse
import logging
import os
import webbrowser
from example_usage import load_embeddings
from vec2graph import visualize

logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO
)

parser = argparse.ArgumentParser()

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

args = parser.parse_args()

model = load_embeddings(args.model)

while True:
    text = input('Type your query (WORD, LIM, NR_NEIGHBORS):')
    word, lim, nr_n = text.strip().split()
    if '_' not in word:
        word = word + '_NOUN'
    out = visualize(
        args.output,
        model,
        word,
        topn=int(nr_n),
        threshold=float(lim),
        sep=args.sep
    )
    if out:
        print('Visualization generated!')
        filepath = os.path.join(args.output, word + ".html")
        webbrowser.open('file://' + os.path.realpath(filepath))
    else:
        print('Word not found in the model')
