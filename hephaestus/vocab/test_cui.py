from unittest import TestCase

from hephaestus.vocab.cui import Cui


class TestCui(TestCase):
    def setUp(self):
        self._cui = Cui('cui2vec_gensim.bin')
        self._cui.cui = 'C0000052'

    def test_similar_concepts(self):
        self.assertIn(['C0002268', 40342168, 0.9437048435211182, 'Alpha-galactosidase A'],
                      self._cui.similar_concepts(2), "Similar concepts failed."
                      )

    def test_outlier(self):
        cuis = ['C0002268', 'C0000052', 'C0000075']
        cui_outlier = self._cui.outlier(cuis)
        self.assertEqual(cui_outlier, 'C0002268', "Outlier not found")

    def test_distances(self):
        cuis = ['C0002268', 'C0000052']
        cui_distances = self._cui.distances(cuis)
        self.assertLess(cui_distances[1], 1)

    def test_combinations(self):
        cui_distances = self._cui.combinations('C0031951', 'C0887117')
        self.assertEqual(len(cui_distances), 3)

    def test_closer_to(self):
        concepts = self._cui.closer_to('C0031951', 'C0887117')
        self.assertGreater(len(concepts), 0)
