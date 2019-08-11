
## Using on cedar

* pgsql.sh
* ssh -N -L 5432:cedar-pgsql-vm:5432 username@int.cedar.computecanada.ca


## Creating CDM

* psql -h cedar-pgsql-vm username_db < OMOP\ CDM\ postgresql\ ddl.txt
* psql -h cedar-pgsql-vm username_db < OMOP\ CDM\ postgresql\ constraints.txt
* psql -h cedar-pgsql-vm username_db < OMOP\ CDM\ postgresql\ indexes.txt


```
\COPY DRUG_STRENGTH FROM '/home/username/scratch/OHDSI/DRUG_STRENGTH.csv' WITH DELIMITER E'\t' CSV HEADER QUOTE E'\b' ;

\COPY CONCEPT FROM '/home/username/scratch/OHDSI/CONCEPT.csv' WITH DELIMITER E'\t' CSV HEADER QUOTE E'\b' ;

\COPY CONCEPT_RELATIONSHIP FROM '/home/username/scratch/OHDSI/CONCEPT_RELATIONSHIP.csv' WITH DELIMITER E'\t' CSV HEADER QUOTE E'\b' ;

\COPY CONCEPT_ANCESTOR FROM '/home/username/scratch/OHDSI/CONCEPT_ANCESTOR.csv' WITH DELIMITER E'\t' CSV HEADER QUOTE E'\b' ;

\COPY CONCEPT_SYNONYM FROM '/home/username/scratch/OHDSI/CONCEPT_SYNONYM.csv' WITH DELIMITER E'\t' CSV HEADER QUOTE E'\b' ;

\COPY VOCABULARY FROM '/home/username/scratch/OHDSI/VOCABULARY.csv' WITH DELIMITER E'\t' CSV HEADER QUOTE E'\b' NULL AS 'null';

\COPY RELATIONSHIP FROM '/home/username/scratch/OHDSI/RELATIONSHIP.csv' WITH DELIMITER E'\t' CSV HEADER QUOTE E'\b' ;

\COPY CONCEPT_CLASS FROM '/home/username/scratch/OHDSI/CONCEPT_CLASS.csv' WITH DELIMITER E'\t' CSV HEADER QUOTE E'\b' ;

\COPY DOMAIN FROM '/home/username/scratch/OHDSI/DOMAIN.csv' WITH DELIMITER E'\t' CSV HEADER QUOTE E'\b' ;

```


## Primary keys are required by sqlalchemy for automaping

```sql
ALTER TABLE attribute_definition ADD PRIMARY KEY (attribute_definition_id);
ALTER TABLE care_site ADD PRIMARY KEY (care_site_id);
ALTER TABLE cdm_source ADD PRIMARY KEY (cdm_source_id);
ALTER TABLE cohort ADD PRIMARY KEY (cohort_id);
ALTER TABLE cohort_attribute ADD PRIMARY KEY (cohort_attribute_id);
ALTER TABLE cohort_definition ADD PRIMARY KEY (cohort_definition_id);
ALTER TABLE concept ADD PRIMARY KEY (concept_id);
ALTER TABLE concept_ancestor ADD PRIMARY KEY (concept_ancestor_id);
ALTER TABLE concept_class ADD PRIMARY KEY (concept_class_id);
ALTER TABLE concept_relationship ADD PRIMARY KEY (concept_relationship_id);
ALTER TABLE concept_synonym ADD PRIMARY KEY (concept_synonym_id);
ALTER TABLE condition_era ADD PRIMARY KEY (condition_era_id);
ALTER TABLE condition_occurrence ADD PRIMARY KEY (condition_occurrence_id);
ALTER TABLE cost ADD PRIMARY KEY (cost_id);
ALTER TABLE death ADD PRIMARY KEY (death_id);
ALTER TABLE device_exposure ADD PRIMARY KEY (device_exposure_id);
ALTER TABLE domain ADD PRIMARY KEY (domain_id);
ALTER TABLE dose_era ADD PRIMARY KEY (dose_era_id);
ALTER TABLE drug_era ADD PRIMARY KEY (drug_era_id);
ALTER TABLE drug_exposure ADD PRIMARY KEY (drug_exposure_id);
ALTER TABLE drug_strength ADD PRIMARY KEY (drug_strength_id);
ALTER TABLE fact_relationship ADD PRIMARY KEY (fact_relationship_id);
ALTER TABLE location ADD PRIMARY KEY (location_id);
ALTER TABLE measurement ADD PRIMARY KEY (measurement_id);
ALTER TABLE metadata ADD PRIMARY KEY (metadata_id);
ALTER TABLE note ADD PRIMARY KEY (note_id);
ALTER TABLE note_nlp ADD PRIMARY KEY (note_nlp_id);
ALTER TABLE observation ADD PRIMARY KEY (observation_id);
ALTER TABLE observation_period ADD PRIMARY KEY (observation_period_id);
ALTER TABLE payer_plan_period ADD PRIMARY KEY (payer_plan_period_id);
ALTER TABLE person ADD PRIMARY KEY (person_id);
ALTER TABLE procedure_occurrence ADD PRIMARY KEY (procedure_occurrence_id);
ALTER TABLE provider ADD PRIMARY KEY (provider_id);
ALTER TABLE relationship ADD PRIMARY KEY (relationship_id);
ALTER TABLE source_to_concept_map ADD PRIMARY KEY (source_to_concept_map_id);
ALTER TABLE specimen ADD PRIMARY KEY (specimen_id);
ALTER TABLE visit_detail ADD PRIMARY KEY (visit_detail_id);
ALTER TABLE visit_occurrence ADD PRIMARY KEY (visit_occurrence_id);
ALTER TABLE vocabulary ADD PRIMARY KEY (vocabulary_id);

```