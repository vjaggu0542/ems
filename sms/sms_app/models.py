from django.db import models
from django.contrib.auth.models import AbstractUser

class Customuser(AbstractUser):
    USER = (
        (1,'manager'),
        (2,'teamlead'),
        (3,'employee'),
    )

    user_type = models.CharField(choices=USER,max_length=220,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')



class Designation(models.Model):
     name = models.CharField(max_length=120)
     created_date = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.name
     
class Duration(models.Model):
     joining_date = models.CharField(max_length=120)
     end_date = models.CharField(max_length=120)
     def __str__(self):
            return self.joining_date + " To  " + self.end_date

class Employee(models.Model):
     admin = models.OneToOneField(Customuser,on_delete=models.CASCADE)
     address = models.TextField()
     gender = models.CharField(max_length=100)
     designation_id = models.ForeignKey(Designation,on_delete=models.DO_NOTHING)
     duration_id = models.ForeignKey(Duration,on_delete=models.DO_NOTHING)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
            return self.admin.first_name + " " + self.admin.last_name
     
    
class Teamlead(models.Model):
     admin = models.OneToOneField(Customuser,on_delete=models.CASCADE)
     address = models.TextField()
     gender = models.CharField(max_length=100)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
            return self.admin.username



