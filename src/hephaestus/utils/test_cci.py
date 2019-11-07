from unittest import TestCase

from hephaestus.utils.import_cci import Cci


class TestCci(TestCase):
    def setUp(self):
        self._cci = Cci()

    def test_cci(self):
        # self._cci.get_cci()
        pass

    def test_cci_code(self):
        self._cci.cci_code = '1AP59SZAW'
        print(self._cci.cci_long)
        self.assertGreater(len(self._cci.cci_long), 0)
