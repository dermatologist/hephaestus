import csv

import pkg_resources

from .. import settings as C

respath = pkg_resources.resource_filename('hephaestus', 'resources') + '/'
dad_file = respath + C.SOURCE_USER_CCI_FILE


def read_cci():
    with open(dad_file, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            yield row
    csvFile.close()
