from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class Doctor(AbstractBaseUser):
    is_doctor = models.BooleanField(default=False)
    def str(self):
     return self.username

class Patient(AbstractBaseUser):
    created_by = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='patients')
    def str(self):
        return self.username
    
class Appointment(models.Model):
   patient =  models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointments')
   doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointments')
   time = models.TimeField()
   date = models.DateField()

   def str(self):
      return f"Doctor {self.doctor} has appointment at {self.time} {self.date}:"



    



