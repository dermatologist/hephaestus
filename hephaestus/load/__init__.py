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
Person = Base.classes.person
Care_site = Base.classes.care_site

# TODO: To complete this
