from gensim.models import KeyedVectors
from sqlalchemy.orm import sessionmaker
from hephaestus.service import pgsql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from hephaestus.cdm.automap import Concept

Base = declarative_base()

"""
This is a class used by sqlalchemy to query the table
"""


class Ohdsi2Cui(Base):
    __tablename__ = 'ohdsi_to_cui'

    cui = Column(String, primary_key=True)
    concept_id = Column(Integer)
    vocabulary_id = Column(String)


"""
Class for sqlalchemy query
"""
Session = sessionmaker(bind=pgsql.get_reader())


class Cui(object):

    def __init__(self, model):
        __model = '../model/' + model
        self._model = KeyedVectors.load_word2vec_format(__model, unicode_errors='ignore', binary=True)
        self._cui = ""
        self._concept_id = 0
        self._vocab = ""
        self._concept = ""
        self._engine = pgsql.get_reader()
        self._session = Session()

    # Getters before setters
    @property
    def cui(self):
        return self._cui

    @property
    def concept_id(self):
        return self._concept_id

    @property
    def vocab(self):
        return self._vocab

    @property
    def concept(self):
        return self._concept

    # setters after getters

    @cui.setter
    def cui(self, cui):
        self._cui = cui
        ohdsi_cui = self._session.query(Ohdsi2Cui).filter_by(cui=cui).one()
        self._concept_id = ohdsi_cui.concept_id
        self.vocab = ohdsi_cui.vocabulary_id
        _c = self._session.query(Concept).filter_by(concept_id=self._concept_id).one()
        self._concept = _c.concept_name

    @concept_id.setter
    def concept_id(self, concept_id):
        self._concept_id = concept_id
        ohdsi_cui = self._session.query(Ohdsi2Cui).filter_by(concept_id=concept_id).one()
        self._cui = ohdsi_cui.cui
        self.vocab = ohdsi_cui.vocabulary_id
        _c = self._session.query(Concept).filter_by(concept_id=concept_id).one()
        self._concept = _c.concept_name

    @vocab.setter
    def vocab(self, vocab):
        self._vocab = vocab

    @concept.setter
    def concept(self, concept):
        self._concept = concept


if __name__ == '__main__':
    _cui = Cui('cui2vec_gensim.bin')
    _cui.cui = 'C1952632'
    print(_cui.concept_id)
    print(_cui.concept)
