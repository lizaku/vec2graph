# vec2graph
Mini-library for producing graph visualizations from embedding models

Code is available at https://github.com/lizaku/vec2graph

# Usage

`pip install vec2graph`

`from vec2graph import visualize`

`visualize(OUTPUT_DIR, MODEL, WORD, depth=0, topn=10, threshold=0, edge=1, sep=False, library="web")`

### Example

`model = gensim.models.KeyedVectors.load_word2vec_format('googlenews300.bin', binary=True)`

`visualize('tmp/graphs', model, 'apple')`

### Required arguments

- **OUTPUT_DIR** is the directory to store your visualizations
- **MODEL** is a word embedding model loaded with Gensim
- **WORD** is your query (single word or list of the words: `['apple', 'pear']`). If in the model PoS-tag is attached to the word, it shoul be written explicitly: `'apple_NOUN'`

### Optional arguments

- **depth**: *integer, default 0*  
      depth to which the algorithm has to drill down into the relations of semantic neighbours (the higher this number is,    the deeper the recursion, which means that it produces visualizations for the neighbours of the neighbours of the query word). 
- **topn**: *integer, default 10*  
      the number of neighbors to extract for each word
- **threshold**: *float, default 0*  
      the value from which we start drawing edges between nodes. By default the fully connected graph is produced.
- **edge**: *integer, default 1*  
      the width of edges in the graph
- **sep**: *bool, default False*  
      if this parameter is used, token is split by a separator (underscore), and only first part is shown in visualization (E.g. it is useful when PoS is attached to a word - `'apple_NOUN'`).
- **library**: *str, default 'web'*  
      the path to D3.js library, can be 'web' (link to version at the D3.js site) or 'local' (file in the directory with generated HTML, if not present, it is downloaded from web).

