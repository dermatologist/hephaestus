from unittest import TestCase

from hephaestus.utils.import_cci import Cci


class TestCci(TestCase):
    def setUp(self):
        self._cci = Cci()

    def test_cci(self):
        self._cci.get_cci()
