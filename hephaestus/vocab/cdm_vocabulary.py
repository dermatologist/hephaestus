from sqlalchemy.orm import sessionmaker

from hephaestus.cdm.automap import Concept
from hephaestus.service import pgsql

Session = sessionmaker(bind=pgsql.get_reader())


class CdmVocabulary(Concept):
    def __init__(self):
        self._concept_id = 0
        self._concept_name = ''
        self._domain_id = ''
        self._vocabulary_id = ''
        self._concept_class_id = ''
        self._concept_code = ''
        self._session = Session()

    @property
    def concept_id(self):
        return self._concept_id

    @property
    def concept_code(self):
        return self._concept_code

    @property
    def concept_name(self):
        return self._concept_name

    @property
    def vocabulary_id(self):
        return self._vocabulary_id

    @property
    def domain_id(self):
        return self._domain_id

    @concept_id.setter
    def concept_id(self, concept_id):
        self._concept_id = concept_id
        _concept = self._session.query(Concept).filter_by(concept_id=concept_id).one()
        self._concept_name = _concept.concept_name
        self._domain_id = _concept.domain_id
        self._vocabulary_id = _concept.vocabulary_id
        self._concept_class_id = _concept.concept_class_id
        self._concept_code = _concept.concept_code

    def set_concept(self, vocabulary_id, concept_code):
        self._concept_code = concept_code
        self._vocabulary_id = vocabulary_id
        _concept = self._session.query(Concept).filter_by(concept_code=concept_code) \
            .filter_by(vocabulary_id=vocabulary_id).one()
        self._concept_name = _concept.concept_name
        self._domain_id = _concept.domain_id
        self._concept_id = _concept.concept_id
        self._concept_class_id = _concept.concept_class_id
        self._concept_code = _concept.concept_code
