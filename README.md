# Ayulla
##Clone the repository to your local machine:
git clone https://github.com/Zamokuhle23/hospital_management_api.git

##Create a virtual environment:
 python3 -m venv venv

##Activate the virtual environment:
source venv/bin/activate

##Install the project's dependencies:
pip install -r requirements.txt

##Migrate the database:
python manage.py migrate

## To run unit tests:
## To test if Doctor Signs Up
python manage.py test api.tests.DoctorSignUpTestCase

## To test Creation of Patient
python manage.py test api.tests.PatientCreationTestCase

## To test Appointment Booking // There is an error for this test, there was no time to correct
python manage.py test api.tests.AppointmentBookingTestCase


##Start the development server:
python manage.py runserver

##Open a web browser and navigate to the following URL:
http://localhost:8000/

## to create a new doctor using the API:
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "username": "new_doctor",
    "email": "new_doctor@example.com",
    "is_doctor": true
  }' \
  http://localhost:8000/doctors/


  ##to book an appointment for a patient using the API:
  curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "patient": 1,
    "doctor": 2,
    "date": "2023-10-28",
    "time": "10:00 AM"
  }' \
  http://localhost:8000/appointments/

  

