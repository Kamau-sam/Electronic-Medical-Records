import click
from datetime import datetime
from sqlalchemy.orm import Session
from.database import SessionLocal, init_db
from.models.patient import Patient
from.models.doctor import Doctor
from.models.appointment import Appointment
from.models.medical_record import MedicalRecord

# Function to add a new patient to the database
def add_patient(db: Session, name: str, date_of_birth: str, gender: str, address: str, phone_number: str):
    patient = Patient(name=name, date_of_birth=datetime.strptime(date_of_birth, '%Y-%m-%d').date(), gender=gender, address=address, phone_number=phone_number)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient.patient_id

# Function to add a new doctor to the database
def add_doctor(db: Session, name: str, specialty: str, contact_info: str, phone_number: str):
    doctor = Doctor(name=name, specialty=specialty, contact_info=contact_info, phone_number=phone_number)
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor.doctor_id

# Function to schedule a new appointment between a patient and a doctor
def add_appointment(db: Session, patient_id: int, doctor_id: int, date: str, time: str, reason: str):
    appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, date=datetime.strptime(date, '%Y-%m-%d').date(), time=datetime.strptime(time, '%H:%M').time(), reason=reason)
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment.appointment_id

# Function to create a new medical record for an appointment
def add_medical_record(db: Session, appointment_id: int, diagnosis: str, treatment: str, notes: str = None):
    appointment = db.query(Appointment).filter_by(appointment_id=appointment_id).one()
    medical_record = MedicalRecord(patient_id=appointment.patient_id, doctor_id=appointment.doctor_id, appointment_id=appointment_id, diagnosis=diagnosis, treatment=treatment, notes=notes)
    db.add(medical_record)
    db.commit()
    db.refresh(medical_record)
    return medical_record.medical_record_id

# Click group definition for CLI commands
@click.group()
def cli():
    pass

# Command to register a new patient
@click.command()
@click.argument('name')
@click.argument('date_of_birth')
@click.argument('gender')
@click.argument('address')
@click.argument('phone_number')
def register_patient(name, date_of_birth, gender, address, phone_number):
    db = SessionLocal()
    patient_id = add_patient(db, name, date_of_birth, gender, address, phone_number)
    db.close()
    click.echo(f'Patient {name} registered successfully with ID {patient_id}.')

# Command to register a new doctor
@click.command()
@click.argument('name')
@click.argument('specialty')
@click.argument('contact_info')
@click.argument('phone_number')
def register_doctor(name, specialty, contact_info, phone_number):
    db = SessionLocal()
    doctor_id = add_doctor(db, name, specialty, contact_info, phone_number)
    db.close()
    click.echo(f'Doctor {name} registered successfully with ID {doctor_id}.')

# Command to schedule a new appointment
@click.command()
@click.argument('patient_id')
@click.argument('doctor_id')
@click.argument('date')
@click.argument('time')
@click.argument('reason')
def schedule_appointment(patient_id, doctor_id, date, time, reason):
    db = SessionLocal()
    appointment_id = add_appointment(db, patient_id, doctor_id, date, time, reason)
    db.close()
    click.echo(f'Appointment scheduled successfully with ID {appointment_id}.')

# Command to create a medical record for an appointment
@click.command()
@click.argument('appointment_id')
@click.argument('diagnosis')
@click.argument('treatment')
@click.argument('notes', required=False)
def create_medical_record(appointment_id, diagnosis, treatment, notes=None):
    db = SessionLocal()
    medical_record_id = add_medical_record(db, appointment_id, diagnosis, treatment, notes)
    db.close()
    click.echo(f'Medical record created successfully with ID {medical_record_id}.')

# Adding commands to the CLI group
cli.add_command(register_patient)
cli.add_command(register_doctor)
cli.add_command(schedule_appointment)
cli.add_command(create_medical_record)

# Main execution block
if __name__ == '__main__':
    init_db()  # Initialize the database
    cli()      # Run the CLI
