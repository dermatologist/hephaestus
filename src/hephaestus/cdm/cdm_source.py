from sqlalchemy import Column, String, Integer, Date, DateTime
from sqlalchemy.ext.automap import automap_base

Base = automap_base()


class Cdm_source(Base):
    __tablename__ = "cdm_source"
    cdm_source_name = Column(String)
    cdm_source_abbreviation = Column(String)
    cdm_holder = Column(String)
    source_description = Column(String)
    source_documentation_reference = Column(String)
    cdm_etl_reference = Column(String)
    source_release_date = Column(Date)
    cdm_release_date = Column(Date)
    cdm_version = Column(String)
    vocabulary_version = Column(String)
