from django.db import models

# Create your models here.
class Student(models.Model):
    gender_choices = (('male', 'male'), ('female', 'female'))
    student_ID = models.IntegerField(db_column="student ID", primary_key=True, null=False)
    name = models.CharField(db_column="student name", max_length=100, null=False)


    class Meta:
        managed = True
        db_table = "Student"


    def __str__(self):
        return f"student number:{self.student_ID}\t student name:{self.name}"