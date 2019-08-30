from hephaestus.models.cci_model import CciModel


def transform(*args):
    cci = CciModel()
    for row in args:
        cci.cci_code = row[1]
        cci.cci_short = row[2]
        cci.cci_long = row[3]
        yield cci
