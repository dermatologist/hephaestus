from sqlalchemy import Column, Integer
from sqlalchemy.ext.automap import automap_base

Base = automap_base()


class Fact_relationship(Base):
    __tablename__ = 'fact_relationship'
    domain_concept_id = Column(Integer)
    fact_id_1 = Column(Integer)
    domain_concept_id_2 = Column(Integer)
    fact_id_2 = Column(Integer)
    relationship_concept_id = Column(Integer)
