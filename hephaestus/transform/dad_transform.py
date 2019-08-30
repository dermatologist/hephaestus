import datetime
import time

from hephaestus.cdm.automap import Location, Person, Observation, Procedure_occurrence
from hephaestus.settings import LocalSettings as C


def transform(*args):
    location = Location()
    person = Person()
    observation = Observation()
    procedure_occurence = Procedure_occurrence()

    for row in args:
        person.person_source_value = row[1]
        if row[4] == 'M':
            person.gender_concept_id = C.CDM_CONCEPT_MALE
        else:
            person.gender_concept_id = C.CDM_CONCEPT_FEMALE
        today = datetime.today()
        if row[3] == 'newborn':
            person.year_of_birth = today.year
        yield person
