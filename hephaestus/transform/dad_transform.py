from datetime import datetime

from hephaestus.cdm.automap import Location, Person, Observation, Procedure_occurrence
from hephaestus.settings import LocalSettings as C


def transform(*args):
    location = Location()
    person = Person()
    observation = Observation()
    procedure_occurence = Procedure_occurrence()
    currentYear = datetime.now().year
    for row in args:
        person.person_source_value = row[0]
        location.location_source_value = row[1]
        if row[2].strip() == 'newborn':
            person.year_of_birth = currentYear
        elif row[2].strip() == '1-7 yrs':
            person.year_of_birth = currentYear - 4
        elif row[2].strip() == '8-12 yrs':
            person.year_of_birth = currentYear - 10
        elif row[2].strip() == '13-17 yrs':
            person.year_of_birth = currentYear - 15
        # TODO to complete
        if row[3] == 'M':
            person.gender_concept_id = C.CDM_CONCEPT_MALE
        else:
            person.gender_concept_id = C.CDM_CONCEPT_FEMALE
        yield person
        yield location
        yield row[2]
