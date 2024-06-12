from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class MedicalRecord(Base):
    __tablename__ = 'medical_records'
    record_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'), nullable=False)
    appointment_id = Column(Integer, ForeignKey('appointments.appointment_id'), nullable=False)
    diagnosis = Column(String, nullable=False)
    treatment = Column(String, nullable=False)
    notes = Column(String)

    patient = relationship('Patient', back_populates='medical_records')
    doctor = relationship('Doctor', back_populates='medical_records')
    appointment = relationship('Appointment', back_populates='medical_record')
