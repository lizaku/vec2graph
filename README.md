# vec2graph
Mini-library for producing graph visualizations from embedding models

Code is available at https://github.com/lizaku/vec2graph

# Usage

`pip install vec2graph`

`from vec2graph import visualize`

`visualize(OUTPUT_DIR, MODEL, WORD)`

OUTPUT_DIR is the directory to store your visualizations, MODEL is a word embedding model 
loaded with Gensim, WORD is your query word

For example:

`model = gensim.models.KeyedVectors.load_word2vec_format('googlenews300.bin', binary=True)`

`visualize('tmp/graphs', model, 'apple')`