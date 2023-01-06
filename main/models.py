from django.db import models
    
# Create your models here.
class JobSeeker(models.Model):
    user_id = models.IntegerField()
    log_id = models.IntegerField(default=None, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, default=None, null=True)
    location = models.CharField(max_length=200, default=None, null=True)
    experience = models.CharField(max_length=100, default=None, null=True)
    skills = models.CharField(max_length=100, default=None, null=True)
    basic_edu = models.CharField(max_length=100, default=None, null=True)
    master_edu = models.CharField(max_length=100, default=None, null=True)
    other_qual = models.CharField(max_length=100, default=None, null=True)
    dob = models.CharField(max_length=50, default=None, null=True)
    Resume = models.CharField(max_length=100, default=None, null=True)
    photo = models.CharField(max_length=200, default=None, null=True)
    email = models.EmailField(max_length=100, default=None, null=True)
    password = models.CharField(max_length=100, default=None, null=True)
    class Meta:
        db_table = "jobseeker"

