
# :stars: Hephaestus - Data analytics tools for Digital Health!

*Hephaestus was the god of fire, metalworking, stone masonry, forges and the art of sculpture.*

## About

Efficient and effective health data warehousing and analysis require a common data model. 

The [OHDSI - OMOP Common Data Model](https://www.ohdsi.org/) allows for the systematic analysis of disparate observational databases and EMRs. The data from disparate systems needs to be extracted, transformed and loaded on to a CDM database. Once a database has been converted to the OMOP CDM, evidence can be generated using standardized analytics tools.

Each data source requires customized ETL tools for this conversion. :stars: Hephestus is a tool for this ETL process organized into modules to allow code reuse between various ETL tools for open-source EMR systems and data sources. :stars: Hephestus uses [*SqlAlchemy*](https://www.sqlalchemy.org/) for database connection and automapping tables to classes and [*bonobo*](https://www.bonobo-project.org/) for managing ETL. Hephaestus also aims to support common machine learning workflows such as model building with Apache spark. 


## Design principles

* Support common functions such as creating OMOP table structure from the command line.
* Use ORM (sqlalchemy) and ETL (bonobo) libraries to reduce boilerplate code and make code extensible and reusable.
* Support ETL for common open-source EMRs such as OpenMRS and OSCAR EMR, and national level health databases such as Discharge Abstract Database (Canada) from the command line.
* Create libraries to support common use cases such as vocabulary lookup and [Cui2Vec](http://cui2vec.dbmi.hms.harvard.edu/) based concept similarity search.
* Support patient-level predictions.
* Extend OMOP for public health use cases and support cohort-level predictions using MLlib (Spark's machine learning library).

![Hephaestus](https://raw.github.com/dermatologist/hephaestus/develop/notes/hephaestus.png)

## Features (Expected)

### ETL tools for open source EMRs (OpenMRS and OSCAR EMR) and Discharge Anstract Database (Canada)
* Work in Progress
* Ref : https://github.com/maurya/openmrs-module-ohdsi

### [Cui2Vec](http://cui2vec.dbmi.hms.harvard.edu/) based concept similarity search *hepahestus/vocabulary* folder
* Work in progress
* Create tables using instructions here: https://github.com/E-Health/OHDSIconceptid2cui
* Cui.init_model() downloads and builds [Cui2Vec](https://arxiv.org/abs/1804.01486) model.
* Find similar concepts, outliers and calculate distances.
* Cui2Vec for noisy labeling and anchor learning.
* See Also: https://github.com/OHDSI/Aphrodite

### Spark ML based model building with tools for deploying models on serverless framework
* Work in progress
* See Also: https://github.com/OHDSI/PatientLevelPrediction

## How to contribute and use:

### Hephaestus is a work in progress. Please read CONTRIBUTING.md for more information on joining this project.

## What it does

### ETL
* [x] Work in progress

### ML
* [x] Work in progress

### Deployment artifacts
* [x] Work in progress

## How to install

```text

Work in progress


```

## How to Use

* Use [OHDSIconceptid2cui](https://github.com/E-Health/OHDSIconceptid2cui) to create the mapping table ohdsi_to_cui in the vocabulary schema for all [cui2vec](https://arxiv.org/abs/1804.01486) functions of Hephaestus.
* WIP


### Command-line options

```text
work in progress

```

| Command | Alternate | Description |
| --- | --- | --- |
| --inp | -i | Input file in the text format with <break> Topic </break> |



## Contributors and other projects

* [Bell Eapen](https://nuchange.ca) (McMaster U) |  [Contact](https://nuchange.ca/contact)
* This software is developed and tested using [Compute Canada](http://www.computecanada.ca) resources.
* See also:  [:fire: The FHIRForm framework for managing healthcare eForms](https://github.com/E-Health/fhirform)
* See also: [:eyes: Drishti | An mHealth sense-plan-act framework!](https://github.com/E-Health/drishti)
* See also [:flashlight: Qualitative Research support tools in Python](https://github.com/dermatologist/nlp-qrmine)
* See also [:hospital: Public Health Data Warehouse using FHIR and Kibana](https://github.com/E-Health/phis-dw)



## Citation

```

@misc{eapenbr2018Hephaestus,
  title={Hephaestus - Data warehouse and ETL tools for open source EMRs.},
  author={Eapen, Bell Raj and contributors},
  year={2018},
  publisher={GitHub},
  journal = {GitHub repository},
  howpublished={\url{https://github.com/dermatologist/hephaestus}}
}

```

### Disclaimer

*Parts of this material are based on the Canadian Institute for Health Information Discharge Abstract Database Research Analytic Files (sampled from fiscal years 2014-15). However the analysis, conclusions, opinions and statements expressed herein are those of the author(s) and not those of the Canadian Institute for Health Information.*
