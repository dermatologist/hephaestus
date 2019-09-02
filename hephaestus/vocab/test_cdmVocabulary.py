from unittest import TestCase

from hephaestus.vocab.cdm_vocabulary import CdmVocabulary


class TestCdmVocabulary(TestCase):
    def setUp(self):
        self.cdmv = CdmVocabulary()

    def test_concept_id(self):
        self.cdmv.concept_id = 198185
        self.assertEqual(self.cdmv.concept_code, '90688005')

    def test_set_concept(self):
        self.cdmv.set_concept('90688005', 'SNOMED')
        self.assertEqual(self.cdmv.concept_id, 198185)
