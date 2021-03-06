from unittest import TestCase

from ..vocab.cui import Cui


class TestCui(TestCase):
    def setUp(self):
        self.cui2vec = Cui('cui2vec_gensim.bin')
        #self.cui2vec.cui = ['C1579029']
        self.cui2vec.concept_id = [198185]

    def test_conversion(self):
        self.cui2vec.cui = ['C1579029']
        self.assertIn(198185, self.cui2vec.concept_id)
        self.cui2vec.concept_id = [198185]
        self.assertIn('C1579029', self.cui2vec.cui)

    def test_similar_concepts(self):
        self.assertGreater(len(self.cui2vec.similar_concepts(5)), 0)

    def test_similar_concept_ids(self):
        x = self.cui2vec.similar_concepts(5, only_id=True)
        self.assertGreater(len(x), 0)

    def test_outlier(self):
        cuis = ['C0002268', 'C0000052', 'C0000075']
        cui_outlier = self.cui2vec.outlier(cuis)
        self.assertEqual(cui_outlier, 'C0002268', "Outlier not found")

    def test_distances(self):
        cuis = ['C0002268', 'C0000052']
        cui_distances = self.cui2vec.distances(cuis)
        self.assertLess(cui_distances[1], 1)

    def test_combinations(self):
        cui_distances = self.cui2vec.combinations('C0031951', 'C0887117')
        self.assertEqual(len(cui_distances), 3)

    def test_closer_to(self):
        concepts = self.cui2vec.closer_to('C0031951', 'C0887117')
        self.assertGreater(len(concepts), 0)

    def test_cuis_to_concepts(self):
        cuis = ['C0002268', 'C0000052']
        concepts = self.cui2vec.cuis_to_concepts(cuis)
        self.assertIn(40614810, concepts)

    def test_concepts_to_cuis(self):
        concepts = [40614810, 198185]
        cuis = self.cui2vec.concepts_to_cuis(concepts)
        self.assertIn('C1579029', cuis)

    def test_anchors(self):
        concepts = [40614810, 198185]
        self.cui2vec.concept_id = concepts
        self.cui2vec.find_anchors(20)
        self.assertIn(44782429, self.cui2vec.anchors)

    def test_write_to_ohdsi(self):
        self.cui2vec.write_to_ohdsi("ohdsi", 2)

    def test_read_from_ohdsi(self):
        self.cui2vec.read_from_ohdsi("ohdsi", 2)

    def test_find_anchors(self):
        self.cui2vec.read_from_ohdsi("ohdsi", 2)
        anchors = self.cui2vec.find_anchors(20)
        self.assertIn(44782429, anchors)
