from django.db import models


# Create your models here.
class Student(models.Model):
    gender_choices = (('male', 'male'), ('female', 'female'))
    student_ID = models.IntegerField(db_column="student_ID", primary_key=True, null=False)
    name = models.CharField(db_column="student_name", max_length=100, null=False)
    gender = models.CharField(db_column="gender", max_length=100, default='Unknown', choices=gender_choices)
    birthdate = models.DateField(db_column="birthdate", null=True)
    mobile = models.CharField(db_column="mobile", max_length=100, default='Unknown')
    email = models.CharField(db_column="email", max_length=100, default='Unknown')
    address = models.CharField(db_column="address", max_length=100, default='Unknown')
    image = models.CharField(db_column="image", max_length=200, null=True)

    class Meta:
        managed = True
        db_table = "Student"
        app_label = 'student'

    def __str__(self):
        return f"student number:{self.student_ID}\t student name:{self.name} \t gender: {self.gender}"
