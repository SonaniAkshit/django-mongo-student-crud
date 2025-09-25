# student/models.py
from djongo import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    enrolment_no = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)

    def __str__(self):
        return self.name
