from sqlalchemy import Column, String, Integer, Date, DateTime
from sqlalchemy.ext.automap import automap_base

Base = automap_base()


class Concept_synonym(Base):
    __tablename__ = 'concept_synonym'
    concept_id = Column(Integer)
    concept_synonym_name = Column(String)
    language_concept_id = Column(Integer)
