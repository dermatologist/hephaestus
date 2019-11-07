import findspark
import os

from src.hephaestus import settings as C

os.environ["JAVA_HOME"] = C.JAVA_HOME
os.environ['PYSPARK_SUBMIT_ARGS'] = C.PYSPARK_SUBMIT_ARGS
findspark.init(C.SPARK_HOME)
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("CDM-Spark") \
    .getOrCreate()
df = spark.read \
    .format("jdbc") \
    .option("url", C.JDBC_CDM_URL) \
    .option("dbtable", "(select * from vocabulary.concept) as tmptest") \
    .option("user", C.CDM_USER_NAME) \
    .option("password", C.CDM_USER_PASS) \
    .option("driver", "org.postgresql.Driver") \
    .load()
df.printSchema()
print(df.count())
