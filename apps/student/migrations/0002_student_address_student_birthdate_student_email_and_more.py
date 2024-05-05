# Generated by Django 4.1.13 on 2024-05-02 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(db_column='address', default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='birthdate',
            field=models.DateField(db_column='birthdate', null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(db_column='email', default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], db_column='gender', default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.CharField(db_column='image', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(db_column='mobile', default='Unknown', max_length=100),
        ),
    ]
