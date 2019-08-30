import csv

import pkg_resources

from hephaestus.settings import LocalSettings as C

respath = pkg_resources.resource_filename('hephaestus', 'resources') + '/'
dad_file = respath + C.SOURCE_USER_DAD_FILE


def read_dad():
    with open(dad_file, 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader, None)  # skip the headers
        count = 0
        for row in reader:
            count += 1
            if count > 10:
                break
            yield row
    csvFile.close()
