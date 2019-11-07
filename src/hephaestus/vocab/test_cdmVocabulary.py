from unittest import TestCase

from sqlalchemy.orm import sessionmaker

from .. import settings as C
from ..service import pgsql
from ..vocab.cdm_vocabulary import CdmVocabulary

Session = sessionmaker(bind=pgsql.get_schema_engine(C.CDM_USER_VOCAB))

class TestCdmVocabulary(TestCase):
    def setUp(self):
        self.cdmv = CdmVocabulary()

    def test_concept_id(self):
        self.cdmv.concept_id = 198185
        self.assertEqual(self.cdmv.concept_code, '90688005')

    def test_set_concept(self):
        self.cdmv.set_concept('90688005', 'SNOMED')
        self.assertEqual(self.cdmv.concept_id, 198185)

    def test_get_concept_id(self):
        session = Session()
        concept_id = CdmVocabulary.get_concept_id('90688005', session)
        print(concept_id)
