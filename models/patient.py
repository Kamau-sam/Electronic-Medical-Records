
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .base import Base

class Patient(Base):
    __tablename__ = 'patients'
    patient_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    appointments = relationship('Appointment', back_populates='patient')
    medical_records = relationship('MedicalRecord', back_populates='patient')