from django.db import models
from datetime import datetime
# Create your models here.

class Signup(models.Model):
    username = models.CharField(max_length=50)
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    email= models.CharField(max_length=100)
    pass1= models.CharField(max_length=30)
    pass2= models.CharField(max_length=30)
    date = models.DateField()

    def __str__(self):
        return self.fname

class Feedback(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    feedbackemail = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    feedback = models.Field()
    date_add = models.DateField()
    class Meta:
        db_table="feedback"

    def __str__(self):
        return self.first_name

class Contactus(models.Model):
    contactemail = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    date_add1 = models.DateField()

    class Meta:
        db_table="contact"

    def __str__(self):
        return self.fname