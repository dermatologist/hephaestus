import pkg_resources
from gensim.models import KeyedVectors

"""
This demonstrates how to use spark
The model should be available to all nodes. (In compute canada all nodes have access to the same file)
In a different environment use S3 bucket or something similar
Ref: https://trivial.io/word2vec-on-databricks-791157831eaa

Loading the model is an expensive operation.
The following pattern makes sure that model is loaded only once.
"""


class CuiSpark(object):
    # This is never serialized
    # ref: https://trivial.io/word2vec-on-databricks-791157831eaa
    cache = {}

    def __init__(self, model='cui2vec_gensim.bin'):
        self._respath = pkg_resources.resource_filename('hephaestus', 'resources') + '/'
        self.fn = self._respath + model

    @property
    def cui2vec(self):
        if self.fn not in CuiSpark.cache:
            CuiSpark.cache[self.fn] = \
                KeyedVectors.load_word2vec_format(self.fn, binary=True)
        return CuiSpark.cache[self.fn]

    """
    Note that the return type is an array.
    If It was cui, use map as documented in test_cuiSpark.py
    """

    def similar_cuis(self, cui):
        try:
            return self.cui2vec.most_similar(cui)
        except:
            return []
