import csv

import pkg_resources
from sqlalchemy import MetaData, Column, Integer, String, Table, Date

from src.hephaestus import settings as C
from hephaestus.service import pgsql

respath = pkg_resources.resource_filename('hephaestus', 'resources') + '/'
dad_file = respath + C.SOURCE_USER_DAD_FILE


def read_dad():
    engine = pgsql.get_schema_engine(C.CDM_USER_DAD_SCHEMA)  # Access the DB Engine
    if not engine.dialect.has_table(engine, 'location_history'):  # If table don't exist, Create.
        metadata = MetaData(engine)
        # Create a table with the appropriate Columns
        Table('location_history', metadata,
              Column('location_id', Integer, nullable=False),
              Column('relationship_type_concept_id', String, nullable=False),
              Column('domain_id', String, nullable=False),
              Column('entity_id', Integer, nullable=False),
              Column('start_date', Date, nullable=False),
              Column('end_date', Date))
        metadata.create_all()

    with open(dad_file, 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader, None)  # skip the headers
        for row in reader:
            yield row
    csvFile.close()
