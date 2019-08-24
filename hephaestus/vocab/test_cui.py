from unittest import TestCase

from hephaestus.vocab.cui import Cui


class TestCui(TestCase):
    def setUp(self):
        self._cui = Cui('cui2vec_gensim.bin')
        self._cui.cui = 'C1579029'

    def test_similar_concepts(self):
        print(self._cui.similar_concepts(5))
        self.assertGreater(len(self._cui.similar_concepts(5)), 0)

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

    def test_cuis_to_concepts(self):
        cuis = ['C0002268', 'C0000052']
        concepts = self._cui.cuis_to_concepts(cuis)
        self.assertIn(40614810, concepts)
