from sqlalchemy.ext.automap import automap_base

from hephaestus.service import pgsql
from hephaestus import settings as C

Base = automap_base()
engine = pgsql.get_schema_engine(C.CDM_USER_VOCAB)
# reflect the tables
Base.prepare(engine, reflect=True)

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
