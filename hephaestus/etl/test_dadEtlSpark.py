from unittest import TestCase

from hephaestus.etl.dad_etl_spark import DadEtlSpark


class TestDadEtlSpark(TestCase):
    def setUp(self):
        self._etl = DadEtlSpark()

    # def test_read_head(self):
    #     head = self._etl.read_head()
    #     self.assertIsNone(head['SUB_PROV'], 'Head is None')
    #
    # def test_etl(self):
    #     result = self._etl.etl()
    #
    # def test_process_rows(self):
    #     self.fail()

    def test_transform_person(self):
        self._etl.transform_person()
        print("Done")
