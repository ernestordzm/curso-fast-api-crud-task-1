

from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base


#server = 'DESKTOP-R8OR3OF'
server = 'LOCALHOST'

database = 'PROMFAM2'
username = 'famsa'
password = 'famsa'
port = 1433
driver='ODBC Driver 17 for SQL Server'

#DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/tasks"
#DATABASE_URL = "mysql+mysqlconnector://username:password@localhost:1433/database"
#DATABASE_URL = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}')

# DATABASE_URL = 'mssql+pyodbc://sa:Erm58631#@{LOCALHOST}:1433/PROMFAM2?driver=ODBC+Driver+17+for+SQL+Server'

# DATABASE_URL = 'mssql+pyodbc://famsa:famsa@LOCALHOST/PROMFAM2?driver=ODBC+Driver+17+for+SQL+Server'

DATABASE_URL = 'mssql+pyodbc://'+username+':'+password+'@'+server+'/'+database+'?driver='+driver

# DATABASE_URL = 'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

# DATABASE_URL = URL.create(
#     "mssql+pyodbc",
#     username=username,
#     password=password,
#     host=server,
#     database=database,
#     query={"driver": driver}
# )



engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_database_session():
    try:
        db = SessionLocal()
#        print("*** INIT DB ***")
        yield db
        # return db
    finally:
#        print("*** END DB ***")
        db.close()
#    print('aaa')

