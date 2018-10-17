
# :stars: Hephaestus - Data warehouse and ETL tools for open source EMRs!

## About

The [OHDSI - OMOP Common Data Model](https://www.ohdsi.org/) allows for the systematic analysis of disparate observational databases and EMRs. The data from disparate systems needs to be extracted, transformed and loaded on to a CDM database. Once a database has been converted to the OMOP CDM, evidence can be generated using standardized analytics tools.

Each data source requires customized ETL tools for this conversion. :stars: Hephestus is a tool for this ETL process organized into modules to allow code reuse between various ETL tools for open-source EMR systems and data sources. :stars: Hephestus uses [*SqlAlchemy*](https://www.sqlalchemy.org/) for database connection and automapping tables to classes and [*bonobo*](https://www.bonobo-project.org/) for managing ETL.

## Supported systems

* [x] [OpenMRS](http://openmrs.org)
* [ ] [OSCAR EMR](https://oscar-emr.com/)
* [ ] DAD.
* [ ] [SynPuf](https://github.com/OHDSI/ETL-CMS)

## How to use

Work in progress. Do not use in production

## Contributors

[Bell Eapen](https://nuchange.ca) | McMaster U

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
