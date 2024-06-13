from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = 'sqlite:///emr.db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)





#UPDATE doctors
#SET specialty = 'Dermatology', phone_number = '0723456794'
#WHERE doctor_id = 1;


#SELECT * FROM patients WHERE name LIKE '%Mwangi%';

#
