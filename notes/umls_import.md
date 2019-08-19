
* remove line
sed -i '6562211d' MRCONSO.RRF > 2MRCONSO.RRF #try this. removed in original though


* Read a line
sed -n LINE_NUMBERp file.txt
sed -n 6562211p MRCONSO.RRF

set schema 'umls_cui';
\COPY mrconso 'MRCONSO.RRF' with delimiter as '|' null as '';


```

DROP TABLE IF EXISTS umls_cui.mrconso;
CREATE TABLE umls_cui.MRCONSO (
	CUI	char(10) NOT NULL,
	LAT	char(3) NOT NULL,
	TS	char(1) NOT NULL,
	LUI	char(10) NOT NULL,
	STT	varchar(3) NOT NULL,
	SUI	char(10) NOT NULL,
	ISPREF	char(1) NOT NULL,
	AUI	varchar(10) NOT NULL,
	SAUI	varchar(50),
	SCUI	varchar(50),
	SDUI	varchar(50),
	SAB	varchar(20) NOT NULL,
	TTY	varchar(20) NOT NULL,
	CODE text NOT NULL,
	STR	text NOT NULL,
	SRL	varchar(3) NOT NULL,
	SUPPRESS	char(1) NOT NULL,
	CVF	int,
	dummy char(1) default null
);

SELECT count(*) from mrconso;

alter table MRCONSO drop column dummy;

CREATE INDEX X_MRCONSO_CUI ON MRCONSO(CUI)
;

 
ALTER TABLE MRCONSO ADD CONSTRAINT X_MRCONSO_PK PRIMARY KEY (AUI)
;

CREATE INDEX X_MRCONSO_SUI ON MRCONSO(SUI)
;

CREATE INDEX X_MRCONSO_LUI ON MRCONSO(LUI)
;

CREATE INDEX X_MRCONSO_CODE ON MRCONSO(CODE)
;

CREATE INDEX X_MRCONSO_SAB_TTY ON MRCONSO(SAB,TTY)
;

CREATE INDEX X_MRCONSO_SCUI ON MRCONSO(SCUI)
;

CREATE INDEX X_MRCONSO_STR ON MRCONSO(STR)
;


```

# https://github.com/E-Health/OHDSIconceptid2cui
```sql
DROP TABLE IF EXISTS vocabulary.OHDSI_to_CUI;
CREATE TABLE vocabulary.OHDSI_to_CUI AS (
SELECT AAA.* FROM (
SELECT AA.* FROM (
SELECT A.CUI, B.concept_id, B.vocabulary_id FROM umls_cui.MRCONSO as A LEFT JOIN vocabulary.concept as B ON A.CODE=B.concept_code WHERE A.LAT='ENG' AND A.SAB='RXNORM' AND B.vocabulary_id='RxNorm'
) AA GROUP BY AA.CUI, AA.concept_id, AA.vocabulary_id
UNION
SELECT AA.* FROM (
SELECT A.CUI, B.concept_id, B.vocabulary_id FROM umls_cui.MRCONSO as A LEFT JOIN vocabulary.concept as B ON A.CODE=B.concept_code WHERE A.LAT='ENG' AND A.SAB='CPT' AND B.vocabulary_id='CPT4'
) AA GROUP BY AA.CUI, AA.concept_id, AA.vocabulary_id
UNION
SELECT AA.* FROM (
SELECT A.CUI, B.concept_id, B.vocabulary_id FROM umls_cui.MRCONSO as A LEFT JOIN vocabulary.concept as B ON A.CODE=B.concept_code WHERE A.LAT='ENG' AND A.SAB='HCPCS' AND B.vocabulary_id='HCPCS'
) AA GROUP BY AA.CUI, AA.concept_id, AA.vocabulary_id
UNION
SELECT AA.* FROM (
SELECT A.CUI, B.concept_id, B.vocabulary_id FROM umls_cui.MRCONSO as A LEFT JOIN vocabulary.concept as B ON A.CODE=B.concept_code WHERE A.LAT='ENG' AND A.SAB='ICD10CM' AND B.vocabulary_id='ICD10CM'
) AA GROUP BY AA.CUI, AA.concept_id, AA.vocabulary_id
UNION
SELECT AA.* FROM (
SELECT A.CUI, B.concept_id, B.vocabulary_id FROM umls_cui.MRCONSO as A LEFT JOIN vocabulary.concept as B ON A.CODE=B.concept_code WHERE A.LAT='ENG' AND A.SAB='ICD10PCS' AND B.vocabulary_id='ICD10PCS'
) AA GROUP BY AA.CUI, AA.concept_id, AA.vocabulary_id
UNION
SELECT AA.* FROM (
SELECT A.CUI, B.concept_id, B.vocabulary_id FROM umls_cui.MRCONSO as A LEFT JOIN vocabulary.concept as B ON A.CODE=B.concept_code WHERE A.LAT='ENG' AND A.SAB='ICD9CM' AND B.vocabulary_id='ICD9CM'
) AA GROUP BY AA.CUI, AA.concept_id, AA.vocabulary_id
UNION
SELECT AA.* FROM (
SELECT A.CUI, B.concept_id, B.vocabulary_id FROM umls_cui.MRCONSO as A LEFT JOIN vocabulary.concept as B ON A.CODE=B.concept_code WHERE A.LAT='ENG' AND A.SAB='MDR' AND B.vocabulary_id='MedDRA'
) AA GROUP BY AA.CUI, AA.concept_id, AA.vocabulary_id
UNION
SELECT AA.* FROM (
SELECT A.CUI, B.concept_id, B.vocabulary_id FROM umls_cui.MRCONSO as A LEFT JOIN vocabulary.concept as B ON A.CODE=B.concept_code WHERE A.LAT='ENG' AND A.SAB='HCPCS' AND B.vocabulary_id='HCPCS'
) AA GROUP BY AA.CUI, AA.concept_id, AA.vocabulary_id
UNION
SELECT AA.* FROM (
SELECT A.CUI, B.concept_id, B.vocabulary_id FROM umls_cui.MRCONSO as A LEFT JOIN vocabulary.concept as B ON A.CODE=B.concept_code WHERE A.LAT='ENG' AND A.SAB='NDFRT' AND B.vocabulary_id='NDFRT'
) AA GROUP BY AA.CUI, AA.concept_id, AA.vocabulary_id
UNION
SELECT AA.* FROM (
SELECT A.CUI, B.concept_id, B.vocabulary_id FROM umls_cui.MRCONSO as A LEFT JOIN vocabulary.concept as B ON A.CODE=B.concept_code WHERE A.LAT='ENG' AND A.SAB='SNOMEDCT_US' AND B.vocabulary_id='SNOMED'
) AA GROUP BY AA.CUI, AA.concept_id, AA.vocabulary_id
UNION
SELECT AA.* FROM (
SELECT A.CUI, B.concept_id, B.vocabulary_id FROM umls_cui.MRCONSO as A LEFT JOIN vocabulary.concept as B ON A.CODE=B.concept_code WHERE A.LAT='ENG' AND A.SAB='LNC' AND B.vocabulary_id='LOINC'
) AA GROUP BY AA.CUI, AA.concept_id, AA.vocabulary_id
) as AAA
);

CREATE INDEX X_cui ON vocabulary.OHDSI_to_CUI(cui);
CREATE INDEX X_concept_id ON vocabulary.OHDSI_to_CUI(concept_id);
CREATE INDEX X_vocabulary_id ON vocabulary.OHDSI_to_CUI(vocabulary_id);
```