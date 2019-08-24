import urllib.request
import zipfile

from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from hephaestus.cdm.automap import Concept
from hephaestus.service import pgsql

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

    def __init__(self, model='cui2vec_gensim.bin'):
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

    """
    Return cocepts and cuis similar to the given one
    
    input: number of similar ones to return: ex: 2
    output: list of [cui (string), concept_id (int), similarity score (float), 
    concept_name (string)]
    Example: [['C0002268', 40342168, 0.9437048435211182, 'Alpha-galactosidase A'], 
    ['C0072596', 4321882, 0.9419581890106201, 'alpha-Dextrin endo-1,6-alpha-glucosidase']]

    """

    def similar_concepts(self, tn):
        # query using gensim cui[0] is the cui and cui[1] is the score
        cuis = self._model.most_similar(self._cui, topn=tn)
        concepts = []
        for cui in cuis:
            # Query the Ohdsi2Cui table  - cui to concept_id mapping
            ohdsi_cui = self._session.query(Ohdsi2Cui).filter_by(cui=cui[0]).one()
            _c = self._session.query(Concept).filter_by(concept_id=ohdsi_cui.concept_id).one()
            concept = [cui[0], ohdsi_cui.concept_id, cui[1], _c.concept_name]
            concepts.append(concept)
        return concepts

    def cuis_to_concepts(self, cuis):
        concepts = []
        results = self._session.query(Ohdsi2Cui.concept_id).filter(Ohdsi2Cui.cui.in_(cuis)).all()
        for result in results:
            concepts.append(result.concept_id)
        return concepts

    def similar_concepts_with_neg(self, neg_cui, tn):
        # query using gensim cui[0] is the cui and cui[1] is the score
        cuis = self._model.most_similar(positive=self._cui, negative=neg_cui, topn=tn)
        concepts = []
        for cui in cuis:
            # Query the Ohdsi2Cui table  - cui to concept_id mapping
            ohdsi_cui = self._session.query(Ohdsi2Cui).filter_by(cui=cui[0]).one()
            _c = self._session.query(Concept).filter_by(concept_id=ohdsi_cui.concept_id).one()
            concept = [cui[0], ohdsi_cui.concept_id, cui[1], _c.concept_name]
            concepts.append(concept)
        return concepts

    # Find the top-N most similar concepts, using the multiplicative combination objective,
    def cosmul_similar_concepts(self, tn):
        return self._model.most_similar_cosmul(self._cui, topn=tn)

    def cosmul_similar_concepts_with_neg(self, neg_cui, tn):
        return self._model.most_similar_cosmul(positive=self._cui, negative=neg_cui, topn=tn)

    def outlier(self, cuis):
        return self._model.doesnt_match(cuis)

    # Compute cosine distances from given concept or vector to all concepts.
    def distances(self, cuis):
        return self._model.distances(self._cui, cuis)

    # Compute cosine similarities
    def combinations(self, cui1, cui2):
        return self._model.cosine_similarities(self._model[self._cui],
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
        url = 'https://ndownloader.figshare.com/files/10959626'
        print('Downloading model...')
        urllib.request.urlretrieve(url, '../model/' + 'cui2vec_pretrained.csv.zip')
        print('Unzipping model...')
        with zipfile.ZipFile('../model/' + 'cui2vec_pretrained.csv.zip', "r") as zip_ref:
            zip_ref.extractall('../model/')
        print('Processing model...')
        with open('../model/' + 'cui2vec_pretrained.csv', 'r') as f:
            with open('../model/' + "cui2vec_g.txt", 'w') as f1:
                next(f)  # skip header line
                count = 0
                for line in f:
                    line = '"'.join(line.split()).replace('"', '')
                    line = ",".join(line.split()).replace(',', ' ')
                    line = line + ' \n'
                    f1.write(line)
                    count += 1
        print('Converting model ...')
        glove2word2vec('../model/' + "cui2vec_g.txt", '../model/' + "cui2vec_w.txt")
        wv_from_text = KeyedVectors.load_word2vec_format('../model/' + 'cui2vec_w.txt', unicode_errors='ignore')
        wv_from_text.save_word2vec_format('../model/' + 'cui2vec_gensim.bin', binary=True)
        print('Model processing completed ..')


if __name__ == '__main__':
    Cui.init_model()
