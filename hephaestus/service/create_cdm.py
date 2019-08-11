import requests
from sqlalchemy.orm import Session
from hephaestus.service import pgsql


def execute_sql(url):
    req = requests.get(
        url,
        stream=True)
    pgsql_engine = pgsql.get_writer()
    session = Session(pgsql_engine)
    # Create an empty command string
    sql_command = ''
    is_comment = False
    for line in req.iter_lines():
        line = line.decode("utf-8")
        if line.strip().startswith('/*') or line.strip().startswith('*'):
            is_comment = True
        if line.strip().endswith('*/'):
            is_comment = False

        # Ignore commented lines
        if not line.startswith('--') and line.strip('\n') and not is_comment and not "*" in line:
            # Append line to the command string
            sql_command += line.strip('\n')

            # If the command string ends with ';', it is a full statement
            if sql_command.endswith(';'):
                # Try to execute statement and commit it
                try:
                    session.execute(sql_command)
                    session.commit()
                    print(sql_command)
                # Assert in case of error
                except:
                    print('Ops')
                    print(sql_command)
                # Finally, clear command string
                finally:
                    sql_command = ''


def load_cdm():
    execute_sql('https://raw.githubusercontent.com/OHDSI/CommonDataModel/master/PostgreSQL/OMOP%20CDM%20postgresql%20ddl.txt')


def set_constraints():
    execute_sql('https://raw.githubusercontent.com/OHDSI/CommonDataModel/master/PostgreSQL/OMOP%20CDM%20postgresql%20pk%20indexes.txt')
    execute_sql('https://raw.githubusercontent.com/OHDSI/CommonDataModel/master/PostgreSQL/OMOP%20CDM%20postgresql%20constraints.txt')



