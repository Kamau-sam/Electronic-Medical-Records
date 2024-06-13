# Electronic Medical Records System

## Author

Samuel Kamau

## Project Overview

The Electronic Medical Records System is meticulously crafted to revolutionize the way healthcare facilities manage patient health information. By centralizing patient records, including appointments and comprehensive medical histories, this system streamlines operations, enhances accessibility, and improves patient care. Leveraging Python and SQLAlchemy, alongside SQLite for efficient database management, this system is perfectly suited for small to medium-sized healthcare practices seeking to modernize their record-keeping processes.

## Features

- **Patient Management**: Efficiently create, store, and retrieve detailed patient records.
- **Appointment Scheduling**: Seamlessly schedule and track appointments with ease.
- **Medical History Tracking**: Maintain a comprehensive history of each patient's medical conditions and treatments.
- **User-Friendly Interface**: A simple yet intuitive command-line interface (CLI) for quick access and management of records.

## Installation

To get started with the Electronic Medical Records System, follow these steps:

1. **Clone the Repository**
   bash git clone https://your-repository-url.git cd emr-system

2. **Install Dependencies**
   bash pip install -r requirements.txt

3. **Initialize the Database**
   bash python main.py init-db

4. **Run the Application**
   - **Register a New Patient**
     bash python main.py add-patient "John Doe"

## Usage

The system offers a variety of commands to manage patient and doctor records effectively. Here are a few examples:

- Registering a new patient:
  bash python cli.py register_patient "Diana Wambui" "1988-12-12" "F" "Nakuru" "0712345681"

- Registering a new doctor:
  bash python cli.py register_doctor "Dr. Peter Ochieng" "Orthopedics" "Molo" "0723456791"

## Contributing

We welcome contributions from the community Whether you're fixing bugs, improving documentation, or adding new features, we'd love to hear from you. Before contributing, please:

1. Fork the repository
2. Create a new branch for your feature or fix
3. Make your changes and submit a pull request

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
