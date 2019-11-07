import random
from datetime import datetime, timedelta

from sqlalchemy.orm import sessionmaker

from src.hephaestus import settings as C
from hephaestus.cdm.automap import Person, Visit_occurrence, \
    Condition_occurrence, Observation_period
from hephaestus.service import pgsql
from hephaestus.vocab.cdm_vocabulary import CdmVocabulary


def transform(*args):
    person = Person()
    visit_occurrence = Visit_occurrence()
    condition_occurrence = Condition_occurrence()
    observation_period = Observation_period()
    # procedure_occurrence = Procedure_occurrence()
    currentYear = datetime.now().year
    _end_datetime = datetime.now()
    _end_date = str(_end_datetime).split()[0]
    # cdm = CdmVocabulary()
    # cci = Cci()
    Session = sessionmaker(bind=pgsql.get_schema_engine(C.CDM_USER_VOCAB))
    session = Session()
    for row in args:
        _start_datetime = datetime.now() - timedelta(days=int(row[153]))
        _start_date = str(_start_datetime).split()[0]
        """
        Transforming person
        The unique personid from row 158 is used
        """
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
            person.gender_concept_id = int(C.CDM_CONCEPT_MALE)
        else:
            person.gender_concept_id = int(C.CDM_CONCEPT_FEMALE)
        person.race_concept_id = int(C.CDM_NOT_DEFINED)
        person.ethnicity_concept_id = int(C.CDM_NOT_DEFINED)
        person.gender_source_concept_id = int(C.CDM_NOT_DEFINED)
        person.race_source_concept_id = int(C.CDM_NOT_DEFINED)
        person.ethnicity_source_concept_id = int(C.CDM_NOT_DEFINED)
        yield person

        """
        Transforming visit
        TODO: find concept numbers of categories and improve below
        """
        visit_occurrence.visit_occurrence_id = row[0]
        visit_occurrence.person_id = person.person_id
        visit_occurrence.visit_concept_id = int(
            C.CDM_ADM_DISC_HOSP_VISIT)  # Hospice (hospital based)@Admit through Discharge Claim
        visit_occurrence.visit_start_datetime = _start_datetime  # Length of stay
        visit_occurrence.visit_end_datetime = _end_datetime
        visit_occurrence.visit_start_date = _start_date  # Length of stay
        visit_occurrence.visit_end_date = _end_date
        visit_occurrence.visit_type_concept_id = int(C.CDM_ADM_DISC_HOSP_VISIT)
        visit_occurrence.visit_source_concept_id = int(C.CDM_ADM_DISC_HOSP_VISIT)
        visit_occurrence.visit_source_value = row[5]  # admit category
        visit_occurrence.admitted_from_concept_id = int(C.CDM_ADM_DISC_HOSP_VISIT)
        visit_occurrence.discharge_to_concept_id = int(C.CDM_ADM_DISC_HOSP_VISIT)

        yield visit_occurrence

        observation_period.observation_period_id = row[0]
        observation_period.person_id = person.person_id
        observation_period.observation_period_start_date = _start_date  # Length of stay
        observation_period.observation_period_end_date = _end_date
        observation_period.period_type_concept_id = int(C.CDM_NOT_DEFINED)

        yield observation_period

        # Create the linked diagnosis records
        column_range = range(10, 59, 2)
        for column in column_range:
            if column % 2 == 0:
                if len(row[column].strip()) > 2:
                    # print(row[column] + ' | ' + row[column + 1])
                    if len(row[column].strip()) > 3:
                        icd = row[column][:3] + '.' + row[column][3:4]
                    else:
                        icd = row[column]
                    condition_occurrence.condition_occurrence_id = random.randint(1, 9223372036854775807)
                    condition_occurrence.person_id = row[158]
                    # cdm.set_concept(icd)
                    # condition_occurrence.condition_concept_id = cdm.concept_id
                    condition_occurrence.condition_concept_id = CdmVocabulary.get_concept_id(icd, session)
                    condition_occurrence.condition_start_datetime = _start_datetime
                    condition_occurrence.condition_end_datetime = _end_datetime
                    condition_occurrence.condition_start_date = _start_date
                    condition_occurrence.condition_end_date = _end_date
                    condition_occurrence.condition_source_concept_id = int(C.CDM_NOT_DEFINED)
                    condition_occurrence.condition_source_value = row[column].strip()
                    # TODO Change this
                    condition_occurrence.condition_type_concept_id = int(C.CDM_NOT_DEFINED)
                    condition_occurrence.condition_status_concept_id = int(C.CDM_NOT_DEFINED)
                    condition_occurrence.visit_occurrence_id = visit_occurrence.visit_occurrence_id
                    yield condition_occurrence

        yield row

        # if len(row[10].strip()) > 3:
        #     yield row[10][:3] + '.' + row[10][3:4]
        # else:
        #     yield row[10]

        # # Fix any blank cells
        # column_range = range(1, 153)
        # for column in column_range:
        #     if row[column] == ' ':
        #         row[column] = '-1'

        # Create the linked diagnosis records
        # column_range = range(10, 59)
        # for column in column_range:
        #     if column % 2 == 0:
        #         if len(row[column].strip()) > 2:
        #             # print(row[column] + ' | ' + row[column + 1])
        #             if len(row[column].strip()) > 3:
        #                 icd = row[column][:3] + '.' + row[column][3:4]
        #             else:
        #                 icd = row[column]
        #             condition_occurrence.condition_occurrence_id = random.randint(1, 9223372036854775807)
        #             condition_occurrence.person_id = person.person_id
        #             cdm.set_concept(icd)
        #             condition_occurrence.condition_concept_id = cdm.concept_id
        #             condition_occurrence.condition_start_datetime = datetime.now()
        #             condition_occurrence.condition_source_concept_id = int(C.CDM_NOT_DEFINED)
        #             condition_occurrence.condition_source_value = row[column].strip()
        #             # TODO Change this
        #             condition_occurrence.condition_type_concept_id = int(C.CDM_NOT_DEFINED)
        #             condition_occurrence.condition_status_concept_id = int(C.CDM_NOT_DEFINED)
        #             condition_occurrence.visit_occurrence_id = visit_occurrence.visit_occurrence_id
        #             yield condition_occurrence
        #
        # # Create the linked intervention records
        # column_range = range(60, 139)
        # for column in column_range:
        #     if column % 4 == 0:
        #         if len(row[column].strip()) > 2:
        #             # print(row[column] + ' | ' + row[column + 1] + ' | ' + row[column + 2] + ' | ' + row[
        #             #     column + 3])
        #             cci.cci_code = row[column].strip()
        #             # print(cci.cci_long)
        #             procedure_occurrence.procedure_occurrence_id = random.randint(1, 9223372036854775807)
        #             procedure_occurrence.person_id = person.person_id
        #             # TODO CCI codes are not mapped yet
        #             procedure_occurrence.procedure_concept_id = int(C.CDM_NOT_DEFINED)
        #             procedure_occurrence.procedure_datetime = datetime.now()
        #             # TODO fix me
        #             procedure_occurrence.procedure_type_concept_id = int(C.CDM_NOT_DEFINED)
        #             procedure_occurrence.modifier_concept_id = int(C.CDM_NOT_DEFINED)
        #             procedure_occurrence.procedure_source_value = row[column].strip()
        #             procedure_occurrence.procedure_source_concept_id = int(C.CDM_NOT_DEFINED)
        #             yield procedure_occurrence

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
