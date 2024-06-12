from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Doctor(Base):
    __tablename__ = 'doctors'
    doctor_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    appointments = relationship('Appointment', back_populates='doctor')
    medical_records = relationship('MedicalRecord', back_populates='doctor')
