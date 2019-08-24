"""Settings
Defines constants for the local environment.
Add to .gitignore
"""


class LocalSettings(object):
    SOURCE_USER_NAME = "openmrs"
    SOURCE_USER_PASS = "openmrs"
    SOURCE_USER_DB = "openmrs"
    SOURCE_USER_HOST = "192.168.0.250"
    SOURCE_USER_PORT = 3306

    CDM_USER_NAME = "openmrs"
    CDM_USER_PASS = "openmrs"
    CDM_USER_DB = "openmrs"
    CDM_USER_HOST = "192.168.0.250"
    CDM_USER_PORT = 5432
    CDM_USER_SCHEMA = "hephaestus"
    CDM_USER_VOCAB = "cdm"

    JAVA_HOME = ""
    SPARK_HOME = ""
    SPARK_MASTER_URL = ""
    PYSPARK_SUBMIT_ARGS = ""
    JDBC_CDM_URL = ""
