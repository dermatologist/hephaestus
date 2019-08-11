
# :stars: Hephaestus - Data warehouse and ETL tools for open source EMRs!

![Hephaestus](https://raw.github.com/dermatologist/hephaestus/develop/notes/hephaestus.png)

## About

Efficient and effective health data warehousing and analysis require a common data model. 

The [OHDSI - OMOP Common Data Model](https://www.ohdsi.org/) allows for the systematic analysis of disparate observational databases and EMRs. The data from disparate systems needs to be extracted, transformed and loaded on to a CDM database. Once a database has been converted to the OMOP CDM, evidence can be generated using standardized analytics tools.

Each data source requires customized ETL tools for this conversion. :stars: Hephestus is a tool for this ETL process organized into modules to allow code reuse between various ETL tools for open-source EMR systems and data sources. :stars: Hephestus uses [*SqlAlchemy*](https://www.sqlalchemy.org/) for database connection and automapping tables to classes and [*bonobo*](https://www.bonobo-project.org/) for managing ETL.

Hephaestus also aims to support common machine learning workflows such as model building with Apache spark, model optimization using h2o.ai and model deployment using serverless architecture.

## Design principles and plans:

* Support common functions such as creating OMOP table structure from the command line.
* Use ORM (sqlalchemy) and ETL (bonobo) libraries to reduce boilerplate code and make code extensible and reusable.
* Support ETL for common open-source EMRs such as OpenMRS and OSCAR EMR, and national level health databases such as Discharge Abstract Database (Canada) from the command line.
* Create libraries to support common use cases such as vocabulary lookup.
* Support patient-level predictions.
* Extend OMOP for public health use cases and support cohort-level predictions.

## How to contribute and use:

Hephaestus is a work in progress. Please read CONTRIBUTING.md for more information on joining this project.


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
