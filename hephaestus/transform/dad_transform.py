from datetime import datetime

from sqlalchemy.orm import Session

from hephaestus import settings as C
from hephaestus.cdm.automap import Location, Person, Observation, Procedure_occurrence, Provider
from hephaestus.service import pgsql


def transform(*args):
    location = Location()
    person = Person()
    observation = Observation()
    procedure_occurence = Procedure_occurrence()
    provider = Provider()
    currentYear = datetime.now().year
    session = Session(pgsql.get_schema_engine(C.CDM_USER_DAD_SCHEMA))

    for row in args:
        # person.person_id = row[0]
        person.person_id = row[158]
        person.person_source_value = row[158]
        # location.location_source_value = row[1]
        if row[2].strip() == 'newborn':
            person.year_of_birth = currentYear
        elif row[2].strip() == '0 days to 11 months':
            person.year_of_birth = currentYear - 1
        elif row[2].strip() == '1-7 yrs':
            person.year_of_birth = currentYear - 4
        elif row[2].strip() == '8-12 yrs':
            person.year_of_birth = currentYear - 10
        elif row[2].strip() == '13-17 yrs':
            person.year_of_birth = currentYear - 15
        elif row[2].strip() == '18-24 yrs':
            person.year_of_birth = currentYear - 21
        elif row[2].strip() == '25-29 yrs':
            person.year_of_birth = currentYear - 27
        elif row[2].strip() == '30-34 yrs':
            person.year_of_birth = currentYear - 32
        elif row[2].strip() == '35-39 yrs':
            person.year_of_birth = currentYear - 37
        elif row[2].strip() == '40-44 yrs':
            person.year_of_birth = currentYear - 42
        elif row[2].strip() == '45-49 yrs':
            person.year_of_birth = currentYear - 47
        elif row[2].strip() == '50-54 yrs':
            person.year_of_birth = currentYear - 52
        elif row[2].strip() == '55-59 yrs':
            person.year_of_birth = currentYear - 57
        elif row[2].strip() == '60-64 yrs':
            person.year_of_birth = currentYear - 62
        elif row[2].strip() == '65-69 yrs':
            person.year_of_birth = currentYear - 67
        elif row[2].strip() == '70-74 yrs':
            person.year_of_birth = currentYear - 72
        elif row[2].strip() == '75-79 yrs':
            person.year_of_birth = currentYear - 77
        elif row[2].strip() == '80+ yrs':
            person.year_of_birth = currentYear - 82
        else:
            print("Not processed" + row[2].strip())
        # TODO to complete
        if row[3] == 'M':
            person.gender_concept_id = C.CDM_CONCEPT_MALE
        else:
            person.gender_concept_id = C.CDM_CONCEPT_FEMALE
        person.race_concept_id = C.CDM_NOT_DEFINED
        person.ethnicity_concept_id = C.CDM_NOT_DEFINED
        person.gender_source_concept_id = C.CDM_NOT_DEFINED
        person.race_source_concept_id = C.CDM_NOT_DEFINED
        person.ethnicity_source_concept_id = C.CDM_NOT_DEFINED
        if len(row[10].strip()) > 3:
            yield row[10][:3] + '.' + row[10][3:4]
        else:
            yield row[10]
        yield person

        # Fix any blank cells
        # column_range = range(1, 153)
        # for column in column_range:
        #     if row[column] == ' ':
        #         row[column] = '-1'
        #
        # # Create the linked diagnosis records
        # column_range = range(11, 60)
        # for column in column_range:
        #     if column % 2 == 1:
        #         if len(row[column]) > 2:
        #             print(row[column] + ' | ' + row[column + 1])
        #             sql = "INSERT INTO `morbidity` " \
        #                   "(`icd_10_ca`, `type`, `encounter_encounter_id`) " \
        #                   "VALUES (%s, %s, %s)"
        #             cursor.execute(sql, (row[column], row[column + 1], encounter_id))
        #
        # # Create the linked intervention records
        # column_range = range(61, 140)
        # for column in column_range:
        #     if column % 4 == 1:
        #         if len(row[column]) > 2:
        #             print(row[column] + ' | ' + row[column + 1] + ' | ' + row[column + 2] + ' | ' + row[
        #                 column + 3])
        #             sql = "INSERT INTO `intervention` " \
        #                   "(`cci_code`, `status`, `location`, `anaesthetic`, `encounter_encounter_id`) " \
        #                   "VALUES (%s, %s, %s, %s, %s)"
        #             cursor.execute(sql, (row[column], row[column + 1],
        #                                  row[column + 2], row[column + 3], encounter_id))
        #
        # # Create the linked speciality care records
        # column_range = range(142, 153)
        # for column in column_range:
        #     if column % 2 == 0:
        #         if int(row[column]) < 99:
        #             print(row[column] + ' | ' + row[column + 1])
        #             sql = "INSERT INTO `special_care` " \
        #                   "(`unit`, `hours`, `encounter_encounter_id`) " \
        #                   "VALUES (%s, %s, %s)"
        #             cursor.execute(sql, (row[column], row[column + 1],
        #                                  encounter_id))

        # yield location
