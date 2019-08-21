from unittest import TestCase

from hephaestus.vocab.cui import Cui


class TestCui(TestCase):
    def test_similar_concepts(self):
        _cui = Cui('cui2vec_gensim.bin')
        _cui.cui = 'C0000052'
        self.assertIn(['C0002268', 40342168, 0.9437048435211182, 'Alpha-galactosidase A'],
                      _cui.similar_concepts(2), "Similar concepts failed."
                      )
