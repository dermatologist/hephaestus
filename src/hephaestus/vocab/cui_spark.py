import pkg_resources
from gensim.models import KeyedVectors

from src.hephaestus import settings as C

"""
This demonstrates how to use spark
The model should be available to all nodes. (In compute canada all nodes have access to the same file)
In a different environment use S3 bucket or something similar
Ref: https://trivial.io/word2vec-on-databricks-791157831eaa

Loading the model is an expensive operation.
The following pattern makes sure that model is loaded only once.
"""


class CuiSpark(object):
    # This is never serialized
    # ref: https://trivial.io/word2vec-on-databricks-791157831eaa
    cache = {}

    def __init__(self, model='cui2vec_gensim.bin'):
        self._respath = pkg_resources.resource_filename('hephaestus', 'resources') + '/'
        self.fn = self._respath + model

    @property
    def cui2vec(self):
        if self.fn not in CuiSpark.cache:
            CuiSpark.cache[self.fn] = \
                KeyedVectors.load_word2vec_format(self.fn, binary=True)
        return CuiSpark.cache[self.fn]

    """
    Note that the return type is an array.
    If It was cui, use map as documented in test_cuiSpark.py
    """

    def similar_cuis(self, cui):
        try:
            return self.cui2vec.most_similar(cui)
        except:
            return []

    def concepts_to_cuis(self, spark, concepts):
        dbsql = "(select * from {}.ohdsi_to_cui) as tmptest"
        dbsql = dbsql.format(C.CDM_USER_VOCAB)
        df = spark.read \
            .format("jdbc") \
            .option("url", C.JDBC_CDM_URL) \
            .option("dbtable", dbsql) \
            .option("user", C.CDM_USER_NAME) \
            .option("password", C.CDM_USER_PASS) \
            .option("driver", "org.postgresql.Driver") \
            .load()
        # df.printSchema()
        df.createOrReplaceTempView("ohdsi_cui")
        sql = "SELECT cui FROM ohdsi_cui WHERE concept_id IN {}"
        sql = sql.format(concepts)
        # replace [] with () in the IN clause
        _cuis = spark.sql(sql.replace("[", "(").replace("]", ")"))
        pandas_cuis = _cuis.toPandas()
        cuis = []
        for index, rows in pandas_cuis.iterrows():
            cuis.append(rows.cui.strip())
        return cuis
