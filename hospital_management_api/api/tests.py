from django.test import TestCase
from django.contrib.auth.models import User
import unittest
import unittest
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client


# Create your tests here.

class DoctorSignUpTestCase(unittest.TestCase):
    def test_doctor_can_signup(self):

        user = User.objects.create_user(username='doctor1',
                                                    email='doctor@gmail.com',
                                                    password='DoctorPass')
        user.is_doctor = True
        user.save()

        
        self.assertEqual(user.is_doctor,True)

        def test_patient_cannot_signup(self):
            user = User.objects.create_user(user='patient2',
                                                        email='patient@gmail.com',
                                                        password='DPatientPass')
            user.is_doctor = True
            user.save()
            self.assertEqual(user.is_doctor,False)



class PatientCreationTestCase(unittest.TestCase):
    client = Client()
    def test_doctor_can_create_patient_login(self):

        doctor = User.objects.create_user(username='doctor3', email='doctor@example.com', password='password')

        patient = doctor.create_patient(username='patient3', email='patient@example.com', password='password')

        self.assertEqual(patient.is_doctor, False)

    def test_patient_can_use_login_to_access_system(self):
        patient = User.objects.create_user(username='patient2', email='patient@example.com', password='password')

        self.client.login(username='patient2', password='password')

        response = self.client.get('/api/patients/')

        self.assertEqual(response.status_code, 200)


class AppointmentBookingTestCase(unittest.TestCase):
    def test_patient_can_book_appointment_to_see_any_doctor(self):
        """
        A patient should be able to book an appointment to see any doctor.
        """
        patient = User.objects.create_user(username='patient100', email='patient@example.com', password='password')
        doctor = User.objects.create_user(username='doctor291', email='doctor@example.com', password='password')

        url = reverse('appointments-create')

        data = {
            'doctor': doctor.pk,
            'date': '2023-10-28',
            'time': '10:00 AM'
        }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 201)

    def test_only_doctor_who_booked_appointment_can_view_patient_information(self):
        """
        Only the doctor who booked an appointment should be able to view the patient's information.
        """
        patient = User.objects.create_user(username='patient1', email='patient@example.com', password='password')
