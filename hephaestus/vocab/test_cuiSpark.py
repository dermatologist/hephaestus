from unittest import TestCase

import findspark
import os

from hephaestus.settings import LocalSettings as C
from hephaestus.vocab.cui_spark import CuiSpark

"""
This test demonstrate how to use spark
See the SetUp and TearDown
spark is a SparkSession. 
parallelize needs sparkcontext: self.spark.sparkContext.parallelize
We used flatMap as .similar_cuis returns an array
If the return type is the same as input use map
"""


class TestCuiSpark(TestCase):
    def setUp(self):
        os.environ["JAVA_HOME"] = C.JAVA_HOME
        os.environ['PYSPARK_SUBMIT_ARGS'] = C.PYSPARK_SUBMIT_ARGS
        findspark.init(C.SPARK_HOME)
        from pyspark.sql import SparkSession

        self.spark = SparkSession \
            .builder \
            .appName("CDM-Spark") \
            .getOrCreate()

    def tearDown(self):
        self.spark.stop()

    def test_similar_cuis(self):
        cuis = ['C0002268', 'C0000052', 'C0000075', 'C0001053', 'C0015278', 'C0017976', 'C0072596']
        sim_cuis = self.spark.sparkContext.parallelize(cuis, 2).flatMap(CuiSpark().similar_cuis).collect()
        print(sim_cuis)
        self.assertGreater(len(sim_cuis), 0)
