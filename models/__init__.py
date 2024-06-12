from .base import Base
from .patient import Patient
from .doctor import Doctor
from .appointment import Appointment
from .medical_record import MedicalRecord
from ..database import engine  

def init_db():
    Base.metadata.create_all(bind=engine)
