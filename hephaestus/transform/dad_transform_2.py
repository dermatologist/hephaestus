import random
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from hephaestus import settings as C
from hephaestus.cdm.automap import Location, Person, Observation, Procedure_occurrence, Visit_occurrence, \
    Condition_occurrence, Measurement
from hephaestus.service import pgsql
from hephaestus.vocab.cdm_vocabulary import CdmVocabulary
from hephaestus.utils.import_cci import Cci


def transform2(*args):
    person = Person()
    visit_occurrence = Visit_occurrence()
    condition_occurrence = Condition_occurrence()
    procedure_occurrence = Procedure_occurrence()
    currentYear = datetime.now().year
    cdm = CdmVocabulary()
    cci = Cci()
    for row in args:
        className = row.__class__.__name__
        # classDef = mysql_base.classes[className]
        if className == 'person' or className == 'visit_occurrence' or className == 'condition_occurrence':
            yield row
        else:
            # Create the linked intervention records
            column_range = range(60, 139, 4)
            for column in column_range:
                if column % 4 == 0:
                    if len(row[column].strip()) > 2:
                        # print(row[column] + ' | ' + row[column + 1] + ' | ' + row[column + 2] + ' | ' + row[
                        #     column + 3])
                        cci.cci_code = row[column].strip()
                        # print(cci.cci_long)
                        procedure_occurrence.procedure_occurrence_id = random.randint(1, 9223372036854775807)
                        procedure_occurrence.person_id = row[158]
                        # TODO CCI codes are not mapped yet
                        procedure_occurrence.procedure_concept_id = int(C.CDM_NOT_DEFINED)
                        procedure_occurrence.procedure_datetime = datetime.now()
                        # TODO fix me
                        procedure_occurrence.procedure_type_concept_id = int(C.CDM_NOT_DEFINED)
                        procedure_occurrence.modifier_concept_id = int(C.CDM_NOT_DEFINED)
                        procedure_occurrence.procedure_source_value = row[column].strip()
                        procedure_occurrence.procedure_source_concept_id = int(C.CDM_NOT_DEFINED)
                        yield procedure_occurrence

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
