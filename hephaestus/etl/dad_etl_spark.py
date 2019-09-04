from datetime import datetime, timedelta
import json

import os
import findspark
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

    def read_head(self):
        self._df.show()
        self.stop_spark()

    def process_rows(row):
        pass

    def etl(self):
        result = self._df.rdd.map(self.process_rows)
        self.stop_spark()

    def stop_spark(self):
        self._spark.stop()
