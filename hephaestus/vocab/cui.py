import urllib.request
import zipfile

import pkg_resources
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from hephaestus.cdm.automap import Concept
from hephaestus.service import pgsql
from hephaestus.settings import LocalSettings as C

Base = declarative_base()

"""
This is a class used by sqlalchemy to query the table
"""


class Ohdsi2Cui(Base):
    __tablename__ = 'ohdsi_to_cui'

    cui = Column(String, primary_key=True)
    concept_id = Column(Integer)
    vocabulary_id = Column(String)


class ConceptSetItem(Base):
    __tablename__ = 'concept_set_item'

    concept_set_item_id = Column(Integer, primary_key=True)
    concept_set_id = Column(Integer)
    concept_id = Column(Integer)
    is_excluded = Column(Integer)
    include_descendants = Column(Integer)
    include_mapped = Column(Integer)

    def __init__(self, concept_set_id):
        self.concept_set_id = concept_set_id
        self.is_excluded = 0
        self.include_descendants = 0
        self.include_mapped = 0


"""
Class for sqlalchemy query
"""
Session = sessionmaker(bind=pgsql.get_schema_engine(C.CDM_USER_VOCAB))


class Cui(object):

    def __init__(self, model='cui2vec_gensim.bin'):
        self._respath = pkg_resources.resource_filename('hephaestus', 'resources') + '/'
        __model = self._respath + model
        self._model = KeyedVectors.load_word2vec_format(__model, unicode_errors='ignore', binary=True)
        self._cui = []
        self._concept_id = []
        self._anchors = []
        self._vocab = []
        self._concept = []
        self._engine = pgsql.get_schema_engine(C.CDM_USER_VOCAB)
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

    @property
    def anchors(self):
        return self._anchors

    # setters after getters

    @cui.setter
    def cui(self, cui):
        self._cui = cui
        # ohdsi_cuis = self._session.query(Ohdsi2Cui).filter_by(cui=cui).all()
        ohdsi_cuis = self._session.query(Ohdsi2Cui).filter(Ohdsi2Cui.cui.in_(cui)).all()
        for ohdsi_cui in ohdsi_cuis:
            self._concept_id.append(ohdsi_cui.concept_id)
            self._vocab.append(ohdsi_cui.vocabulary_id)
            _c = self._session.query(Concept).filter_by(concept_id=ohdsi_cui.concept_id).one()
            self._concept.append(_c.concept_name)

    @concept_id.setter
    def concept_id(self, concept_id):
        self._concept_id = concept_id
        # ohdsi_cuis = self._session.query(Ohdsi2Cui).filter_by(concept_id=concept_id).all()
        ohdsi_cuis = self._session.query(Ohdsi2Cui).filter(Ohdsi2Cui.concept_id.in_(concept_id)).all()
        for ohdsi_cui in ohdsi_cuis:
            self._cui.append(ohdsi_cui.cui.strip())  # Removes trailing spaces
            self._vocab.append(ohdsi_cui.vocabulary_id)
            _c = self._session.query(Concept).filter_by(concept_id=ohdsi_cui.concept_id).one()
            self._concept.append(_c.concept_name)

    @vocab.setter
    def vocab(self, vocab):
        self._vocab = vocab

    @concept.setter
    def concept(self, concept):
        self._concept = concept

    """
    Return cocepts and cuis similar to the given one
    
    input: 
    tn - number of similar ones to return: default: 2
    cutoff - cutoff value for similarity concept to be included. default=0 (all)
    output: list of [cui (string), concept_id (int), similarity score (float), 
    concept_name (string)]
    Example: [['C0002268', 40342168, 0.9437048435211182, 'Alpha-galactosidase A'], 
    ['C0072596', 4321882, 0.9419581890106201, 'alpha-Dextrin endo-1,6-alpha-glucosidase']]

    """

    def similar_concepts(self, tn=3, cutoff=0, neg_cui=None, only_id=False):
        # query using gensim cui[0] is the cui and cui[1] is the score
        concepts = []
        cuis = []
        concept_ids = []

        for _cui in self.cui:
            if neg_cui is None:
                cuis.append(self._model.most_similar(_cui, topn=tn))
            else:
                cuis.append(self._model.most_similar(positive=_cui, negative=neg_cui, topn=tn))
        for _cuis in cuis:  # _cuis is a list of most similar for each
            for cui in _cuis:
                # Query the Ohdsi2Cui table  - cui to concept_id mapping
                try:
                    ohdsi_cui = self._session.query(Ohdsi2Cui).filter_by(cui=cui[0].strip()).one()
                    _c = self._session.query(Concept).filter_by(concept_id=ohdsi_cui.concept_id).one()
                    concept = [cui[0].strip(), ohdsi_cui.concept_id, cui[1], _c.concept_name]
                    if cui[1] > cutoff:
                        concepts.append(concept)
                except:
                    pass

        if only_id:
            for c in concepts:
                concept_ids.append(c[1])
            for d in self.concept_id:
                concept_ids.append(d)
            return concept_ids
        else:
            return concepts

    def cuis_to_concepts(self, cuis):
        concepts = []
        results = self._session.query(Ohdsi2Cui.concept_id).filter(Ohdsi2Cui.cui.in_(cuis)).all()
        for result in results:
            concepts.append(result.concept_id)
        return concepts

    def concepts_to_cuis(self, concepts):
        cuis = []
        results = self._session.query(Ohdsi2Cui.cui).filter(Ohdsi2Cui.concept_id.in_(concepts)).all()
        for result in results:
            cuis.append(result.cui.strip())
        return cuis

    # Find the top-N most similar concepts, using the multiplicative combination objective,
    def cosmul_similar_concepts(self, tn):
        return self._model.most_similar_cosmul(self._cui[0], topn=tn)

    def cosmul_similar_concepts_with_neg(self, neg_cui, tn):
        return self._model.most_similar_cosmul(positive=self._cui[0], negative=neg_cui, topn=tn)

    def outlier(self, cuis):
        return self._model.doesnt_match(cuis)

    # Compute cosine distances from given concept or vector to all concepts.
    def distances(self, cuis):
        return self._model.distances(self._cui[0], cuis)

    # Compute cosine similarities
    def combinations(self, cui1, cui2):
        return self._model.cosine_similarities(self._model[self._cui[0]],
                                               vectors_all=(
                                                   self._model[cui1],
                                                   self._model[cui2],
                                                   self._model[cui1] + self._model[cui2]
                                               ))

    # Get the words closer to cui1 than cui2
    def closer_to(self, cui1, cui2):
        return self._model.words_closer_than(cui1, cui2)

    """
    static function that downloads and converts the cui2vec model to gensim binary format
    
    """

    @staticmethod
    def init_model():
        _respath = pkg_resources.resource_filename('hephaestus', 'resources') + '/'
        url = 'https://ndownloader.figshare.com/files/10959626'
        print('Downloading model...')
        urllib.request.urlretrieve(url, _respath + 'cui2vec_pretrained.csv.zip')
        print('Unzipping model...')
        with zipfile.ZipFile(_respath + 'cui2vec_pretrained.csv.zip', "r") as zip_ref:
            zip_ref.extractall(_respath)
        print('Processing model...')
        with open(_respath + 'cui2vec_pretrained.csv', 'r') as f:
            with open(_respath + "cui2vec_g.txt", 'w') as f1:
                next(f)  # skip header line
                count = 0
                for line in f:
                    line = '"'.join(line.split()).replace('"', '')
                    line = ",".join(line.split()).replace(',', ' ')
                    line = line + ' \n'
                    f1.write(line)
                    count += 1
        print('Converting model ...')
        glove2word2vec(_respath + "cui2vec_g.txt", _respath + "cui2vec_w.txt")
        wv_from_text = KeyedVectors.load_word2vec_format(_respath + 'cui2vec_w.txt', unicode_errors='ignore')
        wv_from_text.save_word2vec_format(_respath + 'cui2vec_gensim.bin', binary=True)
        print('Model processing completed ..')

    """
    Writes anchors to concept_list_item if not present already
    
    input: ohdsi schema, concept_set_id
    """

    def write_to_ohdsi(self, schema, concept_set_id):
        WriteSession = sessionmaker(bind=pgsql.get_schema_engine(schema))
        write_session = WriteSession()
        items = []
        items_array = write_session.query(ConceptSetItem.concept_id).filter_by(concept_set_id=concept_set_id).all()
        for item in items_array:
            items.append(item[0])
        anchors = self.anchors
        for anchor in anchors:
            if anchor not in items:
                c = ConceptSetItem(concept_set_id)
                c.concept_id = anchor
                write_session.add(c)
        write_session.commit()

    def read_from_ohdsi(self, schema, concept_set_id):
        WriteSession = sessionmaker(bind=pgsql.get_schema_engine(schema))
        write_session = WriteSession()
        items = []
        items_array = write_session.query(ConceptSetItem.concept_id).filter_by(concept_set_id=concept_set_id).all()
        for item in items_array:
            items.append(item[0])
        self.concept_id = items

    def find_anchors(self, topn=20):
        self._anchors = self.similar_concepts(topn, only_id=True)
        for concept in self._concept_id:
            self._anchors.append(concept)
        self._anchors = list(dict.fromkeys(self._anchors))  # Remove duplicates
        return self._anchors

if __name__ == '__main__':
    Cui.init_model()
