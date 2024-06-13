# Electronic Medical Records System
# Author
Samuel Kamau

# Project Overview
The Electronic Medical Records System is designed to streamline the management of patient health information within healthcare facilities. It allows for the creation, storage, and retrieval of patient records, including appointments and medical histories. Built with Python and SQLAlchemy, this system utilizes SQLite for lightweight database management, making it ideal for small to medium-sized practices.

## Installation

Clone the repository to your local machine..

```bash
git clone https://your-repository-url.git
cd emr-system

```
Install the required packages...

```bash
pip install -r requirements.txt
```
Running the Application
Initialize the database.

```bash
python main.py init-db
```
To add a new patient, run:.

```bash
python main.py add-patient "John Doe"

```
## Usage

```
# python cli.py register_patient "Diana Wambui" "1988-12-12" "F" "Nakuru" "0712345681"

# returns 'geese'
python cli.py register_doctor "Dr. Peter Ochieng" "Orthopedics" "dr.peter@hospital.com" "0723456791"

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project is licensed under the MIT License. 
[MIT](https://choosealicense.com/licenses/mit/)
