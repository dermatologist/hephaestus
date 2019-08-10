from sqlalchemy import Column, String, Integer, Date, DateTime
from sqlalchemy.ext.automap import automap_base

from hephaestus.service import pgsql

"""
Automap all CDM tables to corresponding class definitions

"""

Base = automap_base()
engine = pgsql.get_reader()
Base.prepare(engine, reflect=True)
# mapped classes are now created with names by default
# matching that of the table name.

# CDMMetadata = Base.classes.metadata
# Cdm_source = Base.classes.cdm_source
Source_to_concept_map = Base.classes.source_to_concept_map
Vocabulary = Base.classes.vocabulary
Concept_ancestor = Base.classes.concept_ancestor
Drug_strength = Base.classes.drug_strength
Concept_class = Base.classes.concept_class
Concept_relationship = Base.classes.concept_relationship
# Concept_synonym = Base.classes.concept_synonym
Relationship = Base.classes.relationship
Death = Base.classes.death
Observation_period = Base.classes.observation_period
Specimen = Base.classes.specimen
Visit_detail = Base.classes.visit_detail
Procedure_occurrence = Base.classes.procedure_occurrence
Drug_exposure = Base.classes.drug_exposure
Condition_occurrence = Base.classes.condition_occurrence
Device_exposure = Base.classes.device_exposure
Measurement = Base.classes.measurement
Note = Base.classes.note
Note_nlp = Base.classes.note_nlp
Provider = Base.classes.provider
Visit_occurrence = Base.classes.visit_occurrence
# Fact_relationship = Base.classes.fact_relationship
Location = Base.classes.location
Care_site = Base.classes.care_site
Observation = Base.classes.observation
Payer_plan_period = Base.classes.payer_plan_period
Drug_era = Base.classes.drug_era
Cohort_definition = Base.classes.cohort_definition
Attribute_definition = Base.classes.attribute_definition
Cohort_attribute = Base.classes.cohort_attribute
Cost = Base.classes.cost
Person = Base.classes.person
Condition_era = Base.classes.condition_era
Concept = Base.classes.concept
Dose_era = Base.classes.dose_era
Cohort = Base.classes.cohort
Domain = Base.classes.domain


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


class Concept_synonym(Base):
    __tablename__ = 'concept_synonym'
    concept_id = Column(Integer)
    concept_synonym_name = Column(String)
    language_concept_id = Column(Integer)


class Fact_relationship(Base):
    domain_concept_id = Column(Integer)
    fact_id_1 = Column(Integer)
    domain_concept_id_2 = Column(Integer)
    fact_id_2 = Column(Integer)
    relationship_concept_id = Column(Integer)

# TODO: To refactor this file
