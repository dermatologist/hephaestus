from datetime import datetime

import findspark
import os
import pkg_resources

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
        # https://changhsinlee.com/pyspark-udf/
        from pyspark.sql.functions import udf
        from pyspark.sql.types import StringType
        # https://stackoverflow.com/questions/33681487/how-do-i-add-a-new-column-to-a-spark-dataframe-using-pyspark
        from pyspark.sql.functions import lit
        udf_age_to_year = udf(lambda age: DadEtlSpark.age_to_year(age), StringType())
        udf_gender_to_code = udf(lambda gender: DadEtlSpark.gender_to_code(gender), StringType())
        df1 = self._df.withColumn("year_of_birth", udf_age_to_year("AGRP_F_D")) \
            .withColumn("gender_concept_id", udf_gender_to_code("GENDER")) \
            .withColumn("race_concept_id", lit(0)) \
            .withColumn("ethnicity_concept_id", lit(0)) \
            .withColumn("gender_source_concept_id", lit(0)) \
            .withColumn("race_source_concept_id", lit(0)) \
            .withColumn("ethnicity_source_concept_id", lit(0)) \
            # https://spark.apache.org/docs/2.3.0/sql-programming-guide.html
        # https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PySpark_SQL_Cheat_Sheet_Python.pdf
        # sql1 = "SELECT PATNT_ID AS person_id, " \
        #        "PATNT_ID AS person_source_value, " \
        #        "year_of_birth "
        # https://stackoverflow.com/questions/34077353/how-to-change-dataframe-column-names-in-pyspark
        df2 = df1.selectExpr("PATNT_ID AS person_id",
                             "PATNT_ID AS person_source_value",
                             "gender_concept_id",
                             "ethnicity_concept_id", "gender_source_concept_id",
                             "race_source_concept_id", "ethnicity_source_concept_id",
                             "year_of_birth", "race_concept_id")

        mode = "overwrite"
        properties = {
            "user": self._username,
            "password": self._password,
            "schema": self._schema,
            "driver": "org.postgresql.Driver"
        }
        df2.write.jdbc(url=self._url, table="person", mode=mode, properties=properties)
        # df2.show()
        # df1 = self._df
        # self._df.show()

    def read_head(self):
        self._df.show()
        self.stop_spark()

    def process_rows(self, row):
        pass

    def etl(self):
        result = self._df.rdd.map(self.process_rows)
        self.stop_spark()

    @staticmethod
    def gender_to_code(gender):
        if gender.strip() == 'M':
            return C.CDM_CONCEPT_MALE
        else:
            return C.CDM_CONCEPT_FEMALE

    @staticmethod
    def age_to_year(age):
        currentYear = datetime.now().year
        year_of_birth = 0
        if age.strip() == 'newborn':
            year_of_birth = currentYear
        elif age.strip() == '0 days to 11 months':
            year_of_birth = currentYear - 1
        elif age.strip() == '1-7 yrs':
            year_of_birth = currentYear - 4
        elif age.strip() == '8-12 yrs':
            year_of_birth = currentYear - 10
        elif age.strip() == '13-17 yrs':
            year_of_birth = currentYear - 15
        elif age.strip() == '18-24 yrs':
            year_of_birth = currentYear - 21
        elif age.strip() == '25-29 yrs':
            year_of_birth = currentYear - 27
        elif age.strip() == '30-34 yrs':
            year_of_birth = currentYear - 32
        elif age.strip() == '35-39 yrs':
            year_of_birth = currentYear - 37
        elif age.strip() == '40-44 yrs':
            year_of_birth = currentYear - 42
        elif age.strip() == '45-49 yrs':
            year_of_birth = currentYear - 47
        elif age.strip() == '50-54 yrs':
            year_of_birth = currentYear - 52
        elif age.strip() == '55-59 yrs':
            year_of_birth = currentYear - 57
        elif age.strip() == '60-64 yrs':
            year_of_birth = currentYear - 62
        elif age.strip() == '65-69 yrs':
            year_of_birth = currentYear - 67
        elif age.strip() == '70-74 yrs':
            year_of_birth = currentYear - 72
        elif age.strip() == '75-79 yrs':
            year_of_birth = currentYear - 77
        elif age.strip() == '80+ yrs':
            year_of_birth = currentYear - 82
        else:
            year_of_birth = 0
        return str(year_of_birth)

    def stop_spark(self):
        self._spark.stop()
