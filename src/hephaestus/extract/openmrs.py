from bonobo.config import use
from sqlalchemy.orm import Session


@use('mysql_engine', 'mysql_base')
def extract_person(mysql_engine, mysql_base):
    session = Session(mysql_engine)
    Person = mysql_base.classes.person
    persons = session.query(Person).all()
    for person in persons:
        yield person


@use('mysql_engine', 'mysql_base')
def extract_patient_identifier(mysql_engine, mysql_base, person_id):
    session = Session(mysql_engine)
    Patient_identifier = mysql_base.classes.patient_identifier
    patient_identifiers = session.query(Patient_identifier).filter(Patient_identifier.patient_id == person_id)
    for patient_identifier in patient_identifiers:
        yield patient_identifier


@use('mysql_engine', 'mysql_base')
def extract_provider(mysql_engine, mysql_base):
    session = Session(mysql_engine)
    Provider = mysql_base.classes.provider
    providers = session.query(Provider).distinct()
    for provider in providers:
        yield provider


@use('mysql_engine', 'mysql_base')
def extract_observation_person_id(mysql_engine, mysql_base):
    session = Session(mysql_engine)
    Observation = mysql_base.classes.obs
    observations = session.query(Observation).distinct(Observation.person_id)
    for observation in observations:
        yield observation


@use('mysql_engine', 'mysql_base')
def extract_observation(mysql_engine, mysql_base):
    session = Session(mysql_engine)
    Observation = mysql_base.classes.obs
    observations = session.query(Observation)
    for observation in observations:
        yield observation


@use('mysql_engine', 'mysql_base')
def extract_encounter(mysql_engine, mysql_base):
    session = Session(mysql_engine)
    Encounter = mysql_base.classes.encounter
    encounters = session.query(Encounter)
    for encounter in encounters:
        yield encounter
