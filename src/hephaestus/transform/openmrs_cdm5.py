from datetime import datetime

import src.hephaestus.constants as C


def transform(*args):
    for arg in args:
        yield arg


"""

Transforms an OpenMRS person to CDM person

"""


def transform_person(openmrs_person, cdm_person):
    cdm_person.person_id = openmrs_person.person_id

    cdm_person.gender_concept_id = 0  # Default unknown value
    if openmrs_person.gender.upper() == 'M':
        cdm_person.gender_concept_id = C.OMOP_CONSTANTS.GENDER_MALE
    if openmrs_person.gender.upper() == 'F':
        cdm_person.gender_concept_id = C.OMOP_CONSTANTS.GENDER_FEMALE

    # Birthdate
    dt = datetime.strptime(openmrs_person.birthdate, '%Y-%m-%d %H:%M:%S')
    cdm_person.year_of_birth = dt.year
    cdm_person.month_of_birth = dt.month
    cdm_person.day_of_birth = dt.day

    return cdm_person
