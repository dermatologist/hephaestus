from datetime import datetime

import findspark
import os
import pkg_resources
from pyspark.sql import Column

from hephaestus import settings as C


class DadEtlSpark(object):

    def __init__(self):
        self._url = C.JDBC_CDM_URL
        self._schema = C.CDM_USER_DAD_SCHEMA
        self._username = C.CDM_USER_NAME
        self._password = C.CDM_USER_PASS
        self._driver = 'org.postgresql.Driver'

        self._respath = pkg_resources.resource_filename('hephaestus', 'resources') + '/'
        self._dad_file = self._respath + C.SOURCE_USER_DAD_FILE

        self._currentYear = datetime.now().year

        os.environ["JAVA_HOME"] = C.JAVA_HOME
        os.environ['PYSPARK_SUBMIT_ARGS'] = C.PYSPARK_SUBMIT_ARGS
        findspark.init(C.SPARK_HOME)
        from pyspark.sql import SparkSession

        self._spark = SparkSession.builder.appName("CDM-Spark").getOrCreate()

        self._df = self._spark.read.format("csv").option("header", "true").load(self._dad_file)

    def write_df(self, df, table):
        properties = {"user": C.CDM_USER_NAME, "password": C.CDM_USER_PASS, "schema": C.CDM_USER_DAD_SCHEMA,
                      "driver": "org.postgresql.Driver"}
        df.write.jdbc(url=self._url,
                      table=table,
                      mode='overwrite',
                      properties=properties
                      )

    def transform_person(self):
        df1 = self._df.withColumn("year_of_birth", self.age_to_year("AGRP_F_D"))
        df1.show()
        sql1 = "SELECT PATNT_ID AS person_id, " \
               "PATNT_ID AS person_source_value, " \
               "year_of_birth AS year_of_birth"
        # df1 = self._df

    def read_head(self):
        self._df.show()
        self.stop_spark()

    def process_rows(self, row):
        pass

    def etl(self):
        result = self._df.rdd.map(self.process_rows)
        self.stop_spark()

    def age_to_year(self, age):
        year_of_birth = 0
        if age.strip() == 'newborn':
            year_of_birth = self._currentYear
        elif age.strip() == '0 days to 11 months':
            year_of_birth = self._currentYear - 1
        elif age.strip() == '1-7 yrs':
            year_of_birth = self._currentYear - 4
        elif age.strip() == '8-12 yrs':
            year_of_birth = self._currentYear - 10
        elif age.strip() == '13-17 yrs':
            year_of_birth = self._currentYear - 15
        elif age.strip() == '18-24 yrs':
            year_of_birth = self._currentYear - 21
        elif age.strip() == '25-29 yrs':
            year_of_birth = self._currentYear - 27
        elif age.strip() == '30-34 yrs':
            year_of_birth = self._currentYear - 32
        elif age.strip() == '35-39 yrs':
            year_of_birth = self._currentYear - 37
        elif age.strip() == '40-44 yrs':
            year_of_birth = self._currentYear - 42
        elif age.strip() == '45-49 yrs':
            year_of_birth = self._currentYear - 47
        elif age.strip() == '50-54 yrs':
            year_of_birth = self._currentYear - 52
        elif age.strip() == '55-59 yrs':
            year_of_birth = self._currentYear - 57
        elif age.strip() == '60-64 yrs':
            year_of_birth = self._currentYear - 62
        elif age.strip() == '65-69 yrs':
            year_of_birth = self._currentYear - 67
        elif age.strip() == '70-74 yrs':
            year_of_birth = self._currentYear - 72
        elif age.strip() == '75-79 yrs':
            year_of_birth = self._currentYear - 77
        elif age.strip() == '80+ yrs':
            year_of_birth = self._currentYear - 82
        else:
            year_of_birth = 0
        return Column(year_of_birth)

    def stop_spark(self):
        self._spark.stop()
