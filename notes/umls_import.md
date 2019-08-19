
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