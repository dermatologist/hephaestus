from sqlalchemy import Column, String, Integer, Date, DateTime
from sqlalchemy.ext.automap import automap_base

Base = automap_base()


class CDMMetadata(Base):
    __tablename__ = 'metadata'
    # override schema elements like Columns
    metadata_concept_id = Column(Integer, primary_key=True)
    metadata_type_concept_id = Column(Integer)
    name = Column(String)
    value_as_string = Column(String)
    value_as_concept_id = Column(Integer)
    metadata_date = Column(Date)
    metadata_datetime = Column(DateTime)

