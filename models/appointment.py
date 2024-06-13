from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


# Define the Appointment model class
class Appointment(Base):
    __tablename__ = 'appointments'
    appointment_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    reason = Column(String, nullable=False)

#Relationship to the Patient , doctor, and medical record model
    patient = relationship('Patient', back_populates='appointments')
    doctor = relationship('Doctor', back_populates='appointments')
    medical_record = relationship('MedicalRecord', uselist=False, back_populates='appointment')
